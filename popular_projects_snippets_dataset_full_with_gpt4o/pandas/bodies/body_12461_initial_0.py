import pandas as pd # pragma: no cover
from pandas import DataFrame # pragma: no cover

spam_data = '<table><tr><td>1</td></tr></table>' # pragma: no cover
self = type('Mock', (object,), {'read_html': lambda self, data: [pd.DataFrame({'col1': [1]})]})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
from l3.Runtime import _l_
dfs = self.read_html(spam_data)
_l_(17741)
for df in dfs:
    _l_(17743)

    assert isinstance(df, DataFrame)
    _l_(17742)
