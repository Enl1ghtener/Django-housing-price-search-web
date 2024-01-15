# Project Name

Brief Project Overview: This project utilizes the Django framework to create a web application for querying housing price information in various cities. It involves web scraping to collect housing price data. The backend reads and processes the data, passing it to the frontend for display and generating line charts.

# README.md同时有以下语言的版本
- EN [English](README_EN.md)
- CN [简体中文](README_CN.md)


## How to Run

Below are the basic steps to run the project locally:

1. Clone the project to your local machine:

    ```bash
    git clone [https://github.com/your-username/your-repo.git](https://github.com/Enl1ghtener/Django-housing-price-search-web)
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repo
    ```

3. Create a virtual environment (optional):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser to view the project.

## Project Structure

Provide a brief explanation of the project's directory structure and main files.

- `Django_first`: Main project directory
    - `Django_first`: Django framework
    - `crwal`: Web scraping
    - `stu`: Main application directory
    - `templates/`: HTML template files
    - `static/`: Static files (CSS, JS, images, etc.)
    - `views.py`: View functions
    - ...
  - `manage.py`: Django management script
  - `db.sqlite3`: Database

## Data Crawling and Processing

Data is obtained through the `crwal_houseprice.py` spider program. Due to the variation in city URLs, only 15 cities were manually crawled.

## Notes

Apart from the city query feature, the project also includes a login and register functionality for student testing purposes. The query functionality is also implemented within the `stu` app.

The code only has Chinese comments.

This is a practice project and may have some shortcomings, with potential updates in the future.



## License

MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
