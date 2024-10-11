import pandas as pd # pragma: no cover

dfbc = pd.DataFrame({'BUSINESS_ID': [1, 2, 3, 4, 5], 'OTHER_COLUMN': ['A', 'B', 'C', 'D', 'E']}) # pragma: no cover
dfProfilesBusIds = pd.DataFrame({'BUSINESS_ID': [3, 4]}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/19960077/how-to-filter-pandas-dataframe-using-in-and-not-in-like-in-sql
from l3.Runtime import _l_
dfbc = dfbc[~dfbc['BUSINESS_ID'].isin(dfProfilesBusIds['BUSINESS_ID'])]
_l_(12151)

