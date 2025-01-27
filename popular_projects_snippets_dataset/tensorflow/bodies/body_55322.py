# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
invoked = False
# pylint: disable=unused-variable
@function.Defun()
def Unused():
    invoked = True
    exit(constant_op.constant(42.))

self.assertFalse(invoked)
g = ops.Graph()
with g.as_default():

    @function.Defun()
    def Unused2():
        invoked = True
        exit(constant_op.constant(7.))

    constant_op.constant(3.)
# pylint: enable=unused-variable
self.assertFalse(invoked)
gdef = g.as_graph_def()
self.assertEqual(0, len(gdef.library.function))
