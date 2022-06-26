#importing necessary modules and libraires
from bs4 import BeautifulSoup
import requests
import csv
import os

#using requests to fetch source code and using the lxml parser
source = requests.get('https://cdn.jsdelivr.net/gh/younginnovations/internship-challenges@master/data-analysis/scrape-it/exampledata.html').text
soup = BeautifulSoup(source, 'lxml')

#print(soup.prettify())

#creating folder, csv file and parsing html rows to csv file
os.mkdir('out')
csv_file = open('out/'+'data.csv', 'w', newline='')
csv_writer = csv.writer(csv_file,delimiter=",")
new_list=[]
for row in soup.find_all('tr'):
  local_list=[]
  for t_data in row.find_all('td'):
      local_list.append(t_data.text)
  new_list.append(local_list)    

for item in new_list:
  csv_writer.writerow(item)
csv_file.close()