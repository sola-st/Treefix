import pandas as pd # pragma: no cover
import json # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/20199126/reading-json-from-a-file
from l3.Runtime import _l_
try:
    import pandas as pd
    _l_(64)

except ImportError:
    pass
df = pd.read_json('strings.json', lines=True)
_l_(65)
print(df)
_l_(66)

