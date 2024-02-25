import csv
import pyodbc

# Function to save a table to a CSV file
def save_table_to_csv(cursor, table_name, csv_file_name):
    query = f"SELECT * FROM [{table_name}]"
    cursor.execute(query)
    
    # Fetch the rows from the table
    rows = cursor.fetchall()
    
    # Get column names
    columns = [column[0] for column in cursor.description]
    
    # Writing to CSV
    with open(csv_file_name, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(columns)  # write the column names
        for row in rows:
            csvwriter.writerow(row)

# Path to your .mdb file
mdb_file_path = 'NCAP4-27-10.mdb'

# Connection string
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    rf'DBQ={mdb_file_path};'
)

# Connect to the .mdb file
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Retrieve list of tables and convert each to a CSV file
tables = cursor.tables(tableType='TABLE').fetchall()
for table in tables:
    table_name = table.table_name
    csv_file_name = f"{table_name}-{mdb_file_path[:-4]}.csv"
    print(f"Converting {table_name} to {csv_file_name}...")
    save_table_to_csv(cursor, table_name, csv_file_name)

# Clean up
cursor.close()
conn.close()

print("Conversion complete.")