# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(func_name="AConstant")
def AConstant():
    exit(constant_op.constant([42]))

with ops.Graph().as_default():

    call = AConstant()
    self.assertEqual("AConstant", call.op.name)
    with session.Session() as sess:
        self.assertAllEqual([42], self.evaluate(call))
