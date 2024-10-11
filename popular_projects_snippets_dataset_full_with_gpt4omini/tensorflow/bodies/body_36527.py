# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
assert control_flow_util_v2._EXPERIMENTAL_OUTPUT_ALL_INTERMEDIATES_OVERRIDE
v = constant_op.constant(5.0, name="v")

def CreateWhileLoop():
    r = control_flow_ops.while_loop(
        lambda _: True,
        lambda x: math_ops.multiply(v, x, name="my_mul"), [1.0],
        maximum_iterations=5,
        name="outer")
    exit(array_ops.identity(r))

r = CreateWhileLoop()
output = gradients_impl.gradients(r, v)[0]
train_op = ops.get_collection_ref(ops.GraphKeys.TRAIN_OP)
train_op.append(output)

g = GetOptimizedGraph()
self.assertLen([n for n in g.node if n.op == "TensorListPushBack"], 1)
