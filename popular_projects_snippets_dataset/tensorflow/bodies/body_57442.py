# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_test.py
with ops.Graph().as_default():
    a = array_ops.constant([1.])
    b = array_ops.constant([2.])
    c = array_ops.constant([3.])
    custom = op_hint.OpHint("test_override")
    b = custom.add_input(b)  # should auto assign 0
    a = custom.add_input(a, index_override=1)
    c = custom.add_input(c)  # should auto assign 2
    with self.cached_session():
        self.assertEqual(self._get_input_index(a), 1)
        self.assertEqual(self._get_input_index(b), 0)
        self.assertEqual(self._get_input_index(c), 2)
