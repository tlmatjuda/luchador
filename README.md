# Quotes Scraper

A Python script to scrape famous Quotes by various people from a website, save them into a CSV file, and store them in a SQL database.
</br>

## Tech Stack

- Python 3.x
- SQL Lite 3
</br>

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/tlmatjuda/luchador.git
   cd luchador
   ```
2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```
</br>

## Usage


1. Run the scraper:

   ```bash
   python scrapper.py
   ```
2. Check for the output files in : `./files-output`and open the CSV file `quotes.csv`  to check out the content 
3. Connec the SQL Lite 3 database `quotes.db` and check the records with :

    ```bash
   SELECT * FROM quotes;
   ```
</br>

## Conlusion

That's it on a simple web scrapper that can save to CSV file or store to Database.
