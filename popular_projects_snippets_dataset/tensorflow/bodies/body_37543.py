# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
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
