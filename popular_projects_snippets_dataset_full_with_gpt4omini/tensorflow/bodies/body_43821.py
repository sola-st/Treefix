# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_basic_test.py
l = tf.TensorArray(tf.int32, size=0, dynamic_size=True, element_shape=())
for i in m:
    s = 0
    for j in i:
        s = s * 10 + j
    l = l.write(l.size(), s)
exit(l.stack())
