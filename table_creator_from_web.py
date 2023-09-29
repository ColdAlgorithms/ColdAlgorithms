import requests
from bs4 import BeautifulSoup
import pandas as pd
from lxml import html


# Give parameters
hyper_link = ''          # Give your hyper link
your_subject = ''        # Give the subject that defines your hyper link
xpath = ''               # Give the full xpath for the file name that we creates for you
url = f'{hyper_link}/{your_subject}'

# Get the html table content from the web site
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')

# Get the xpath content from the web site
xpath_content = html.fromstring(response.content)
xpath_element = xpath_content.xpath(xpath)

# Get soup data
table = soup.find_all("table")[1]
h1_headings = soup.find_all('a')

# Read table
if table:
    rows = table.find_all('tr')
    data = []    
    for row in rows:
        cols = row.find_all(['th', 'td'])
        cols = [col.text.strip() for col in cols]
        data.append(cols)
    
    # Prepare pandas dataframe 
    headers = data[0]
    data = data[1:]
    df = pd.DataFrame(data, columns=headers)
else:
    print("No table has been finded.")

# Save File
filename = xpath_element[0].text_content() + ".xlsx"
df.to_excel(filename)
