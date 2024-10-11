import pandas as pd # pragma: no cover

raw_data = pd.DataFrame({'Mycol': ['2021-01-01', '2021-02-01', '2021-03-01']}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/26763344/convert-pandas-column-to-datetime
from l3.Runtime import _l_
try:
    import pandas as pd
    _l_(1953)

except ImportError:
    pass
raw_data['Mycol'] =  pd.to_datetime(raw_data['Mycol'], infer_datetime_format=True)
_l_(1954)

