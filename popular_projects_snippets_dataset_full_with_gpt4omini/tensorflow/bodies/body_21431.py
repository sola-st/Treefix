# Extracted from ./data/repos/tensorflow/tensorflow/python/training/sync_replicas_optimizer_test.py
sessions = []
graphs = []
train_ops = []
for worker_id in range(num_workers):
    graph = ops.Graph()
    is_chief = (worker_id == 0)
    with graph.as_default():
        with ops.device("/job:ps/task:0"):
            global_step = variables.VariableV1(
                0, name="global_step", trainable=False)
            var_0 = variables.VariableV1(0.0, name="v0")
        with ops.device("/job:ps/task:1"):
            var_1 = variables.VariableV1(1.0, name="v1")
            var_sparse = variables.VariableV1([[3.0], [4.0]], name="v_sparse")

        with ops.device("/job:worker/task:" + str(worker_id)):
            grads_0 = constant_op.constant(0.1 + worker_id * 0.2)
            grads_1 = constant_op.constant(0.9 + worker_id * 0.2)
            # This is to test against sparse gradients.
            grads_sparse = indexed_slices.IndexedSlices(
                constant_op.constant(
                    [0.1 + worker_id * 0.2], shape=[1, 1]),
                constant_op.constant([1]),
                constant_op.constant([2, 1]))
            sgd_opt = gradient_descent.GradientDescentOptimizer(2.0)
            sync_rep_opt = training.SyncReplicasOptimizer(
                sgd_opt,
                replicas_to_aggregate=replicas_to_aggregate,
                total_num_replicas=num_workers)
            train_op = [
                sync_rep_opt.apply_gradients(
                    zip([grads_0, grads_1, grads_sparse],
                        [var_0, var_1, var_sparse]),
                    global_step=global_step)
            ]
            sync_replicas_hook = sync_rep_opt.make_session_run_hook(
                is_chief, num_tokens=num_workers)

        # Creates MonitoredSession
        session = training.MonitoredTrainingSession(
            master=workers[worker_id].target,
            is_chief=is_chief,
            hooks=[sync_replicas_hook])

    sessions.append(session)
    graphs.append(graph)
    train_ops.append(train_op)

exit((sessions, graphs, train_ops))
