 # Importing all libaraies from python

import requests    
from bs4 import BeautifulSoup
import pandas as pd  

# Accessing all the pages url

urlLst=[]

link1="https://www.timesjobs.com/candidate/job-search.html?from=submit&luceneResultSize=25&postWeek=60&searchType=Home_Search&cboPresFuncArea=35&pDate=Y&sequence="
link2="&CountStart="

# This Store The url in a list

for pages_num in range(1,381):
    main_url = link1+str(pages_num)+link2+str(pages_num)
    urlLst.append(main_url)

# Assigning Variables

AllDictValues=[]
jobTitles = "No Data"
CompanyName="No Data"
Experience="No Data"
location = "No Data"
JobDescription="No Data"
KeySkills= "No Data"

# Fetching all the url of all pages

for con in urlLst:
    print(con)
    response = requests.get(con).text
    print(response)
    convertedData = BeautifulSoup(response,'lxml')
    print(convertedData)
    allContent = convertedData.find_all('li',class_="clearfix job-bx wht-shd-bx")
    print(allContent)


    for value in allContent:
        jobTitles = value.find('a').text   # Extracting all the job titles.
        CompanyName=value.find('h3',class_="joblist-comp-name").text   # Extracting Company Name of all pages
        
        # Extracting All pages experience
        exp = value.find('li').text   
        Experience = exp.split("card_travel")[1]

        # Extracting Location of all pages
        location = value.find('ul',class_="top-jd-dtl clearfix").text
        Location=location.split("location_on")[1]
      
        # Extracting Job Description
        JobDescriptionElement =value.find('ul',class_="list-job-dtl clearfix")
        JobDescriptionSpliting = JobDescriptionElement.find('li').text 
        JobDescription= JobDescriptionSpliting.split('Job Description')[1]
        KeySkills = value.find('span',class_="srp-skills").text    # Extracting Key Skills

       
        ScrapData = {                       # keeping all the data in a dictionary.
            "Job-Title":jobTitles,
            "Company Name": CompanyName,
            "Experience":Experience,
            "Location":Location,
            "Job Description":JobDescription,
            "Key Skills":KeySkills
        }
         
        AllDictValues.append(ScrapData)  # This Append all the data to a list

print(AllDictValues)

data_frame= pd.DataFrame(AllDictValues)  # Generate the data of list data

data_frame.to_excel('scrapedData.xlsx')  # convert all the data in excel sheet

print("Congratulation!  your data has been Sucessfully stored in 'scrapedData' excell file.")





    


