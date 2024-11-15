# import pandas as pd
# import sys


# def main():
#     # Get input from user
#     url = input("Enter the URL: ").strip()

#     # Scrape tables and let the user choose one
#     try:
#         tables = scrape_tables(url)

#         if not tables:
#             sys.exit("No tables found on the page.")

#         print("\nAvailable tables:")
#         for i, table in enumerate(tables):
#             print(f"Table {i}: {table.shape[0]} rows, {table.shape[1]} columns")

#         table_index = int(
#             input("\nSelect the table number you want to scrape (0, 1, ...): ")
#         )
#         selected_table = tables[table_index]

#         # Display available columns
#         print("\nAvailable columns:")
#         for column in selected_table.columns:
#             print(f"- {column}")

#         columns = input(
#             "\nEnter the columns to be displayed (comma-separated): "
#         ).split(",")
#         columns = [col.strip() for col in columns]  # Clean up column names

#         # Convert selected table to CSV
#         csv_file = convert_to_csv(selected_table, "scraped_table")
#         data = read_csv_file(csv_file)

#         if not columns[0]:  # If no specific columns are provided
#             print(data.head(10))  # Print first 10 rows of the full data
#         else:
#             # Ensure columns entered by the user exist in the data
#             missing_columns = [col for col in columns if col not in data.columns]
#             if missing_columns:
#                 print(
#                     f"Warning: The following columns are not found in the data: {missing_columns}"
#                 )
#                 print("Displaying first 10 rows of available columns.")
#                 print(data.head(10))
#             else:
#                 # Display only the specified columns
#                 display_columns = data[columns]
#                 print(display_columns.head(10))

#     except ValueError as e:
#         print(f"Error: {e}.")
#     except Exception as e:
#         print(f"An error occurred: {e}")


# def scrape_tables(url):
#     """
#     Scrape all tables from the URL and return them as a list of DataFrames.
#     """
#     try:
#         tables = pd.read_html(url)
#         return tables
#     except Exception as e:
#         print(f"Failed to scrape tables from {url}: {e}")
#         return []  # Return an empty list if no tables are found


# def convert_to_csv(table, filename):
#     """
#     Convert the scraped table to a CSV file and return the filename.
#     """
#     csv_filename = f"{filename}.csv"
#     table.to_csv(csv_filename, index=False)
#     return csv_filename


# def read_csv_file(csv_file):
#     """
#     Read the CSV file and return the data as a pandas DataFrame.
#     """
#     return pd.read_csv(csv_file)


# if __name__ == "__main__":
#     main()


import pandas as pd
import sys
import sys 
def main():
    # Get input from the user 
    url = input("Enter the URL: ").strip()
    try:
        tables = scrape_tables(url)
def main():
    url = input("Enter the URL : ").

def main():
    # Get input from user
    url = input("Enter the URL: ").strip()
    # Get the inpt
    # Scrape tables and let the user choose one
    try:
        tables = scrape_tables(url)

        if not tables:
            sys.exit("No tables found on the page.")

        # Display table names (you can customize this based on your requirements)
        print("\nAvailable tables:")
        for i, table in enumerate(tables):
            print(
                f"Table {i}: {table.columns.tolist()}"
            )  # Show column names of each table

        table_name = input(
            "\nEnter the exact column name of the table you want to scrape: "
        ).strip()

        # Identify the table that contains the specified column name
        selected_table = None
        for table in tables:
            if table_name in table.columns:
                selected_table = table
                break

        if selected_table is None:
            sys.exit(f"No table found with the column name '{table_name}'.")

        # Display available columns of the selected table
        print("\nAvailable columns:")
        for column in selected_table.columns:
            print(f"- {column}")

        column_name = input("\nEnter the column name to be displayed: ").strip()

        # Convert selected table to CSV
        csv_file = convert_to_csv(selected_table, "scraped_table")
        data = read_csv_file(csv_file)

        if column_name in data.columns:
            print(
                data[[column_name]].head(10)
            )  # Print first 10 rows of the specified column
        else:
            print(f"Column '{column_name}' does not exist in the data.")

    except ValueError as e:
        print(f"Error: {e}.")
    except Exception as e:
        print(f"An error occurred: {e}")


def scrape_tables(url):
    """
    Scrape all tables from the URL and return them as a list of DataFrames.
    """
    try:
        tables = pd.read_html(url)
        return tables
    except Exception as e:
        print(f"Failed to scrape tables from {url}: {e}")
        return []  # Return an empty list if no tables are found


def convert_to_csv(table, filename):
    """
    Convert the scraped table to a CSV file and return the filename.
    """
    csv_filename = f"{filename}.csv"
    table.to_csv(csv_filename, index=False)
    return csv_filename


def read_csv_file(csv_file):
    """
    Read the CSV file and return the data as a pandas DataFrame.
    """
    return pd.read_csv(csv_file)


if __name__ == "__main__":
    main()
