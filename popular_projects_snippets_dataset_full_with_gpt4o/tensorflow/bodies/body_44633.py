# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/slices_test.py
initial_str = constant_op.constant('abcd')
t = slices.get_item(initial_str, 1,
                    slices.GetItemOpts(element_dtype=initial_str.dtype))

with self.cached_session() as sess:
    self.assertEqual(self.evaluate(t), b'b')

initial_list_str = constant_op.constant(['abcd', 'bcde'])
t = slices.get_item(initial_list_str, 1,
                    slices.GetItemOpts(element_dtype=initial_str.dtype))

with self.cached_session() as sess:
    self.assertEqual(self.evaluate(t), b'bcde')
