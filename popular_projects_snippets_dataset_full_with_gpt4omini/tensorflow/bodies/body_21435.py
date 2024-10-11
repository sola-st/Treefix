# Extracted from ./data/repos/tensorflow/tensorflow/python/training/sync_replicas_optimizer_test.py
opt = training.SyncReplicasOptimizer(
    opt=gradient_descent.GradientDescentOptimizer(1.0),
    replicas_to_aggregate=1,
    total_num_replicas=1)
hook = opt.make_session_run_hook(True)
with self.assertRaisesRegex(ValueError, "apply_gradient should be called"):
    hook.begin()
