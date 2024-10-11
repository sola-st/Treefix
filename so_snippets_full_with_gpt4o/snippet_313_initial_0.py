import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

df = pd.DataFrame({'A': ['hello world', 'goodbye world', 'hello universe', 'goodbye universe']}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11350770/filter-pandas-dataframe-by-substring-criteria
from l3.Runtime import _l_
df.query('A.str.contains("hello").values')
_l_(15290)

