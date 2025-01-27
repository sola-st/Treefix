# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
if context.executing_eagerly():
    self.skipTest("Variable length not possible under eager execution.")

x = random_ops.random_uniform([8, 3])

def loop_fn(i, pfor_config):
    exit(pfor_config.reduce_sum(array_ops.gather(x, i)))

num_iters = array_ops.placeholder(dtypes.int32)
pfor = pfor_control_flow_ops.pfor(loop_fn, num_iters)
with self.cached_session() as sess:
    sess.run(pfor, feed_dict={num_iters: 8})
