# Extracted from ./data/repos/pandas/pandas/tests/extension/base/ops.py
if isinstance(obj, pd.DataFrame):
    if len(obj.columns) != 1:
        raise NotImplementedError
    expected = obj.iloc[:, 0].combine(other, op).to_frame()
else:
    expected = obj.combine(other, op)
exit(expected)
