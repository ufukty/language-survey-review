import csv
import json
import os

os.makedirs("clean", 0o711, True)

columnIndexes = {
    "have": {
        "2017": 88,
        "2018": 65,
        "2019": 43,
        "2020": 22,
        "2021": 16,
        "2022": 19,
    },
    "want": {
        "2017": 89,
        "2018": 66,
        "2019": 44,
        "2020": 21,
        "2021": 17,
        "2022": 20,
    },
}

separators = {
    "2017": "; ",
    "2018": ";",
    "2019": ";",
    "2020": ";",
    "2021": ";",
    "2022": ";",
}


def clearNewFormatInputFile(year: int):
    dataset = {
        "have": {},
        "want": {}
    }
    
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
            HaveWorkedLanguage = row[columnIndexes["have"][year.__str__()]]
            if HaveWorkedLanguage != "NA":
                for lang in HaveWorkedLanguage.split(separators[year.__str__()]):
                    if lang not in dataset["have"]:
                        dataset["have"][lang] = 0
                    dataset["have"][lang] += 1
            
            WantWorkLanguage = row[columnIndexes["want"][year.__str__()]]
            if WantWorkLanguage != "NA":
                for lang in WantWorkLanguage.split(separators[year.__str__()]):
                    if lang not in dataset["want"]:
                        dataset["want"][lang] = 0
                    dataset["want"][lang] += 1
    
    with open(f"clean/{year}.json", "w") as output:
        json.dump(dataset, output)


for year in range(2017, 2023):
    clearNewFormatInputFile(year)