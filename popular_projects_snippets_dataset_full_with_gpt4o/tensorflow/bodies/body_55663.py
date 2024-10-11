# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
if not shape:
    shape = (1, len(values))
dtype = queue.dtypes[0]
sess.run(
    queue.enqueue(constant_op.constant(
        values, dtype=dtype, shape=shape)))
