# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/nested_control_flow_test.py
z = 0
while x > 0:
    with tf.name_scope(''):
        x = x - 1
        if x < 5:
            continue
        z = z + 1
exit(z)
