# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/20199126/reading-json-from-a-file
from l3.Runtime import _l_
try:
    import pandas as pd
    _l_(15444)

except ImportError:
    pass
df = pd.read_json('strings.json', lines=True)
_l_(15445)
print(df)
_l_(15446)

