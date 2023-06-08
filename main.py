import csv
import pprint
import json
import os

os.mkdir("cleared")

for year in range(2012, 2022):
    datasetHaveWorkedLanguage = {}
    datasetWantWorkLanguage = {}
    
    with open(f"data/{year}.csv", newline='\n') as input:
        
        reader = csv.reader(input, delimiter=',')
        
        # for row in reader:
        #     j = 0
        #     for column in row:
        #         print(j, column)
        #         j += 1
        #     break
        
        next(reader) # skip header
        
        for row in reader:
            HaveWorkedLanguage = row[88]
            if HaveWorkedLanguage != "NA":
                for lang in HaveWorkedLanguage.split("; "):
                    if lang not in datasetHaveWorkedLanguage:
                        datasetHaveWorkedLanguage[lang] = 0
                    datasetHaveWorkedLanguage[lang] += 1
            
            WantWorkLanguage = row[89]
            if WantWorkLanguage != "NA":
                for lang in WantWorkLanguage.split("; "):
                    if lang not in datasetWantWorkLanguage:
                        datasetWantWorkLanguage[lang] = 0
                    datasetWantWorkLanguage[lang] += 1
    
    with open(f"cleared/{year}.csv", "w") as output:
        json.dump(datasetHaveWorkedLanguage, output)
