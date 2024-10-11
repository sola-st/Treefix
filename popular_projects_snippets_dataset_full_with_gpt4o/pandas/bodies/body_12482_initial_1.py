import os # pragma: no cover
import pandas as pd # pragma: no cover
from pandas import DataFrame # pragma: no cover

banklist_data = 'testdata/banklist.html' # pragma: no cover
self = type('Mock', (object,), {'read_html': lambda self, url, match, attrs: [pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})]})() # pragma: no cover
file_path_to_url = lambda path: 'file://' + path # pragma: no cover
os = type('Mock', (object,), {'path': type('PathMock', (object,), {'abspath': lambda path: path})()})() # pragma: no cover
DataFrame = pd.DataFrame # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
from l3.Runtime import _l_
url = banklist_data
_l_(19153)
dfs = self.read_html(
    file_path_to_url(os.path.abspath(url)), match="First", attrs={"id": "table"}
)
_l_(19154)
assert isinstance(dfs, list)
_l_(19155)
for df in dfs:
    _l_(19157)

    assert isinstance(df, DataFrame)
    _l_(19156)
