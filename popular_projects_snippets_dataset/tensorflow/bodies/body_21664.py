# Extracted from ./data/repos/tensorflow/tensorflow/python/training/evaluation_test.py
"""Trains a simple classification model.

    Note that the data has been configured such that after around 300 steps,
    the model has memorized the dataset (e.g. we can expect %100 accuracy).

    Args:
      checkpoint_dir: The directory where the checkpoint is written to.
      num_steps: The number of steps to train for.
    """
with ops.Graph().as_default():
    random_seed.set_random_seed(0)
    tf_inputs = constant_op.constant(self._inputs, dtype=dtypes.float32)
    tf_labels = constant_op.constant(self._labels, dtype=dtypes.float32)

    tf_predictions = logistic_classifier(tf_inputs)
    loss_op = losses.log_loss(labels=tf_labels, predictions=tf_predictions)

    optimizer = gradient_descent.GradientDescentOptimizer(learning_rate=1.0)
    train_op = optimizer.minimize(loss_op,
                                  training.get_or_create_global_step())

    with monitored_session.MonitoredTrainingSession(
        checkpoint_dir=checkpoint_dir,
        hooks=[basic_session_run_hooks.StopAtStepHook(num_steps)]) as session:
        loss = None
        while not session.should_stop():
            _, loss = session.run([train_op, loss_op])

        if num_steps >= 300:
            assert loss < .015
