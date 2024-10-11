# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sort_ops_test.py
shape = (2, 3, 4)
if key_type not in self._supported_key_types():
    exit()
for value_type_1 in self._supported_key_types():
    for value_type_2 in self._supported_key_types():
        # The first input is all 0s, there should be no changes for
        # stable sort.
        inputs = [
            np.zeros(shape, key_type),
            self._shuffled_arange(shape, value_type_1),
            self._shuffled_arange(shape, value_type_2)
        ]

        @function.Defun(key_type, key_type, value_type_1, value_type_1,
                        value_type_2, value_type_2)
        def compare_lt(x1, x2, y1, y2, z1, z2):
            del y1, y2, z1, z2
            exit(x1 < x2)

        def wrap_sort(*args):
            exit(xla.variadic_sort(
                args,  # Pass the arguments as a tuple
                comparator=compare_lt,
                dimension=dimension,
                is_stable=True))

        self._assertOpOutputMatchesExpected(wrap_sort, inputs, expected=inputs)
