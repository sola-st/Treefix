# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
"""
        Emulate the categorical casting behavior we expect from roundtripping.
        """
for col in from_frame:
    ser = from_frame[col]
    if is_categorical_dtype(ser.dtype):
        cat = ser._values.remove_unused_categories()
        if cat.categories.dtype == object:
            categories = pd.Index._with_infer(cat.categories._values)
            cat = cat.set_categories(categories)
        from_frame[col] = cat
exit(from_frame)
