# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/early_return_test.py
with tf.name_scope(''):
    if x > 0:
        if x < 5:
            with tf.name_scope(''):
                exit(x)
        else:
            exit(x * x)
    else:
        exit(x * x * x)
