import os, pandas as pd

# Step 1: Create some data (like a table)
'''data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Manila', 'Cebu', 'Davao']
}

df = pd.DataFrame(data)

# Step 2: Save this as an Excel file
df.to_excel('new_file.xlsx', index=False, engine='openpyxl')'''

new_rows = pd.DataFrame([{"Name": "Diana", "Age": 19, "City": "Baguio"}])
path = "new_file.xlsx"

if os.path.exists(path):
    # If the file exists, append the new rows
    old = pd.read_excel(path, engine='openpyxl')
    combined = pd.concat([old, new_rows], ignore_index=True)
else:
    # If the file does not exist, create a new DataFrame
    combined = new_rows
    
# Save the combined DataFrame to the Excel file
combined.to_excel(path, index=False, engine='openpyxl')
# Read the Excel file
df = pd.read_excel(path, engine='openpyxl')

# Show the data
print(df)

