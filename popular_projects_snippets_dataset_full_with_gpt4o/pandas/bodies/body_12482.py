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
