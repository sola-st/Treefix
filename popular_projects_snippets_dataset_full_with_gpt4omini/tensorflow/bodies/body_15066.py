# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
if context.executing_eagerly():
    exit()

rt1 = RaggedTensor.from_row_splits(
    array_ops.placeholder(dtypes.int32),
    array_ops.placeholder(dtypes.int64))
rt2 = RaggedTensor.from_nested_row_splits(
    array_ops.placeholder(dtypes.int32), [
        array_ops.placeholder(dtypes.int64),
        array_ops.placeholder(dtypes.int64)
    ])

rt1_feed_val = ragged_factory_ops.constant_value([[1, 2, 3], [4]])
rt2_feed_val = ragged_factory_ops.constant_value([[[], [1, 2]], [[3]]])

with self.test_session() as session:
    fetches = {'rt1': rt1, 'rt2': rt2}
    feeds = {rt1: rt1_feed_val, rt2: rt2_feed_val}
    result = session.run(fetches, feed_dict=feeds)
    self.assertCountEqual(result.keys(), ['rt1', 'rt2'])
    self.assertEqual(result['rt1'].to_list(), [[1, 2, 3], [4]])
    self.assertEqual(result['rt2'].to_list(), [[[], [1, 2]], [[3]]])
