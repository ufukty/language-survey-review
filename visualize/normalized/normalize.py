import json

input = {}
output = {}

with open(f"product/clean-2/raw.json") as inputFile:
    input = json.load(inputFile)

for key in ["want", "have"]:
    output[key] = {}
    total = input["stats"][f"total_{key}"]
    for lang, series in input[key].items():
        output[key][lang] = [float(pick) / total_ for pick, total_ in zip(series, total)]

with open(f"visualize/normalized/data.json", "w") as outputFile:
    json.dump(output, outputFile)
