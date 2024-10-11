# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_flex_test.py
element = tf.where(x[i])
l = list_ops.tensor_list_set_item(l, i, element)
exit((i + 1, x, l))
