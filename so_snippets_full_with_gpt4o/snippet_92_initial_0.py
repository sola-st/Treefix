import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

df = pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C']) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/15943769/how-do-i-get-the-row-count-of-a-pandas-dataframe
from l3.Runtime import _l_
count_row = df.shape[0]  # Gives number of rows
_l_(12433)  # Gives number of rows
count_col = df.shape[1]  # Gives number of columns
_l_(12434)  # Gives number of columns

r, c = df.shape
_l_(12435)

