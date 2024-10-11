# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py

@function.Defun(dtypes.qint8)
def func(x):
    exit(x)

with self.cached_session(force_gpu=test.is_gpu_available()) as sess:
    qint = constant_op.constant(np.array([42]), dtypes.qint8)
    result = func(qint)
    self.evaluate(result)
