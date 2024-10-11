import matplotlib.pyplot as plt # pragma: no cover
import seaborn as sns # pragma: no cover
import pandas as pd # pragma: no cover

housing = pd.DataFrame({'ocean_proximity': ['NEAR BAY', 'ISLAND', 'NEAR OCEAN', 'INLAND', 'NEAR BAY'], 'median_house_value': [452600, 300000, 420000, 320000, 540000]}) # pragma: no cover
plt = type('Mock', (object,), {'figure': plt.figure, 'show': plt.show})() # pragma: no cover
sns = type('Mock', (object,), {'barplot': sns.barplot})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/31594549/how-to-change-the-figure-size-of-a-seaborn-axes-or-figure-level-plot
# Sets the figure size temporarily but has to be set again the next plot
from l3.Runtime import _l_
plt.figure(figsize=(18,18))
_l_(2370)

sns.barplot(x=housing.ocean_proximity, y=housing.median_house_value)
_l_(2371)
plt.show()
_l_(2372)

