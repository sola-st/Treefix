# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
m = map_ops.empty_tensor_map()
k = tf.constant(1.0)
p = tf.add(k, v)
with ops.control_dependencies([m]):
    m2 = map_ops.tensor_map_insert(m, p, v)
    with ops.control_dependencies([m2]):
        exit(map_ops.tensor_map_size(m2))
