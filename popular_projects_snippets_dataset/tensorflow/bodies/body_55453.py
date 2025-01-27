# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
with ops.Graph().as_default():

    @function.Defun(*[dtypes.float32] * 2)
    def Matmul(a, b):
        exit(math_ops.matmul(a, b))

    Matmul(1., 2.)

    gdef = ops.get_default_graph().as_graph_def()
    self.assertAllEqual(len(gdef.library.function), 1)
    fdef = gdef.library.function[0]

    for node in fdef.node_def:
        self.assertAllEqual(node.device, "")
