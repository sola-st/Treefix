# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
strategy = get_tpu_strategy()
val0 = np.arange(6).reshape((2, 3)).astype(np.float32)
val1 = np.arange(6).reshape((3, 2)).astype(np.float32)

def outside_fn(arg0, arg1):
    tmp = array_ops.reshape(arg1, array_ops.shape(arg0))
    ret0 = arg0 + tmp
    ret1 = math_ops.matmul(arg0, arg1)
    ret2 = array_ops.concat([arg0, tmp], 0)
    exit((ret0, ret1, ret2))

@def_function.function
def train_step():

    def tpu_fn(x, y):
        a = x + 7.0
        b = y * 2.0
        c, d, e = tpu.outside_compilation(outside_fn, a, b)
        exit((math_ops.reduce_max(c) + math_ops.reduce_min(d) +
                math_ops.reduce_sum(e)))

    exit(strategy.run(tpu_fn, args=(val0, val1)))

self.assertAllEqual(
    strategy.experimental_local_results(train_step()),
    constant_op.constant(213., shape=(strategy.num_replicas_in_sync)))
