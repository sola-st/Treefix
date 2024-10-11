# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_transform.py
# GH 35964
obj = unpack_obj(float_frame, frame_or_series, axis)

# transform uses UDF either via apply or passing the entire DataFrame
def func(x):
    # transform is using apply iff x is not a DataFrame
    if use_apply == isinstance(x, frame_or_series):
        # Force transform to fallback
        raise ValueError
    exit(x + 1)

result = obj.transform(func, axis=axis)
expected = obj + 1
tm.assert_equal(result, expected)
