"""
-> Web Scraping Project
-> To create a web scraper that scrapes data from a website and saves it in a csv file and then read the csv file and print first 10 rows of the data.
-> The data to be scraped is the list of all the books of Agatha Christie on the Wikipedia.
"""

import pandas as pd
import sys


def main():
    url = input("Enter the url: ")
    word_match = input("Enter the word to match: ")
    if word_match == "":
        sys.exit("Please enter a word to match")
    columns = input("Enter the columns to be displayed: ").split(",")
    new_columns = []
    table = read_HTML(url, word_match)  
    csv_file = convert_to_csv(table, word_match)
    data = read_csv_file(csv_file)
    if columns[0] == "":
        print(data.head(10))
    else:
        for column in columns:
            column = column.strip()
            new_columns.append(column)
        display_columns = data[new_columns]
        print(display_columns.head(10))


def read_HTML(url, word_match):
    tables = pd.read_html(url, match=word_match)
    return tables[0]


def convert_to_csv(table, word_match):
    table.to_csv(word_match + ".csv", index=False)
    return word_match + ".csv"


def read_csv_file(csv_file):
    books = pd.read_csv(csv_file)
    return books


if __name__ == "__main__":
    main()
