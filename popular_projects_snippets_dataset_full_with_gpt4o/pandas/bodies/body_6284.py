# Extracted from ./data/repos/pandas/pandas/tests/extension/base/reduce.py
op_name = all_numeric_reductions
s = pd.Series(data)

msg = (
    "[Cc]annot perform|Categorical is not ordered for operation|"
    "does not support reduction|"
)

with pytest.raises(TypeError, match=msg):
    getattr(s, op_name)(skipna=skipna)
