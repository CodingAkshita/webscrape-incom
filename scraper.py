#Importing
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

#Assigning the value of the constant
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/Users/apoorvelous/Downloads/chromedriver")
browser.get(START_URL)

time.sleep(11)

# function definition to identify specific part of the given webpage to extract data from 
def scrape():
    headers = ["Name", "Distance", "Mass", "Radius"]
    #Creating an empty list
    starData = []
    #Running a nested loop
    for i in range(0, 97):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ulTag in soup.find_all("ul", attrs = {"class", "exoplanet"}):
                  liTags = ulTag.find_all("li")   
                  tempList = []     
                  for index, liTag in enumerate(liTags):
                      if index == 0:
                          tempList.append(liTag.find_all("a")[0].contents[0])
                      else:
                          try:
                              tempList.append(liTag.contents[0]) 
                          except:
                              tempList.append("")                             
                  starData.append(tempList) 
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(starData)  
        
#function call
scrape()                                  