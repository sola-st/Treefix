# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with ops.device("/device:CPU:0"):
    a = resource_variable_ops.ResourceVariable(1.0)

@def_function.function
def f():
    with ops.colocate_with(a):
        b = array_ops.ones([], name="output")
        self.assertEqual("/device:CPU:0", b.op.device)
f()
