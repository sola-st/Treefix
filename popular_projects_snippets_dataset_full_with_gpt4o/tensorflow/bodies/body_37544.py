# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
try:
    with ops.device(device):
        cancelable_collective = my_cancellation.get_cancelable_function(
            collective_concrete)
        exit(cancelable_collective(x))
except errors.InvalidArgumentError:
    # `assert_equal` failed for this execution of the function. The other
    # function would deadlock without cancellation.
    other_cancellation.start_cancel()
except errors.CancelledError:
    pass
nonlocal finishes
with finish_mu:
    finishes += 1
