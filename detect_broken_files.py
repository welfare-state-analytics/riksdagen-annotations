import pandas as pd
from lxml import etree
from pathlib import Path
import subprocess
import traceback

raw = Path("raw/")
parser = etree.XMLParser(remove_blank_text=True)
problematic_paths = []
for p in raw.glob("*.xml"):

    try:
        root = etree.parse(p.open(), parser=parser)
        #print(root)
    except Exception:
        relative_path = p.relative_to(".")
        print(relative_path)
        problematic_paths.append(p.relative_to("."))
        traceback.print_exc()
        print()

subprocess.run(["subl"] + problematic_paths)
print("Broken files in total:", len(problematic_paths))