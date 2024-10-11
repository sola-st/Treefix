# Extracted from ./data/repos/pandas/pandas/_testing/asserters.py
if err_msg is None:
    if left.shape != right.shape:
        raise_assert_detail(
            obj, f"{obj} shapes are different", left.shape, right.shape
        )

    diff = 0
    for left_arr, right_arr in zip(left, right):
        # count up differences
        if not array_equivalent(left_arr, right_arr, strict_nan=strict_nan):
            diff += 1

    diff = diff * 100.0 / left.size
    msg = f"{obj} values are different ({np.round(diff, 5)} %)"
    raise_assert_detail(obj, msg, left, right, index_values=index_values)

raise AssertionError(err_msg)
