import pandas as pd
from lxml import etree
from pathlib import Path
import numpy as np
import re

raw = Path("raw/")
parser = etree.XMLParser(remove_blank_text=True)
rows = []
columns = ["text", "tag", "protocol", "page"]
for p in raw.glob("*.xml"):
    # Map back to corpus
    prot, page, _ = re.split(r'(?:p)(\d+)', str(p))
    prot = prot.split('/')[-1] + '.xml'
    prot = prot.split('_')[-1]
    prot = prot.replace('ô', 'ö')

    root = etree.parse(p.open(), parser=parser).getroot()
    for elem in root:
        text = " ".join(elem.text.split())
        row = [text, elem.tag, prot, page]
        rows.append(row)

df = pd.DataFrame(rows, columns=columns)
np.random.seed(123)
df["split"] = np.random.choice(["train", "val", "test"], size=len(df), p=[0.6, 0.2, 0.2])

df.to_csv("data/dataset_mapped.csv", index=False)