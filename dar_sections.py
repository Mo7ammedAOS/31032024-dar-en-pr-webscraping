from bs4 import BeautifulSoup as Bs
import requests
import csv
import pandas as pd

url = 'https://www.dar-engineering.com/portfolio_architecture.html'
html_dar = requests.get(url).text
soup = Bs(html_dar, 'html5lib')

holder = soup.find_all('div', {'id': 'portfolio'})
file = 'dar_projects.csv'

with open(file, 'w', encoding='utf-8', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['PROJECT CATEGORY', 'PROJECT NAME'])
    for item in holder:
        section_name = item.h1.text.strip()
        csv_writer.writerow([section_name, ''])
        
        section_projects = item.find_all('div', {'id': 'proholder'})
        for section in section_projects:
            projects = section.find_all('a')
            for element in projects:
                project_name = element.div.h2.text.strip()
                csv_writer.writerow(['', project_name])

print("CSV file 'dar_projects.csv' has been created successfully.")