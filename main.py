import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("./datasamples/traffic.csv")

month = df["month"]
searches = df["searches"]
direct = df["direct"]
social_media = df["social_media"]

blue = "#3498DB"
pink = "#DD7195"
amber = "#FFAF00"

bar_width = 0.3
x = np.arange(len(month))

plt.figure(figsize=(8, 6))

plt.bar(x - bar_width, searches, width=bar_width, label="Searches", color=blue)
plt.bar(x, direct, width=bar_width, label="Direct", color=pink)
plt.bar(x + bar_width, social_media, width=bar_width, label="Social Media", color=amber)

plt.ylim(0, 100)
plt.xlabel("Months")
plt.ylabel("Visitors (in thousands)")
plt.title("Visitors by Web Traffic Sources")
plt.xticks(x, month)
plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=3)
plt.show()
