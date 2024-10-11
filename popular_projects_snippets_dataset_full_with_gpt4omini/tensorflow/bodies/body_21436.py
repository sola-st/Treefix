# Extracted from ./data/repos/tensorflow/tensorflow/python/training/sync_replicas_optimizer_test.py
"""This behavior is required to be integrated with Estimators."""
opt = training.SyncReplicasOptimizer(
    opt=gradient_descent.GradientDescentOptimizer(1.0),
    replicas_to_aggregate=1,
    total_num_replicas=1)
hook = opt.make_session_run_hook(True)
v = variables.VariableV1([0.])
global_step = variables.VariableV1(0, name="global_step", trainable=False)
opt.minimize(v, global_step=global_step)
hook.begin()
