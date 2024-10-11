import pandas as pd # pragma: no cover

housing = pd.DataFrame({# pragma: no cover
    'ocean_proximity': ['<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'NEAR OCEAN', 'INLAND', '<1H OCEAN'],# pragma: no cover
    'median_house_value': [100000, 150000, 200000, 250000, 175000, 300000]# pragma: no cover
}) # pragma: no cover

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

