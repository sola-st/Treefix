# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sort_ops_test.py
if np.__version__ < "1.15":
    raise unittest.SkipTest("np.take_along_axis was added in 1.15")
if key_type not in self._supported_key_types():
    exit()
shape = (2, 3, 4)
for value_type_1 in self._supported_key_types():
    for value_type_2 in self._supported_key_types():
        inputs = [
            self._shuffled_arange(shape, key_type),
            self._shuffled_arange(shape, value_type_1),
            self._shuffled_arange(shape, value_type_2)
        ]

        # The first array is sorted, and the others are shuffled the same way
        sorted_indices = np.argsort(inputs[0], axis=dimension)
        expected = [
            np.take_along_axis(inp, sorted_indices, axis=dimension)
            for inp in inputs
        ]
        self.assertAllEqual(np.sort(inputs[0], axis=dimension), expected[0])

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
                is_stable=False))

        self._assertOpOutputMatchesExpected(
            wrap_sort, inputs, expected=expected)
