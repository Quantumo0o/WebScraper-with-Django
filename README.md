# Django Web Scraping Project

## Overview

This Django project is designed to scrape product reviews from Flipkart and store the data in a Django database. The web application allows users to input a product name, fetch reviews from Flipkart, and display the scraped information.

## Project Components

### 1. Web Scraping

- **Libraries Used:**
  - `requests` for making HTTP requests
  - `BeautifulSoup` for parsing HTML content
  - `fake_useragent` for generating fake user agent strings

### 2. Django Web Application

- **Views:**
  - `say_hello`: Default view for rendering a template.
  - `index`: Main view for handling web scraping logic.

- **Templates:**
  - `index.html`: User interface template with a form for input and displaying scraped data.

### 3. Database Interaction

- **Django Model:**
  - `Review`: Model for defining the structure of the database table to store product reviews.

### 4. User Interface

- The project uses Django templates to dynamically render HTML pages.
- Users can input a product name through a form, and the scraped data is presented on the web page.

### 5. Logging

- Python's `logging` module is utilized to log information about the scraping process and error handling.

### 6. Additional Notes

- The code includes handling HTTP requests using `http.client`.
- A fake user agent is generated using the `fake_useragent` library to mimic a web browser's user agent string.

## Getting Started

Follow the steps below to set up and run the project locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-project.git
