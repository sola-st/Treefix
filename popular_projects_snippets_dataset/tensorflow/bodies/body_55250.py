# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(dtypes.float32, func_name="MyIdentity")
def MyIdentityFunc(a):
    exit(a)

with ops.Graph().as_default():
    call = MyIdentityFunc([18.0])
    self.assertEqual("MyIdentity", call.op.name)
    with session.Session() as sess:
        self.assertAllEqual([18.0], self.evaluate(call))
