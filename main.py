# Can only read Excel files if they have the same architecture as the example one!
from datetime import datetime
from tkinter import filedialog

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_excel(filedialog.askopenfilename(), skiprows=5, sheet_name='Stromzähler (1)')
data = data.iloc[:, 1:]
data = data.iloc[::-1]
i = 0
oldValue = 0
newValuesList = []
for index, value in data["Zählerstand (kWh)"].items():
    if i != 0:
        newValuesList.append((value - oldValue))
    else:
        newValuesList.append(0)
    oldValue = value
    i += 1

fig, axs = plt.subplots(2, 1)
print(data)

data["newValues"] = newValuesList
axs[0].plot(data["newValues"], data["Ablesezeitpunkt"])
axs[0].set_ylabel("Datum")
axs[0].set_xlabel("Wie viel ist seit der lezten Messung hinzugekommen")
axs[0].set_title("Zählerstände")
axs[0].grid(True)
for i in range(len(data["Ablesezeitpunkt"])):
    time = data["Ablesezeitpunkt"][i].split(" ")[0]
    if datetime.strptime(time, '%d.%m.%Y').date().weekday() in [5,6]:
        axs[0].scatter(data["newValues"][i], data["Ablesezeitpunkt"][i], color="red")
    else:
        axs[0].scatter(data["newValues"][i], data["Ablesezeitpunkt"][i], color="black")

    i += 1

axs[0].set_xticks(np.arange(0, max(newValuesList) + 2, 2))

axs[1].plot(data["Zählerstand (kWh)"], data["Ablesezeitpunkt"])
axs[1].set_ylabel("Datum")
axs[1].set_xlabel("kWh")
axs[1].set_title("Zählerstände")
axs[1].grid(True)
for i in range(len(data["Ablesezeitpunkt"])):
    time = data["Ablesezeitpunkt"][i].split(" ")[0]
    if datetime.strptime(time, '%d.%m.%Y').date().weekday() in [5,6]:
        axs[1].scatter(data["Zählerstand (kWh)"][i], data["Ablesezeitpunkt"][i], color="red")
    else:
        axs[1].scatter(data["Zählerstand (kWh)"][i], data["Ablesezeitpunkt"][i], color="black")
    i += 1
plt.tight_layout()
plt.show()
