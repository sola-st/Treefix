# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4])
output = dataset.reduce(np.int32(0), lambda x, y: x + y)
exit(output)
