import os
import json
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
import matplotlib.ticker as mtick

dataset = {}

with open(f"visualize/normalized/data.json") as input:
    dataset = json.load(input)

fig, ax = plt.subplots(1, 1, figsize=(8, 6), layout='constrained')

colors = {
    "C#": "#178600",
    "C++": "#9457EB",
    "Go": "#00ADD8",
    "Java": "#FF9800",
    "JavaScript": "#F7DF1E",
    "Kotlin": "#A97BFF",
    "Lua": "#000080",
    "Matlab": "#FFD700",
    "MATLAB": "#FFD700",
    "PHP": "#F692D2",
    "Python": "#3776AB",
    "R": "#1A8CFF",
    "Ruby": "#CC342D",
    "Rust": "#DEA584",
    "Swift": "#5AC8FA",
    "TypeScript": "#007ACC",
    "APL": "#5A8F29",
    "Assembly": "#B7D0E8",
    "Shell": "#4EAA25",
    "C": "#0085CA",
    "Cobol": "#FFD700",
    "COBOL": "#FFD700",
    "CSS": "#2965F1",
    "Clojure": "#5881D8",
    "CoffeeScript": "#244776",
    "Common Lisp": "#3FB68B",
    "Crystal": "#000100",
    "Dart": "#00B4AB",
    "Delphi": "#EE1F35",
    "Delphi/Object Pascal": "#EE1F35",
    "Elixir": "#6E4A7E",
    "Erlang": "#A90533",
    "F#": "#378BBA",
    "Fortran": "#726E97",
    "Groovy": "#4298B8",
    "Hack": "#375EAB",
    "Haskell": "#5E5086",
    "HTML": "#E34C26",
    "HTML/CSS": "#438EFF",
    "Julia": "#9558B2",
    "LISP": "#5C2E85",
    "Node.js": "#43853D",
    "Ocaml": "#EC6813",
    "Objective-C": "#438EFF",
    "Perl": "#39457E",
    "R": "#1A8CFF",
    "SAS": "#B34936",
    "SQL": "#FF9800",
    "Scala": "#DC322F",
    "Smalltalk": "#596706",
    "Solidity": "#AA6746",
    "VB.NET": "#1B6AC6",
    "VBA": "#867DB1",
    "Visual Basic 6": "#1B6AC6",
    "WebAssembly": "#654FF0",
    "PowerShell": "#012456",
}
label_offsets_vertical = {k: 0.5 for k in dataset["have"]}
# label_offsets_vertical["SQL"] += 0.5
# label_offsets_vertical["Python"] += -3.5
# label_offsets_vertical["Java"] += -3.5
# label_offsets_vertical["PHP"] += -2.5
# label_offsets_vertical["C"] += -6.5
# label_offsets_vertical["Go"] += 14
# label_offsets_vertical["Rust"] += 12
# label_offsets_vertical["Ruby"] += 14

# label_offsets_vertical["Assembly"] += 7
# label_offsets_vertical["Swift"] += 2
# label_offsets_vertical["R"] += -6
# label_offsets_vertical["VBA"] += -15
# label_offsets_vertical["Scala"] += -14
# label_offsets_vertical["Objective-C"] += -20

for lang, series in dataset["have"].items():
    line, = ax.plot(range(2017, 2023), series, lw=2.5, color=colors[lang])
    y_pos = series[-1]
    offset = label_offsets_vertical[lang] / 72
    trans = mtransforms.ScaledTranslation(0, offset, fig.dpi_scale_trans)
    trans = ax.transData + trans
    
    ax.text(
        2022.1,
        y_pos,
        lang,
        color=colors[lang],
        transform=trans,
    )

ax.spines[:].set_visible(False)
ax.xaxis.tick_bottom()
ax.yaxis.tick_left()
ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda y, _: f'{int(10000*y)/100}%'))
ax.grid(True, 'major', 'both', ls='--', lw=.5, c='k', alpha=.3)
ax.tick_params(
    axis='both',
    which='both',
    labelsize='large',
    bottom=False,
    top=False,
    labelbottom=True,
    left=False,
    right=False,
    labelleft=True
)
fig.suptitle("Languages I worked last year / year total", ha="center")
plt.ylabel('Pick')
plt.xlabel('Years')
plt.savefig(
    fname="visualize/normalized/output.png",
    dpi=300,
    format=None,
    metadata=None,
    bbox_inches=None,
    pad_inches=0.1,
    facecolor='auto',
    edgecolor='auto',
    backend=None,
)
# plt.show()