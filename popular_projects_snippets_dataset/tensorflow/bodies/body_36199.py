# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
with ops.device("/cpu:0"):
    exit(functional_ops.remote_call(
        args=[constant_op.constant([1.])] + _remote_fn.captured_inputs,
        Tout=[dtypes.float32],
        f=_remote_fn,
        target="/cpu:1")[0])
