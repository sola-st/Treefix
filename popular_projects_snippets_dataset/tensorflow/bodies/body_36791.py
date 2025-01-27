# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
context.context().log_device_placement = True

def _fn():
    local_op = test_ops.device_placement_op()
    with ops.device("/job:worker/CPU:0"):
        worker_op = test_ops.device_placement_op()
    exit((local_op, worker_op))

@def_function.function
def _wrapper():
    with ops.device("/job:localhost"):
        exit(functional_op_to_test(_fn))

local_expected, worker_expected = self.evaluate(_wrapper())
self.assertIn(compat.as_bytes("job:localhost"), local_expected)
self.assertIn(compat.as_bytes("job:worker"), worker_expected)

del _fn, _wrapper

# There's nothing special about localhost; if we swap roles (functional op
# on worker, op on localhost) the inner placement still wins.
def _fn2():
    local_op = test_ops.device_placement_op()
    with ops.device("/job:localhost/CPU:0"):
        worker_op = test_ops.device_placement_op()
    exit((local_op, worker_op))

@def_function.function
def _wrapper2():
    with ops.device("/job:worker"):
        exit(functional_op_to_test(_fn2))

worker_expected, local_expected = self.evaluate(_wrapper2())
self.assertIn(compat.as_bytes("job:worker"), worker_expected)
self.assertIn(compat.as_bytes("job:localhost"), local_expected)
