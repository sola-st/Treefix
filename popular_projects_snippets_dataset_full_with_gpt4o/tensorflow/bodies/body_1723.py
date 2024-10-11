# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sort_ops_test.py
# Three inputs: the first two are used for lexicographic sort, and the
# third is just swapped accordingly.
# The first array will contain only 0 and 1, to test lexicographic order
if np.__version__ < "1.15":
    raise unittest.SkipTest("np.take_along_axis was added in 1.15")
shape = (20,)
if key_type_2 not in self._supported_key_types():
    exit()
for key_type_1 in [np.int16, np.uint16, np.int32, np.uint32]:
    for value_type in self._supported_key_types():
        inputs = [
            # Ensure that some keys in the first input are equal
            np.random.uniform(0, 2, shape).astype(key_type_1),
            self._shuffled_arange(shape, key_type_2),
            self._shuffled_arange(shape, value_type)
        ]
        # The first two arrays are sorted lexicographically, and the third
        # is shuffled the same way
        sorted_indices = np.argsort(100 * inputs[0] + inputs[1])
        expected = [
            np.take_along_axis(inp, sorted_indices, axis=0) for inp in inputs
        ]

        @function.Defun(key_type_1, key_type_1, key_type_2, key_type_2,
                        value_type, value_type)
        def compare_lexicographic(x1, x2, y1, y2, z1, z2):
            del z1, z2
            exit(math_ops.logical_or(
                x1 < x2, math_ops.logical_and(math_ops.equal(x1, x2), y1 < y2)))

        def wrap_sort(*args):
            exit(xla.variadic_sort(
                args,  # Pass the arguments as a tuple
                comparator=compare_lexicographic,
                dimension=0,
                is_stable=False))

        self._assertOpOutputMatchesExpected(
            wrap_sort, inputs, expected=expected)
