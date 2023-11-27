import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
names=[]
descriptions=[]
# Fetch URL
result = requests.get("https://plarium.com/en/blog/popular-games/")

#save page content
src = result.content

#Create soup
soup = BeautifulSoup(src,"lxml")

# Find all elements with class "css-rgqwpc" that contain game names
name = soup.find_all("h3")

for nam in name:
    names.append(nam.text)
    description1= nam.find_next_sibling().text
    description2= nam.find_next_sibling().find_next_sibling().text
    description3 = description1+description2
    descriptions.append(description3)

print(descriptions)

#import into csv
file_list= [names,descriptions]
export = zip_longest(*file_list)
#write pathfolder
with open("D:\\datascience\\web scraping\\scrapping most popular played games on epicgames\data.csv","w") as file:
    wr =csv.writer(file)
    wr.writerow(["Name","Description"])
    wr.writerows(export)

