# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/19960077/how-to-filter-pandas-dataframe-using-in-and-not-in-like-in-sql
from l3.Runtime import _l_
dfbc = dfbc[~dfbc['BUSINESS_ID'].isin(dfProfilesBusIds['BUSINESS_ID'])]
_l_(334)

