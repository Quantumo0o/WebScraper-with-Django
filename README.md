# Django Web Scraping Project

## Table of Contents

1. [Demo](#demo)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Dependencies](#dependencies)
6. [Contributing](#contributing)
7. [License](#license)

## Demo

### 1. Saved CSV Data

![Saved CSV Data](png/Saved%20CSV%20data.png)

### 2. Product Detailed Review Webpage

![Product Detailed Review Webpage](png/Product%20detailed%20review.png)

### 3. Product Search Page

![Product Search Page](png/Product%20search%20page.png)



## Features

In this section, highlight the key features of your Django Web Scraping project:

- **Web Scraping with Ease:** Utilize `requests` and `BeautifulSoup` for seamless web scraping of product reviews from Flipkart.
- **Dynamic User Interface:** Leverage Django templates to create an interactive user interface, allowing users to input product names and view scraped data.
- **Data Storage in CSV:** Save scraped data efficiently in CSV files within the `CSV` folder. The CSV files automatically append data for repeated queries.
- **Duplicate Handling with Pandas:** Implement pandas to manage and remove duplicate data, ensuring clean and unique datasets.
- **Logging and HTTP Handling:** Employ Python's `logging` module for comprehensive logs on the scraping process. Manage HTTP requests using `http.client` for enhanced control.

## Installation

Follow these simple steps to get your project up and running:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/your-project.git
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd your-project
    ```

3. **Create a Virtual Environment (Optional but Recommended):**

    ```bash
    python -m venv venv
    ```

4. **Activate the Virtual Environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. **Install Project Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

6. **Run the Development Server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the Web Application:**

    Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

To use the web scraping functionality of the project:

1. Open your web browser and go to `http://127.0.0.1:8000/`.
2. You will be greeted with the main page, featuring a form to enter the product name.
3. Input the desired product name and submit the form.
4. The application will scrape Flipkart for product reviews, display the results on the page, and append the data to the corresponding CSV file.
5. The CSV files in the `CSV` folder will store the scraped data for each unique query.

Feel free to explore different product queries, and the application will dynamically handle the scraping and data storage.

## Dependencies

Detail the key dependencies used in your project:

- `requests`
- `BeautifulSoup`
- `fake_useragent`
- `http.client`
- `pandas`

## Contributing

If you'd like to contribute to the project or report issues, please follow our [Contribution Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE). See the [LICENSE](LICENSE) file for more details.

---
