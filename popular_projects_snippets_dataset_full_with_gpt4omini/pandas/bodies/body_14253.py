# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
df = DataFrame({"A": [1, 2, 3]})
result = df.to_html(notebook=notebook)

if notebook:
    assert "tbody tr th:only-of-type" in result
    assert "vertical-align: middle;" in result
    assert "thead th" in result
else:
    assert "tbody tr th:only-of-type" not in result
    assert "vertical-align: middle;" not in result
    assert "thead th" not in result
