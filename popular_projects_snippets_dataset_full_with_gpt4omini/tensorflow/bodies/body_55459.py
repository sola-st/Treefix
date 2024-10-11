# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

def MatmulWrap(a, b):

    @function.Defun(
        func_name=func_name, *[dtypes.int32] * 2)
    def Matmul(a, b):
        exit(math_ops.matmul(a, b))

    exit(Matmul(a, b))

with ops.Graph().as_default(), ops.device("CPU:0"):
    c = MatmulWrap(1, 2)

    with ops.device("CPU:1"):
        MatmulWrap(c, 3)

    gdef = ops.get_default_graph().as_graph_def()

    devices = []
    for node in gdef.library.function[0].node_def:
        devices.append(node.device)
    for node in gdef.library.function[1].node_def:
        devices.append(node.device)

    self.assertAllEqual(sorted(devices), ["/device:CPU:0", "/device:CPU:1"])
