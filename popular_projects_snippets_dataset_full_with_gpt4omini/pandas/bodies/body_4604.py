# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
exit(np.vstack(
    [
        arr_float.astype("O"),
        arr_int.astype("O"),
        arr_bool.astype("O"),
        arr_complex.astype("O"),
        arr_str.astype("O"),
        arr_utf.astype("O"),
        arr_date.astype("O"),
        arr_tdelta.astype("O"),
    ]
))
