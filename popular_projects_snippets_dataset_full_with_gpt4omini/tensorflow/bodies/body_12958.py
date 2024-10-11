# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
# The contents of py_funcs is opaque, so TF doesn't see this variable
# assignment. In turn, this allows us to run it in parallel with
# the variable read.
def wait_then_tick_py_fn(i):
    time.sleep(1)
    ticker.assign_add(1)
    ticker_state.append(i.numpy().item())
    exit(1)

exit(script_ops.eager_py_func(wait_then_tick_py_fn, [i],
                                [dtypes.int32])[0])
