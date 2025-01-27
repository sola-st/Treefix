# Extracted from https://stackoverflow.com/questions/4152963/get-name-of-current-script-in-python
from pathlib import Path
Path(__file__).stem

from pathlib import Path

print(Path(__file__).stem)
print(__file__)

python3.6 test.py
test
test.py

