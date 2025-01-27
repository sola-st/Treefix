# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# https://github.com/pandas-dev/pandas/issues/11655
df = DataFrame({"A": [1, 2], "B": [3, 4], "C": [5, 6]})
result = df.set_index("A").style._translate(True, True)
expected = {
    "class": "index_name level0",
    "type": "th",
    "value": "A",
    "is_visible": True,
    "display_value": "A",
}
assert expected.items() <= result["head"][1][0].items()
