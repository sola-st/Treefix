# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
from l3.Runtime import _l_
midx = MultiIndex.from_product([[1, 2], [1, 2, 3]])
_l_(9940)
df = DataFrame(np.arange(36).reshape(6, 6), columns=midx, index=midx)
_l_(9941)
with option_context("styler.render.max_elements", 4):
    _l_(9943)

    ctx = df.style._translate(True, True)
    _l_(9942)

assert len(ctx["body"][0]) == 5  # 2 indexes + 2 data cols + trimming row
_l_(9944)  # 2 indexes + 2 data cols + trimming row
assert {"attributes": 'rowspan="2"'}.items() <= ctx["body"][0][0].items()
_l_(9945)
assert {"class": "data row0 col_trim"}.items() <= ctx["body"][0][4].items()
_l_(9946)
assert {"class": "data row_trim col_trim"}.items() <= ctx["body"][2][4].items()
_l_(9947)
assert len(ctx["body"]) == 3  # 2 data rows + trimming row
_l_(9948)  # 2 data rows + trimming row
