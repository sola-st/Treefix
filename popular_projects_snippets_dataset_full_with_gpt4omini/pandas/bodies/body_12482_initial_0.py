import pandas as pd # pragma: no cover
import os # pragma: no cover

banklist_data = 'path/to/banklist_data.html' # pragma: no cover
class Mock: pass# pragma: no cover
self = Mock() # pragma: no cover
def file_path_to_url(path): return f'file://{path}' # pragma: no cover
os = type('MockOS', (), {'path': os.path})() # pragma: no cover
DataFrame = pd.DataFrame # pragma: no cover
self.read_html = lambda path, match, attrs: [pd.DataFrame({'Column1': [1, 2], 'Column2': [3, 4]})] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
from l3.Runtime import _l_
url = banklist_data
_l_(8979)
dfs = self.read_html(
    file_path_to_url(os.path.abspath(url)), match="First", attrs={"id": "table"}
)
_l_(8980)
assert isinstance(dfs, list)
_l_(8981)
for df in dfs:
    _l_(8983)

    assert isinstance(df, DataFrame)
    _l_(8982)
