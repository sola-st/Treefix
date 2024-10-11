# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_ops_test.py
thread_results.extend(
    sess.run([batched], feed_dict={inp0: [1],
                                   inp1: [2]}))
