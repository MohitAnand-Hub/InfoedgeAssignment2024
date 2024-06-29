import pandas as pd

# Load data from Excel into a pandas dataframe
excel_file = 'sales_data.xlsx'  # Replace with your Excel file path
df = pd.read_excel(excel_file)

# Initialize dictionaries to store monthly totals
monthly_totals = {}

# Calculate monthly totals
for index, row in df.iterrows():
    date = row['Date']
    sales = row['Sales']
    month_year = pd.to_datetime(date).strftime('%Y-%m')  # Get month and year in YYYY-MM format
    
    # Extract year and month
    year, month = month_year.split('-')
    
    if year not in monthly_totals:
        monthly_totals[year] = {}
    
    if month not in monthly_totals[year]:
        monthly_totals[year][month] = 0
    
    monthly_totals[year][month] += sales

# Display the data in the specified format
print(f"{'Year':<10} {'Jan':<10} {'Feb':<10} {'Mar':<10} {'Apr':<10} {'May':<10} {'Jun':<10} {'Jul':<10} {'Aug':<10} {'Sep':<10} {'Oct':<10} {'Nov':<10} {'Dec':<10}")
print('-' * 130)

# Iterate through years and print monthly totals
for year in sorted(monthly_totals.keys()):
    print(f"{year:<10}", end=' ')
    for month in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
        print(f"{monthly_totals[year].get(month, 0):<10}", end=' ')
    print()
