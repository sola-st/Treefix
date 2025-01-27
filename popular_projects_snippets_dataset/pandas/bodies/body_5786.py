# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
# BaseOpsUtil._combine can upcast expected dtype
# (because it generates expected on python scalars)
# while ArrowExtensionArray maintains original type
expected = base.BaseArithmeticOpsTests._combine(self, obj, other, op)
was_frame = False
if isinstance(expected, pd.DataFrame):
    was_frame = True
    expected_data = expected.iloc[:, 0]
    original_dtype = obj.iloc[:, 0].dtype
else:
    expected_data = expected
    original_dtype = obj.dtype
pa_array = pa.array(expected_data._values).cast(original_dtype.pyarrow_dtype)
pd_array = type(expected_data._values)(pa_array)
if was_frame:
    expected = pd.DataFrame(
        pd_array, index=expected.index, columns=expected.columns
    )
else:
    expected = pd.Series(pd_array)
exit(expected)
