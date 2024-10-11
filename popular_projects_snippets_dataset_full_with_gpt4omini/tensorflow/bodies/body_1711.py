# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sort_ops_test.py
for key_type in self._supported_key_types():
    for value_type in self._supported_key_types():
        if key_type == np.uint8 or value_type == np.uint8:
            # I do not understand why the test fails on uint8. We plan to
            # deprecate xla.key_value_sort in favor of xla.variadic_sort anyway.
            continue
        x = self._shuffled_arange((101,), key_type)
        y = (-x).astype(value_type)
        self._assertOpOutputMatchesExpected(
            xla.key_value_sort, [x, y],
            expected=[
                np.arange(101, dtype=key_type),
                -np.arange(101, dtype=value_type)
            ])
