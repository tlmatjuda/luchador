import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine


TARGET_PARSER = 'html.parser'
JOB_LISTINGS_URL = 'http://quotes.toscrape.com/'
FILES_OUTPUT = 'files-output'
CSV_FILE_PATH = f'{FILES_OUTPUT}/quotes.csv'
DATABASE_URI = f'sqlite:///{FILES_OUTPUT}/quotes.db'


def scrape_quotes():
    # Let's perform an HTTP GET to retrieve information from the target page.
    # We are also going to be using the HTML Parser to that we read infor as HTML
    response = requests.get(JOB_LISTINGS_URL)
    soup = BeautifulSoup(response.text, TARGET_PARSER)

    # Let's get our data collection variable ready.
    quotes = []

    # Go through the HTML page to start extracting our the data we are looking for, the rest we throw away.
    for quote in soup.find_all('div', class_='quote'):

        # Pull out pieces of data for each Qute record we find.
        text = quote.find('span', class_='text').text.strip()
        author = quote.find('small', class_='author').text.strip()
        tags = [tag.text for tag in quote.find_all('a', class_='tag')]

        # While we are still in the loop, we also want to create a single Quote record and then APPEND or ADD to our Quotes collection.
        quotes.append({
            'text': text,
            'author': author,
            'tags': ', '.join(str(item) for item in tags)
        })

    return quotes

# This function accepts the given quotes and writes to a CSV file.
# It makes use of the Pandas Data Frame to map or transform to CSV format and write to a file.
def save_to_csv(quotes, filename=CSV_FILE_PATH):
    df = pd.DataFrame(quotes)
    df.to_csv(filename, index=False)

# Assyming that your have an SQL Lite DB createed with the 'quotes' name
# And you have a 'quotes' table as created as well...
# We will also go and insert data into the SQL Lite Table
def save_to_sql(quotes, table_name='quotes'):
    engine = create_engine(DATABASE_URI)
    df = pd.DataFrame(quotes)
    df.to_sql(table_name, engine, if_exists='replace', index=False)


# Script entry point.
# This is where the program starts
if __name__ == "__main__":
    quotes = scrape_quotes()
    print(f'We have found {len(quotes)} Quotes')
    print('Now going to write to CSV..')
    save_to_csv(quotes)

    print('Now going to write to SAL Lite Database...')
    save_to_sql(quotes)

    print(f'DONE & DONE! Please check the CSV file in ; {CSV_FILE_PATH}')



