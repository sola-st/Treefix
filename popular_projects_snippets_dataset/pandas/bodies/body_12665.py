# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH21073
expected = (
    '{"columns":["col1"],"index":[0,1],'
    '"data":[[13342205958987758245],[12388075603347835679]]}'
)
df = DataFrame(data={"col1": [13342205958987758245, 12388075603347835679]})
result = df.to_json(orient="split")
assert result == expected
