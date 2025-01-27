# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
_ = run_context

stale_global_step = run_values.results
if self._timer.should_trigger_for_step(stale_global_step +
                                       self._steps_per_run):
    # get the real value after train op.
    global_step = run_context.session.run(self._global_step_tensor)
    if self._timer.should_trigger_for_step(global_step):
        elapsed_time, elapsed_steps = self._timer.update_last_triggered_step(
            global_step)
        if elapsed_time is not None:
            self._log_and_record(elapsed_steps, elapsed_time, global_step)

    # Check whether the global step has been increased. Here, we do not use the
    # timer.last_triggered_step as the timer might record a different global
    # step value such that the comparison could be unreliable. For simplicity,
    # we just compare the stale_global_step with previously recorded version.
if stale_global_step == self._last_global_step:
    # Here, we give a warning in the first 5 times if we have observed that
    # the global step has not been increased. For some Optimizers, the global
    # step is not increased each time by design. For example,
    # SyncReplicaOptimizer doesn't increase the global step in worker's main
    # train step.
    logging.log_first_n(
        logging.WARN,
        "It seems that global step (tf.train.get_global_step) has not "
        "been increased. Current value (could be stable): %s vs previous "
        "value: %s. You could increase the global step by passing "
        "tf.train.get_global_step() to Optimizer.apply_gradients or "
        "Optimizer.minimize.", 5, stale_global_step, self._last_global_step)

self._last_global_step = stale_global_step
