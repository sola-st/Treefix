import pandas as pd # pragma: no cover

raw_data = pd.DataFrame({'Mycol': ['2023-10-01 14:30:00', '2023-10-02 15:45:00', '2023-10-03 16:00:00']}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/26763344/convert-pandas-column-to-datetime
from l3.Runtime import _l_
try:
    import pandas as pd
    _l_(14168)

except ImportError:
    pass
raw_data['Mycol'] =  pd.to_datetime(raw_data['Mycol'], infer_datetime_format=True)
_l_(14169)

