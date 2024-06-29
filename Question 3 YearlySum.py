import pandas as pd

# Load data from Excel into a pandas dataframe
excel_file = 'sales_data.xlsx'  # Replace with your Excel file path
df = pd.read_excel(excel_file)

# Initialize dictionaries to store monthly and yearly totals
monthly_totals = {}
yearly_totals = {}

# Calculate monthly and yearly totals
for index, row in df.iterrows():
    date = row['Date']
    sales = row['Sales']
    month_year = pd.to_datetime(date).strftime('%Y-%m')  # Get month and year in YYYY-MM format
    
    # Extract year and month
    year, month = month_year.split('-')
    
    # Initialize monthly total if not already initialized
    if year not in monthly_totals:
        monthly_totals[year] = {}
    
    if month not in monthly_totals[year]:
        monthly_totals[year][month] = 0
    
    # Add sales to monthly total
    monthly_totals[year][month] += sales
    
    # Initialize yearly total if not already initialized
    if year not in yearly_totals:
        yearly_totals[year] = 0
    
    # Add sales to yearly total
    yearly_totals[year] += sales

# Display the data in the specified format
print(f"{'Year':<10} {'Jan':<10} {'Feb':<10} {'Mar':<10} {'Apr':<10} {'May':<10} {'Jun':<10} {'Jul':<10} {'Aug':<10} {'Sep':<10} {'Oct':<10} {'Nov':<10} {'Dec':<10} {'Yearly':<10}")
print('-' * 140)

# Iterate through years and print monthly and yearly totals
for year in sorted(monthly_totals.keys()):
    print(f"{year:<10}", end=' ')
    yearly_total = 0
    for month in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
        monthly_total = monthly_totals[year].get(month, 0)
        yearly_total += monthly_total
        print(f"{monthly_total:<10}", end=' ')
    print(f"{yearly_total:<10}")