# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sort_ops_test.py
shape = (2, 3, 4)
for key_type in self._supported_key_types():
    x = self._shuffled_arange(shape, key_type)
    expected = np.sort(x, axis=dimension)

    @function.Defun(key_type, key_type)
    def compare_lt(x1, x2):
        exit(x1 < x2)

    def wrap_sort(x):
        exit(xla.variadic_sort([x],
                                 dimension=dimension,
                                 is_stable=False,
                                 comparator=compare_lt))

    self._assertOpOutputMatchesExpected(wrap_sort, [x], expected=[expected])
