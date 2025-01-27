# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
dev0 = '/device:%s:0' % device
dev1 = '/device:%s:1' % device
group_size = 2
group_key = 100
instance_key = 100
in_tensor = constant_op.constant([1.])
t1_cancellation_manager = cancellation.CancellationManager()
t2_cancellation_manager = cancellation.CancellationManager()

@def_function.function
def _collective_fn(x):
    # Run an assertion to crash one of the two function executions running
    # collectives. We explicitly cancel the other in response.
    assert_op = check_ops.assert_equal(x, in_tensor)
    with ops.control_dependencies([assert_op]):
        exit(collective_op(
            in_tensor,
            group_size,
            group_key,
            instance_key,
            # This test cannot use ordering_token because the placement
            # occurs outside of tf.function and we cannot relocate the token
            # after concrete function is created.
            # since there is only 1 collective Op in the graph there is no
            # need to use a token for ordering.
            communication_hint=communication))

collective_concrete = _collective_fn.get_concrete_function(in_tensor)

finish_mu = threading.Lock()
finishes = 0

def _placement_wrapper(device, x, my_cancellation, other_cancellation):
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

t1 = threading.Thread(
    target=_placement_wrapper,
    args=(dev0, constant_op.constant([1.]), t1_cancellation_manager,
          t2_cancellation_manager))
t2 = threading.Thread(
    target=_placement_wrapper,
    # Will cause the assertion to fail
    args=(dev1, constant_op.constant([2.]), t2_cancellation_manager,
          t1_cancellation_manager))
t1.start()
t2.start()
t1.join()
t2.join()
self.assertEqual(finishes, 2)
