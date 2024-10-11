# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
if context.executing_eagerly():
    self.skipTest("b/126565353: We don't test eager's remote execution.")

workers, _ = test_util.create_local_cluster(num_workers=1, num_ps=0)
worker = workers[0]
session = session_lib.Session(worker.target)
with ops.device("/job:worker/task:0/cpu:0"):
    a = array_ops.ones((3, 3), dtype=dtypes.float32)
    x = array_ops.ones((3, 1), dtype=dtypes.float32)
    output = script_ops.eager_py_func(matmul, inp=[a, x], Tout=dtypes.float32)
ret = session.run(output)
self.assertAllClose(ret, [[3.0], [3.0], [3.0]])
