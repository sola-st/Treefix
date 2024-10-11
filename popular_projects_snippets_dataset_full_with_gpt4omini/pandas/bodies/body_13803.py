# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# See https://github.com/pandas-dev/pandas/issues/16780
df = DataFrame({"a": [1, 3, 5, 6], "b": [2, 4, 12, 21]})
result = df.style.to_html(uuid="test")
assert "test" in result
ids = re.findall('id="(.*?)"', result)
assert np.unique(ids).size == len(ids)
