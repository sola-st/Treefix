# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
if not isinstance(left_list, list):
    left_list, right_list = [left_list], [right_list]

for left, right in zip(left_list, right_list):
    self.assertEqual(type(left), type(right))

    # Convert Mirrored to a list since sess.run(Mirrored) only returns one
    # value.
    if isinstance(left, value_lib.Mirrored):
        left, right = left.values, right.values
    else:
        # When there's only one replica Mirrored is automatically unwrapped.
        left, right = [left], [right]

    for left_value, right_value in zip(left, right):
        self.assertEqual(
            device_util.resolve(left_value.device),
            device_util.resolve(right_value.device))

    # Densify IndexedSlices.
    left = [ops.convert_to_tensor(v) for v in left]
    right = [ops.convert_to_tensor(v) for v in right]
    if not context.executing_eagerly():
        left, right = sess.run((left, right), options=run_options)
    for left_value, right_value in zip(left, right):
        self.assertAllEqual(left_value, right_value)
