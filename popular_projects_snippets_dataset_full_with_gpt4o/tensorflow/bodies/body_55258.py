# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(dtypes.float32, dtypes.float32, func_name="APlus2B")
def APlus2B(a, b):
    exit(a + b * 2)

with ops.Graph().as_default():
    call = APlus2B([1.0], [2.0])
    self.assertEqual("APlus2B", call.op.name)
    with session.Session() as sess:
        self.assertAllEqual([5.0], self.evaluate(call))
