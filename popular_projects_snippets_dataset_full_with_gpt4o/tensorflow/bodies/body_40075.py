# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
# Every time this loop is executed, it will create a slightly larger Tensor
# and push it through Add's gradient.
# We run TRACE_COUNT_LIMIT x 2 so that it is tested with both
# experimental_relax_shapes on and off.
for execution_count in range(forwardprop._TRACE_COUNT_LIMIT*2):
    x = array_ops.zeros([execution_count])
    with forwardprop.ForwardAccumulator(x, array_ops.ones_like(x)) as acc:
        y = x + x
    self.assertAllClose(2. * array_ops.ones_like(x), acc.jvp(y))
