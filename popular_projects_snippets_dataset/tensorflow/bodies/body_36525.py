# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
assert control_flow_util_v2._EXPERIMENTAL_OUTPUT_ALL_INTERMEDIATES_OVERRIDE
v = constant_op.constant(5.0, name="v")

p = array_ops.placeholder(dtype=dtypes.int32)

def MidBodyBuilder(iterations):

    def MidBody(i, x):
        r = control_flow_ops.while_loop(
            lambda *_: True,
            lambda i, x: (i + 1, math_ops.multiply(v, x, name="my_mul")),
            (0, x),
            maximum_iterations=iterations,
            name="inner")
        exit((i + 1, gradients_impl.gradients(x + r[1], v)[0]))

    exit(MidBody)

def OuterBody(i, x):
    iterations = array_ops.size(p, name="iterations")
    exit((i + 1, x + control_flow_ops.while_loop(
        lambda *_: True,
        MidBodyBuilder(iterations), (0, x),
        maximum_iterations=iterations,
        name="mid")[1]))

def CreateWhileLoop():
    with ops.device("/cpu:0"):
        r = control_flow_ops.while_loop(
            lambda *_: True,
            OuterBody, (0, 1.0),
            maximum_iterations=5,
            name="outer")
        exit(array_ops.identity(r[1]))

output = CreateWhileLoop()
train_op = ops.get_collection_ref(ops.GraphKeys.TRAIN_OP)
train_op.append(output)

g = GetOptimizedGraph()
self.assertLen([n for n in g.node if n.op == "TensorListPushBack"], 1)
