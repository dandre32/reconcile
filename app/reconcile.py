import pandas as pd

def reconcile(csv_file, excel_file):
    # Read CSV file
    csv_data = pd.read_csv(csv_file)

    # Read Excel file
    excel_data = pd.read_excel(excel_file, sheet_name='Statement')

    # Clean the CSV data
    csv_data['Transaction Amount'] = csv_data['Transaction Amount'].replace('[\$,)]', '', regex=True).replace('[(]', '-', regex=True).astype(float)

    # Clean the Excel data
    excel_data.columns = excel_data.iloc[0]  # Set the first row as column headers
    excel_data = excel_data[1:]  # Remove the header row
    excel_data['PAID COMMISSION'] = excel_data['PAID COMMISSION'].replace('[\$,)]', '', regex=True).replace('[(]', '-', regex=True).astype(float)

    # Rename columns for clarity
    csv_data.rename(columns={'Transaction Amount': 'CSV_Transaction_Amount'}, inplace=True)
    excel_data.rename(columns={'PAID COMMISSION': 'Excel_Transaction_Amount'}, inplace=True)

    # Combine data into a single DataFrame
    combined_data = pd.merge(csv_data, excel_data, how='outer', left_on='CSV_Transaction_Amount', right_on='Excel_Transaction_Amount', suffixes=('_CSV', '_Excel'))

    # Identify discrepancies
    discrepancies = combined_data[combined_data['CSV_Transaction_Amount'] != combined_data['Excel_Transaction_Amount']]

    return discrepancies
