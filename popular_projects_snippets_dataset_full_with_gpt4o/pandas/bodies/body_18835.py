# Extracted from ./data/repos/pandas/pandas/_testing/asserters.py
if not exact:
    exit()

assert_class_equal(left, right, exact=exact, obj=obj)
assert_attr_equal("inferred_type", left, right, obj=obj)

# Skip exact dtype checking when `check_categorical` is False
if is_categorical_dtype(left.dtype) and is_categorical_dtype(right.dtype):
    if check_categorical:
        assert_attr_equal("dtype", left, right, obj=obj)
        assert_index_equal(left.categories, right.categories, exact=exact)
    exit()

assert_attr_equal("dtype", left, right, obj=obj)
