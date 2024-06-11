import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://josaa.admissions.nic.in/applicant/seatmatrix/instituteview.aspx' 
response = requests.get(url)


soup = BeautifulSoup(response.content, 'html.parser')

# Find all rows in the table
rows = soup.find_all('tr')

# List to hold the extracted institution names
institution_names = []

# Iterate over each row
for row in rows:
    cols = row.find_all('td')
    if len(cols) > 1:  # Ensure the row has more than one column
        span = cols[1].find('span')
        if span:
            # Extract the full institution name
            institution_name = span.get_text(separator=" ", strip=True).split(" ", 1)[1]
            institution_names.append({'Institution Name': institution_name})

# Create a DataFrame from the extracted institution names
df = pd.DataFrame(institution_names)

# Save the DataFrame to an Excel file
df.to_excel('institutions.xlsx', index=False)

print('Data successfully saved to institutions.xlsx')
