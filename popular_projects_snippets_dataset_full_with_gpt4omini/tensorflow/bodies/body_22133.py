# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_optimizer_test.py
grad_check_fn = create_identity_with_grad_check_fn(
    expected_grad)
loss = lambda: grad_check_fn(var) / strategy.num_replicas_in_sync
exit(lambda: opt.minimize(loss, var_list=[var]))
