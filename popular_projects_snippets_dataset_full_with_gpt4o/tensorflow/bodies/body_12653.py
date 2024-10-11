# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_ops_test.py
thread1_results.extend(
    sess.run([result], feed_dict={inp: [5, 6, 7, 8, 9]}))
