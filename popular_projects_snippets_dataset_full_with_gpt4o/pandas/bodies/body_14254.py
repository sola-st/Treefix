# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
# GH 16493
df = DataFrame({"A": [1, 2]}, index=Index(["a", "b"], name="myindexname"))
result = df.to_html(index_names=False)
assert "myindexname" not in result
