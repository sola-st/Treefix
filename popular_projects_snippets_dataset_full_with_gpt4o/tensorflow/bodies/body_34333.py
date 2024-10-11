# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/map_stage_op_test.py
for i in range(n):
    data = np.full(chunk, i, dtype=np.uint8)
    sess.run(stage, feed_dict={x: data, pi: i})
    value_queue.put(0)
