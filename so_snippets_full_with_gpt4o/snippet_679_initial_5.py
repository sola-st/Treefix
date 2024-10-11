import pandas as pd # pragma: no cover

housing = pd.DataFrame({ 'ocean_proximity': ['NEAR BAY', 'INLAND', 'NEAR OCEAN', 'ISLAND', 'NEAR BAY', 'INLAND'], 'median_house_value': [452600, 358500, 352100, 341300, 342200, 231200] }) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/31594549/how-to-change-the-figure-size-of-a-seaborn-axes-or-figure-level-plot
# Sets the figure size temporarily but has to be set again the next plot
from l3.Runtime import _l_
plt.figure(figsize=(18,18))
_l_(13934)

sns.barplot(x=housing.ocean_proximity, y=housing.median_house_value)
_l_(13935)
plt.show()
_l_(13936)

