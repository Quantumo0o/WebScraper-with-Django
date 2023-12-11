
# Import necessary modules and libraries
import os
from django.shortcuts import render
from django.http import HttpResponse 
import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import logging
import http.client
import time
import pandas as pd

def home(request):
    return render(request,'index.html')


# Main view function for handling web scraping logic
def index(request):
    print('start')
    # Declare global variables for storing page-related information
    global flipkartPage
    global count
    global searchString
    global page
    
    # Check if the request method is POST
    if request.method == 'POST':
        # Check if the 'next' button is clicked
        if request.method == 'POST' and 'next' in request.POST:
            count += 1
        else:
            count = 0
            page = 0
        
        # If count is 0, extract and clean the search query from the form
        if count == 0:
            searchString = request.POST.get('content', '').replace(" ", "")
            print(searchString)
        headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Connection': 'keep-alive',
                }

        try:
            # Handle Flipkart URL construction and request
            if (count == 0 or count == 8) and searchString != "":
                count = 0
                
                #ua = UserAgent()
                #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
                #flipkart_url = 'https://www.flipkart.com/search?q=' + searchString + '&page=' + str(page)
                #flipkart_url = str(flipkart_url)
                page = page + 1
                print("0")
                try:
                    # Make a request to Flipkart and get the response
                    conn = http.client.HTTPSConnection("www.flipkart.com")
                    conn.request("GET", "/search?q=" + searchString + '&page=' + str(page),headers=headers)
                    response = conn.getresponse()
                    print(response.status, response.reason)
                    flipkartPage = response.read()
                    conn.close()
                    print("1")

                except requests.exceptions.HTTPError as errh:
                    print(f"HTTP Error: {errh}")
                    print("Response Content:", requests.Response.content)
                    print("Status Code:", requests.Response.status_code)
                except requests.exceptions.RequestException as err:
                    print(f"An error occurred: {err}")

            # Parse HTML content from Flipkart
            flipkart_html = bs(flipkartPage, "html.parser")
            bigboxes = flipkart_html.findAll("div", {"class": "_1AtVbE col-12-12"})
            print(len(bigboxes))
            del bigboxes[0:3]
            box = bigboxes[count]
            print("productLink:", box.div.div.div.a['href'])

            # Request individual product page
            conn = http.client.HTTPSConnection("www.flipkart.com")
            productLink = box.div.div.div.a['href']
            conn.request("GET", productLink,headers=headers)
            prodRes1 = conn.getresponse()

            # Decode the response content
            prodRes = prodRes1.read().decode("utf-8")
            conn.close()

            # Parse product page HTML
            prod_html = bs(prodRes, "html.parser")
            commentboxes = prod_html.find_all('div', {'class': "_16PBlm"})
            productprice = prod_html.find_all('div', {'class': "_30jeq3 _16Jk6d"})[0].text
            productname = prod_html.find_all('span', {'class': "B_NuCI"})[0].text
            img_tag = prod_html.find_all('div', {'class': '_1BweB8'})[0].div.img['src']

            # Create a CSV file to store data
            filename= os.path.join("csv",searchString+".csv")
            if not os.path.exists('csv'):
                os.makedirs('csv')
            with open(filename,"a",encoding="utf-8") as fw:
                headers = "Product, Customer Name, Rating, Heading, Comment \n"
                fw.write(headers)

            reviews = []

            print(len(commentboxes))
            # Loop through comment boxes and extract information
            for commentbox in commentboxes:
                try:
                    print("1")
                    # Extract customer name
                    name = commentbox.find_all('p', {'class': '_2sc7ZR _2V5EHH'})[0].text

                except:
                    name = "no name"
                    logging.info("name")

                try:
                    print("2")
                    # Extract rating
                    rating = commentbox.div.div.div.div.text

                except:
                    rating = 'No Rating'
                    logging.info("rating")

                try:
                    print("3")
                    # Extract comment heading
                    commentHead = commentbox.div.div.div.p.text

                except:
                    commentHead = 'No Comment Heading'
                    logging.info(commentHead)
                try:
                    print("4")
                    # Extract customer comment
                    comtag = commentbox.div.div.find_all('div', {'class': ''})
                    custComment = comtag[0].div.text
                except Exception as e:
                    logging.info(e)
                    custComment = 'No Comment'

                print("5")
                mydict = {"Product": searchString, "Name": name, "Rating": rating, "CommentHead": commentHead,
                        "Comment": custComment}
                print("6")
                reviews.append(mydict)
                print("7")
                x = searchString + "," + name + "," + rating + "," + commentHead + ',"' + custComment+'"'
                print("8")
                with open(filename, "a", encoding="utf-8") as fw:
                    fw.write(x + '\n')
                print("9")
                print(filename)
                duplicate(filename)

            logging.info("log my final result {}".format(reviews))

            # Render the template with the scraped data
            return render(request, 'index.html', {'reviews': reviews[0:(len(reviews)-1)], 'productname': productname, 'price': productprice, 'img_tag': img_tag})

        except Exception as e:
            logging.info(e)
            print(e)
            message = 'Please Enter Product'
            print(message)
            return render(request, 'index.html', {'message': message})

    else:
        return render(request, 'index.html')
    

def duplicate(filename):
    print("1")
    data = pd.read_csv(filename)
    data.drop_duplicates(inplace=True)
    data.to_csv(filename, index=False)

    
