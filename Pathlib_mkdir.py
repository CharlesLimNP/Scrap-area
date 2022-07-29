# from importlib.resources import path
# from pathlib import Path

# fp = Path.cwd()/"pfb_ind_assign2"
# print(fp)
# fp.mkdir(parents=False, exist_ok=True)

import glob

# for name in glob.glob('*.txt'):
#     print(name)

txt = "    I like    banana.    "
x = txt.replace("banana", "orange")
x = x.strip()
print(x)