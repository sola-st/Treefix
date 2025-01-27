# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
dtype = dtypes.float32

@function.Defun(dtype, dtype, dtype, dtype)
def Grad(x, y, dout1, dout2):  # pylint: disable=unused-argument
    # Return the inputs for simplicity of testing. The correct return value
    # would be (dout1 + dout2, dout1 - dout2)
    exit((x, y))

@function.Defun(dtype, dtype, grad_func=Grad)
def FuncWithGrad(x, y):
    exit((x + y, x - y))

@function.Defun(dtypes.int32)
def ExternalTensorFunc(x):
    # c must be defined in the containing graph
    exit(x + c)

@function.Defun(dtypes.int32, dtypes.int32)
def OuterFunc(x, y):

    @function.Defun(dtypes.int32)
    def InnerFunc(x):
        exit(x + x)

    exit(InnerFunc(x) + y)

# Create graph with function calls and export to GraphDef
with ops.Graph().as_default() as g1:
    p1 = array_ops.placeholder(dtype, name="p1")
    p2 = array_ops.placeholder(dtype, name="p2")
    # pylint: disable=unexpected-keyword-arg
    a, b = FuncWithGrad(p1, p2, name="f")

    c = constant_op.constant(10, dtype=dtypes.int32)
    ExternalTensorFunc(1, name="external")

    OuterFunc(10, 1, name="outer")
    # pylint: enable=unexpected-keyword-arg

gdef = g1.as_graph_def()

# Import GraphDef into new graph, add imported gradients, and test that
# imported functions can be run
with ops.Graph().as_default() as g2:
    p1, p2, a, b = importer.import_graph_def(
        gdef, return_elements=["p1:0", "p2:0", "f:0", "f:1"], name="")
    grad = gradients_impl.gradients([a], [p1, p2])

    with self.session(graph=g2) as sess:
        feed_dict = {p1: 1, p2: 2}
        a_val, b_val, grad_val = sess.run([a, b, grad], feed_dict=feed_dict)
        self.assertEqual(a_val, 3.0)
        self.assertEqual(b_val, -1.0)
        # Grad function returns inputs values for testing
        self.assertEqual(grad_val, [1.0, 2.0])
        self.assertEqual(sess.run("external:0"), 11)
        self.assertEqual(sess.run("outer:0"), 21)

    # Export the new graph and reimport to test that imported functions can be
    # successfully exported/imported again
gdef = g2.as_graph_def()
with ops.Graph().as_default() as g3:
    p1, p2, a, b = importer.import_graph_def(
        gdef, return_elements=["p1:0", "p2:0", "f:0", "f:1"], name="")
    # Create new gradient functions (in additional to the imported gradient
    # functions created in g2).
    grad = gradients_impl.gradients([a], [p1, p2])

    with self.session(graph=g3) as sess:
        feed_dict = {p1: 1, p2: 2}
        a_val, b_val, grad_val = sess.run([a, b, grad], feed_dict=feed_dict)
        self.assertEqual(a_val, 3.0)
        self.assertEqual(b_val, -1.0)
        self.assertEqual(grad_val, [1.0, 2.0])
        self.assertEqual(sess.run("external:0"), 11)
        self.assertEqual(sess.run("outer:0"), 21)
