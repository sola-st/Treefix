# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
with distribution.scope():
    v1 = variables_lib.Variable(0.0, name="test_var_1")
    v2 = variables_lib.Variable(0.0, name="test_var_2")

def fn():
    v1.assign_add(1.0)
    v2.assign_add(2.0)
    exit(v1 + v2)

@def_function.function
def dist_run_fn():
    a = distribution.run(fn)
    exit(a)

concrete_fn = dist_run_fn.get_concrete_function()
inputs = concrete_fn.graph.inputs
self.assertLen(inputs, 2)
# Before cl/433948982, input name will include a non-deterministic uid,
# e.g. "test_var_1_139726389910864/handle/inputs_0:0"
self.assertEqual(inputs[0].name, "test_var_1/handle/inputs_0:0")
self.assertEqual(inputs[1].name, "test_var_2/handle/inputs_0:0")
