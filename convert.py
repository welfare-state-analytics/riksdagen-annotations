import pandas as pd
from lxml import etree
from pathlib import Path
import numpy as np

raw = Path("raw/")
parser = etree.XMLParser(remove_blank_text=True)
rows = []
columns = ["text", "tag"]
for p in raw.glob("*.xml"):
    root = etree.parse(p.open(), parser=parser).getroot()
    for elem in root:
        text = " ".join(elem.text.split())
        row = [text, elem.tag]
        rows.append(row)

df = pd.DataFrame(rows, columns=columns)
np.random.seed(123)
df["split"] = np.random.choice(["train", "val", "test"], size=len(df), p=[0.6, 0.2, 0.2])
print(df)

df.to_csv("data/dataset.csv", index=False)