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

bars1 = plt.bar(x - bar_width, searches, width=bar_width, label="Searches", color=blue)
bars2 = plt.bar(x, direct, width=bar_width, label="Direct", color=pink)
bars3 = plt.bar(x + bar_width, social_media, width=bar_width, label="Social Media", color=amber)


def add_labels(bars):
    for bar in bars:
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 2,
            f"{int(bar.get_height())}",
            ha="center",
            fontsize=10,
        )


add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

plt.ylim(0, 100)
plt.xlabel("Months")
plt.ylabel("Visitors (in thousands)")
plt.title("Visitors by Web Traffic Sources")
plt.xticks(x, month)
plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=3, handleheight=2.4, handlelength=2.8)
plt.show()
