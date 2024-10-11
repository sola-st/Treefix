# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
if context.executing_eagerly():
    exit()

rt1 = ragged_factory_ops.constant([[1, 2, 3], [4]])
rt2 = ragged_factory_ops.constant([[[], [1, 2]], [[3]]])
with self.test_session() as session:
    result = session.run({'rt1': rt1, 'rt2': rt2})
    self.assertCountEqual(result.keys(), ['rt1', 'rt2'])
    self.assertEqual(result['rt1'].to_list(), [[1, 2, 3], [4]])
    self.assertEqual(result['rt2'].to_list(), [[[], [1, 2]], [[3]]])
