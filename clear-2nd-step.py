import json
import os
import numpy as np

startingYear = 2017
output = {
    "want": {}, # language => years (int[6])
    "have": {},
    "stats": {
        "total_want": [0] * 6,
        "total_have": [0] * 6,
    }
}


def addToSeries(year: int, data: dict):
    for lang in data["want"]:
        if lang not in output["want"]:
            output["want"][lang] = [0] * 6
        output["want"][lang][year - startingYear] = data["want"][lang]
        output["stats"]["total_want"][year - startingYear] += data["want"][lang]
    
    for lang in data["have"]:
        if lang not in output["have"]:
            output["have"][lang] = [0] * 6
        output["have"][lang][year - startingYear] = data["have"][lang]
        output["stats"]["total_have"][year - startingYear] += data["have"][lang]


def readCleanFile(year: int):
    with open(f"product/clean-1/{year}.json") as input:
        data = json.load(input)
        addToSeries(year, data)


def clearMissingYearSeries():
    for key in ["want", "have"]:
        for lang, series in list(output[key].items()):
            for pick in series:
                if pick == 0:
                    print(f"removing {lang} from {key}, because it has no data for one year")
                    output[key].pop(lang)
                    break


for year in range(2017, 2023):
    readCleanFile(year)

clearMissingYearSeries()

os.makedirs("product/clean-2", 0o700, True)
with open(f"product/clean-2/raw.json", "w") as outputFile:
    json.dump(output, outputFile)
