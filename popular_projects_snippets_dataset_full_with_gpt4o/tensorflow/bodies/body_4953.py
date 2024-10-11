# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
variables1 = [
    variables_lib.Variable([1]),
    variables_lib.Variable([1]),
]
s = sharded_variable.ShardedVariable(variables1)
variables2 = [
    variables_lib.Variable([2]),
    variables_lib.Variable([2]),
]
s2 = sharded_variable.ShardedVariable(variables2)

trace_count = [0]

@def_function.function
def func(sharded_var):
    trace_count[0] = trace_count[0] + 1
    sharded_var.assign([0, 0])

func(s)
self.assertAllEqual(ops.convert_to_tensor(s), [0, 0])
self.assertEqual(trace_count[0], 1)
func(s2)
self.assertAllEqual(ops.convert_to_tensor(s2), [0, 0])
self.assertEqual(trace_count[0], 1)
