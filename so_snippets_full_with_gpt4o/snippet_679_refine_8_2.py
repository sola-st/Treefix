import pandas as pd # pragma: no cover

housing = pd.DataFrame({# pragma: no cover
    'ocean_proximity': ['NEAR BAY', 'INLAND', 'INLAND', 'NEAR BAY', 'ISLAND'],# pragma: no cover
    'median_house_value': [452600, 358500, 352100, 342200, 275000]# pragma: no cover
}) # pragma: no cover

import matplotlib.pyplot as plt # pragma: no cover
import pandas as pd # pragma: no cover

class MockPlt:# pragma: no cover
    @staticmethod# pragma: no cover
    def figure(*args, **kwargs):# pragma: no cover
        pass# pragma: no cover
    @staticmethod# pragma: no cover
    def show(*args, **kwargs):# pragma: no cover
        pass# pragma: no cover
plt = MockPlt # pragma: no cover
class MockSns:# pragma: no cover
    @staticmethod# pragma: no cover
    def barplot(*args, **kwargs):# pragma: no cover
        pass# pragma: no cover
sns = MockSns # pragma: no cover
housing = pd.DataFrame({'ocean_proximity': ['NEAR BAY', 'INLAND', 'NEAR OCEAN', 'ISLAND', 'NEAR BAY'], 'median_house_value': [100000, 150000, 200000, 250000, 175000]}) # pragma: no cover

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

