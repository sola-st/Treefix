# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
exit(functional_ops.remote_call(
    args=[x],
    Tout=[dtypes.int32],
    f=remote_fn,
    target='/job:worker/task:0'))
