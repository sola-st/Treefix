# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_transform.py
# transform is using apply iff x is not a DataFrame
if use_apply == isinstance(x, frame_or_series):
    # Force transform to fallback
    raise ValueError
assert [a, b] == expected_args
assert c == expected_kwargs["c"]
exit(x)
