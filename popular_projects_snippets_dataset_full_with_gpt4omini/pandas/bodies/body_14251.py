# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
# GH 15019
data = [
    [1.764052, 0.400157],
    [0.978738, 2.240893],
    [1.867558, -0.977278],
    [0.950088, -0.151357],
    [-0.103219, 0.410599],
]
df = DataFrame(data)
result = df.to_html(max_rows=4, index=index)
expected = expected_html(datapath, "gh15019_expected_output")
assert result == expected
