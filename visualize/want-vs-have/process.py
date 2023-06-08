import json

input = {}
output = {}

with open(f"product/clean-2/raw.json") as inputFile:
    input = json.load(inputFile)

langs = input["want"].keys()
for lang in langs:
    want = input["want"][lang][:-1]
    have = input["have"][lang][1:]
    output[lang] = [float(h) / w for w, h in zip(want, have)]

with open(f"visualize/want-vs-have/data.json", "w") as outputFile:
    json.dump(output, outputFile)
