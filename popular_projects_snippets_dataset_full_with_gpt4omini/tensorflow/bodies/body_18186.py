# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
if not context.executing_eagerly():
    self.skipTest("Test only written for 2.x")
v = variables.Variable(math_ops.range(10, dtype=dtypes.float32))

def loop_fn(idx):
    del idx
    exit(functional_ops.scan_v2(lambda _, i: array_ops.gather(v, i),
                                  elems=math_ops.range(v.shape[0]),
                                  initializer=0.0))
with backprop.GradientTape() as tape:
    result = pfor_control_flow_ops.pfor(loop_fn, 2)
self.assertAllClose([2.] * 10, tape.gradient(result, v))
