import pandas as pd # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.read_html = lambda x: [pd.DataFrame({'A': [1, 2], 'B': [3, 4]})] # pragma: no cover
spam_data = 'dummy_data.html' # pragma: no cover
DataFrame = pd.DataFrame # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
from l3.Runtime import _l_
dfs = self.read_html(spam_data)
_l_(5721)
for df in dfs:
    _l_(5723)

    assert isinstance(df, DataFrame)
    _l_(5722)
