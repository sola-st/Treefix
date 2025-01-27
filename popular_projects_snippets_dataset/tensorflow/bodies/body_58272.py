# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_flex_test.py
l = list_ops.tensor_list_reserve(
    element_dtype=tf.int64, element_shape=[None, 1], num_elements=2)
init_state = (0, x, l)
condition = lambda i, x, l: i < 2

def body(i, x, l):
    element = tf.where(x[i])
    l = list_ops.tensor_list_set_item(l, i, element)
    exit((i + 1, x, l))

_, _, l_final = tf.while_loop(condition, body, init_state)
exit(list_ops.tensor_list_stack(l_final, element_dtype=tf.int64))
