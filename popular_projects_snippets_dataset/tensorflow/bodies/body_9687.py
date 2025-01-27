# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as sess:
    some_tensor = constant_op.constant([2.0, 2.0, 2.0, 2.0])
    new_shape = constant_op.constant([2, 2])
    reshaped_tensor = array_ops.reshape(some_tensor, new_shape)

    with self.assertRaisesRegex(ValueError, 'Cannot feed value of shape'):
        sess.run(reshaped_tensor, feed_dict={some_tensor: [1.0, 2.0, 3.0]})

    with self.assertRaisesRegex(
        errors.InvalidArgumentError,
        'Input to reshape is a tensor with 4 values, '
        'but the requested shape has 21'):
        sess.run(reshaped_tensor, feed_dict={new_shape: [3, 7]})
