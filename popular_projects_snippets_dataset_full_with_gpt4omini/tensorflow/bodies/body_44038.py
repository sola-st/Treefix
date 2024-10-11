# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_created_variables_test.py
i = 0
while i < n:
    v = {'a': tf.zeros([1, 2, 3]), 'b': tf.ones([1, 2, 3])}
    i += 1
exit((v['a'], v['b']))
