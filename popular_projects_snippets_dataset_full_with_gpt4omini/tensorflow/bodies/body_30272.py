# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
model_input = array_ops.placeholder(dtypes.float32, shape=(1, 10))

# check that we fail during static shape inference if sizes are known
with self.assertRaises(ValueError):
    # pylint: disable=expression-not-assigned
    array_ops.split(model_input, [4], axis=1)[0]
    # pylint: enable=expression-not-assigned

model_input = array_ops.placeholder(dtypes.float32)
inp = np.zeros((1, 10))
# check that we still fail at runtime if the shapes were unknown
with self.cached_session() as sess:
    with self.assertRaises(errors_impl.InvalidArgumentError):
        sess.run(array_ops.split(model_input, [4]), {model_input: inp})

    # scalar Tensors are not permitted as num_splits
for axis in [0, -2]:
    with self.cached_session() as sess:
        with self.assertRaises(ValueError):
            # pylint: disable=expression-not-assigned
            sess.run(
                array_ops.split(
                    array_ops.ones([4, 4]),
                    num_or_size_splits=constant_op.constant(2),
                    axis=axis))
            # pylint: enable=expression-not-assigned

    # test that none split dimensions remain, even if we don't know how
    # the split_dim will be split, but we do know the axis
result = array_ops.split(
    array_ops.ones([5, 2]), array_ops.constant([2, 1, 2]) * 1, axis=0)

self.assertEqual(result[0].shape[1], 2)
self.assertEqual(result[1].shape[1], 2)
self.assertEqual(result[2].shape[1], 2)

model_input2 = array_ops.placeholder(dtypes.float32, shape=[None, 2])
result = array_ops.split(model_input2, [2, 2], axis=0)[0]

with self.cached_session() as sess:
    sess.run(result, feed_dict={model_input2: np.ones([4, 2])})
