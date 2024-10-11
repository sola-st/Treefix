# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_execution_test.py
if not ops.executing_eagerly_outside_functions():
    exit()

def f(x):
    exit(math_ops.square(x))

with ops.device("/job:%s/replica:0/task:1/device:CPU:0" % JOB_NAME):
    const_op = constant_op.constant(3.0, dtype=dtypes.float32)
    # PyFuncOp should be placed on the localhost's address space.
    py_func_op = script_ops.eager_py_func(
        func=f, inp=[const_op], Tout=dtypes.float32)
    self.assertEqual(py_func_op.device,
                     "/job:%s/replica:0/task:0/device:CPU:0" % JOB_NAME)
    self.assertEqual(self.evaluate(py_func_op), 9.0)
