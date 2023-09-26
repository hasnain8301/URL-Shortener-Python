# SolidEcomm

## Introduction

This project involves processing Yearly Order, Cost, and Purchase Sheets by Store. There are two types of sheets we have to process:

1. Yearly Order Cost and Purchase Sheet.
2. Order Cost Sheet of suppliers.

## Project Technical Details

### Excel Files and Directories
- **Order Sheets:** There will be an Excel file inside the folder `data_dir/ordersheet`. Inside this Excel file, there is a sheet named `2023 Orders` that contains two columns we need to process: `ASIN` and `Cost/ASIN`.
- **Suppliers' Cost Sheets:** There will be multiple Excel data sheets from suppliers in which we will be provided with the `ASIN` and `Cost` columns.

The process will involve taking an `ASIN` from the supplier's Excel file and finding the maximum cost of all time against this ASIN from the `Yearly Order Cost and Purchase Sheet`. After finding the maximum cost, we need to store it in the same row inside the `Suppliers' Cost Sheets` for the same ASIN. In cases where the `ASIN` inside the `Suppliers' Cost Sheets` file doesn't exist in the `Order Sheets` file, we should update the `Cost` column with "no sales were found."

## How to Run Scripts

Follow these steps to run the scripts:

1. Create a virtual environment (you can use pipenv).
2. Install the required libraries from the "requirements.txt" file using this command:
  ```
    pip install -r requirements.txt
  ```
3. Execution:
- To run the Crawler (to retrieve PDFs and their .txt files), use the following command:
  ```
  python process.py
  ```

This README file provides clear instructions and details about the project structure, files, and how to run the scripts. Feel free to make any additional adjustments to suit your project's specific needs.
