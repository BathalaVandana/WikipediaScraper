from project import read_HTML, convert_to_csv, read_csv_file
import pandas as pd


tables = pd.read_html(
    "https://en.wikipedia.org/wiki/Agatha_Christie_bibliography",
    match="Christie's novels",
)

books = pd.read_csv("Christie's novels.csv")


def test_read_HTML():
    expected_table = tables[0]
    actual_table = read_HTML(
        "https://en.wikipedia.org/wiki/Agatha_Christie_bibliography",
        "Christie's novels",
    )
    assert actual_table.equals(expected_table)


def test_convert_to_csv():
    assert convert_to_csv(tables[0], "Christie's novels") == "Christie's novels.csv"


def test_read_csv_file():
    expected_books = books
    actual_books = read_csv_file("Christie's novels.csv")
    assert actual_books.equals(expected_books)
