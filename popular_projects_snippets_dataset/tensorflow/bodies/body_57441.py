# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_test.py
"""Test if multiple args with the same tag are grouped."""
with ops.Graph().as_default():
    a = array_ops.constant([1.])
    b = array_ops.constant([2.])
    c = array_ops.constant([3.])
    d = array_ops.constant([4.])
    custom = op_hint.OpHint("test_tag")
    a = custom.add_input(
        a, tag="mytag", aggregate=op_hint.OpHint.AGGREGATE_STACK)
    b, = custom.add_inputs(b)
    c = custom.add_input(
        c, tag="mytag", aggregate=op_hint.OpHint.AGGREGATE_STACK)
    d = custom.add_input(
        d, tag="mytag2", aggregate=op_hint.OpHint.AGGREGATE_STACK)
    res = math_ops.add(math_ops.mul(a, b), math_ops.mul(c, b))
    custom.add_outputs([res])
    with self.cached_session():
        self.assertEqual(self._get_input_index(a), 0)
        self.assertEqual(self._get_sort_index(a), 0)
        self.assertEqual(self._get_input_index(b), 1)
        self.assertEqual(self._get_sort_index(b), 0)
        self.assertEqual(self._get_input_index(c), 0)
        self.assertEqual(self._get_sort_index(c), 1)
