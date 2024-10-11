# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1252163/printing-python-version-in-output
from l3.Runtime import _l_
try:
    import os
    _l_(1124)

except ImportError:
    pass

if __name__ == "__main__":
    _l_(1126)

    os.system('python -V') # can also use python --version
    _l_(1125) # can also use python --version

