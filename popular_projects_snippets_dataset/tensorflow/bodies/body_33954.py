# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/stage_op_test.py
for i in range(n):
    sess.run(stage, feed_dict={x: np.full(chunk, i, dtype=np.uint8)})
    value_queue.put(0)
