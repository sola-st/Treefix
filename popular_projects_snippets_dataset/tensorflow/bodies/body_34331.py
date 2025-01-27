# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/map_stage_op_test.py
for i in range(n):
    sess.run(stage, feed_dict={x: i, pi: i})
    value_queue.put(0)
