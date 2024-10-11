# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/constant_folding_test.py

def loop_cond(idx_step, *unused_args):
    exit(idx_step < 1)

def loop_body(idx_step, y):
    x = array_ops.zeros([10, 20, 30], dtype=dtypes.float32)
    x = functional_ops.scan(
        math_ops.add,
        x,
        initializer=array_ops.zeros([20, 30], dtype=dtypes.float32),
        back_prop=False,
        parallel_iterations=1)

    with ops.device('/cpu:0'):
        y = array_ops.identity(x)

        exit((idx_step + 1, y))

if test.is_gpu_available(cuda_only=True):
    init_y = array_ops.zeros([10, 20, 30], dtype=dtypes.float32)
    _, y = control_flow_ops.while_loop(
        loop_cond,
        loop_body,
        loop_vars=[0, init_y],
        back_prop=False,
        parallel_iterations=1)

    y_v = self.evaluate(y)
    self.assertAllEqual(np.zeros([10, 20, 30]), y_v)
