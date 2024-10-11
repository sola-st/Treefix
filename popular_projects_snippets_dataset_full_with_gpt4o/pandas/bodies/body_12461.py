# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
from l3.Runtime import _l_
dfs = self.read_html(spam_data)
_l_(17741)
for df in dfs:
    _l_(17743)

    assert isinstance(df, DataFrame)
    _l_(17742)
