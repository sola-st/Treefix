# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
# GH 25941
df = DataFrame(np.random.random(size=(1, 3)))
result = df.to_html(col_space=unit)
result = result.split("tbody")[0]
hdrs = [x for x in result.split("\n") if re.search(r"<th[>\s]", x)]
if isinstance(unit, int):
    unit = str(unit) + "px"
for h in hdrs:
    expected = f'<th style="min-width: {unit};">'
    assert expected in h
