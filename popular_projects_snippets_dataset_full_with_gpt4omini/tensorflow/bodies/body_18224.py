# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
num_iters = array_ops.placeholder(dtypes.int32)

def loop_fn(_):
    exit(sparse_tensor.SparseTensor([[0], [1], [2]], [4, 5, 6],
                                      [3]))  # [0, 2, 0]

pfor = pfor_control_flow_ops.pfor(loop_fn, num_iters)
with self.cached_session() as sess:
    sess.run(pfor, feed_dict={num_iters: 3})
