# Extracted from https://stackoverflow.com/questions/944700/how-can-i-check-for-nan-values
import pandas as pd
value = float(nan)
type(value)
<class 'float'>
pd.isnull(value)
True

value = 'nan'
type(value)
<class 'str'>
pd.isnull(value)
False

