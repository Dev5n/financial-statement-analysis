# financial-statement-analysis
This repository contains a Python script to analyze financial statements and calculate key ratios
import pandas as pd

# Load financial data (income statement, balance sheet, etc.)
df = pd.read_csv('financials.csv')

# Calculate key financial ratios
def calc_ratios(df):
    return {
        'Current Ratio': df['Current Assets'] / df['Current Liabilities'],
        'Debt-to-Equity': df['Total Liabilities'] / df['Total Equity'],
        'Gross Margin': df['Gross Profit'] / df['Revenue']
    }

ratios = calc_ratios(df)
print(ratios)
