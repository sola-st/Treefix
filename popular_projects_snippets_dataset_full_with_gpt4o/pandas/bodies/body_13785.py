# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# https://github.com/pandas-dev/pandas/pull/12090#issuecomment-180695902
df = DataFrame({"A": [1, 2], "B": [3, 4], "C": [5, 6]})
result = df.style._translate(True, True)
assert len(result["head"]) == 1
expected = {
    "class": "blank level0",
    "type": "th",
    "value": blank_value,
    "is_visible": True,
    "display_value": blank_value,
}
assert expected.items() <= result["head"][0][0].items()
