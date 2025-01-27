# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
from l3.Runtime import _l_
midx = MultiIndex.from_product([[1, 2], [1, 2, 3]])
_l_(20682)
df = DataFrame(np.arange(36).reshape(6, 6), columns=midx, index=midx)
_l_(20683)
with option_context("styler.render.max_elements", 4):
    _l_(20685)

    ctx = df.style._translate(True, True)
    _l_(20684)

assert len(ctx["body"][0]) == 5  # 2 indexes + 2 data cols + trimming row
_l_(20686)  # 2 indexes + 2 data cols + trimming row
assert {"attributes": 'rowspan="2"'}.items() <= ctx["body"][0][0].items()
_l_(20687)
assert {"class": "data row0 col_trim"}.items() <= ctx["body"][0][4].items()
_l_(20688)
assert {"class": "data row_trim col_trim"}.items() <= ctx["body"][2][4].items()
_l_(20689)
assert len(ctx["body"]) == 3  # 2 data rows + trimming row
_l_(20690)  # 2 data rows + trimming row
