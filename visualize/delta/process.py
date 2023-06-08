import json

input = {}
output = {
    "have": {},
    "want": {},
}

with open(f"visualize/normalized/data.json") as inputFile:
    input = json.load(inputFile)

langs = input["have"].keys()
for lang in langs:
    current = input["have"][lang][1:]
    past = input["have"][lang][:-1]
    output["have"][lang] = [c - p for p, c in zip(past, current)]
    
    current = input["want"][lang][1:]
    past = input["want"][lang][:-1]
    output["want"][lang] = [c - p for p, c in zip(past, current)]

with open(f"visualize/delta/data.json", "w") as outputFile:
    json.dump(output, outputFile)
