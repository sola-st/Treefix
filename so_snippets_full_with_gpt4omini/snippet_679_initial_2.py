import matplotlib.pyplot as plt # pragma: no cover
import seaborn as sns # pragma: no cover
import pandas as pd # pragma: no cover

housing = pd.DataFrame({'ocean_proximity': ['NEAR BAY', 'INLAND', 'NEAR OCEAN', 'NEAR BAY', 'INLAND'], 'median_house_value': [300000, 200000, 400000, 320000, 150000]}) # pragma: no cover

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

