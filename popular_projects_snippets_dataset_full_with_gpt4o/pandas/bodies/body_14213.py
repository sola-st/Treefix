# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
df = DataFrame(np.random.random(size=(1, 3)))
# check that col_space affects HTML generation
# and be very brittle about it.
result = df.to_html(col_space=col_space)
hdrs = [x for x in result.split(r"\n") if re.search(r"<th[>\s]", x)]
assert len(hdrs) > 0
for h in hdrs:
    assert "min-width" in h
    assert str(col_space) in h
