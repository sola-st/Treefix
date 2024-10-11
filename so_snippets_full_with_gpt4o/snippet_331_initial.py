# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3451111/unzipping-files-in-python
from l3.Runtime import _l_
try:
    import zipfile
    _l_(12293)

except ImportError:
    pass
with zipfile.ZipFile("file.zip","r") as zip_ref:
    _l_(12295)

    zip_ref.extractall("targetdir")
    _l_(12294)

