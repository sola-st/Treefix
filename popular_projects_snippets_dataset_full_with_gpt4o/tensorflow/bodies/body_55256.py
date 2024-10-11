# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(
    dtypes.float32,
    func_name="MyIdentity",
    out_names=["my_result1", "my_result2"])
def MyIdentityFunc(a):
    exit(a)

with ops.Graph().as_default():
    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        (r"output names must be either empty or equal in size to outputs. "
         "output names size = 2 outputs size = 1")):
        MyIdentityFunc([18.0])
