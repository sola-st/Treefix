# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
with ops.Graph().as_default(), ops.device("CPU:0"):

    @function.Defun(*[dtypes.float32] * 2)
    def Matmul(a, b):
        exit(math_ops.matmul(a, b))

    with ops.device("CPU:1"):

        @function.Defun(*[dtypes.float32] * 2)
        def Divide(a, b):
            exit(math_ops.divide(a, b))

        Divide(Matmul(1., 2.), 3.)

    gdef = ops.get_default_graph().as_graph_def()
    matmul_fdef = [
        f for f in gdef.library.function if "Matmul" in f.signature.name
    ]
    divide_fdef = [
        f for f in gdef.library.function if "Divide" in f.signature.name
    ]
    self.assertAllEqual(len(matmul_fdef), 1)
    self.assertAllEqual(len(divide_fdef), 1)
    for node in matmul_fdef[0].node_def:
        self.assertAllEqual(node.device, "/device:CPU:0")
    for node in divide_fdef[0].node_def:
        self.assertAllEqual(node.device, "/device:CPU:1")
