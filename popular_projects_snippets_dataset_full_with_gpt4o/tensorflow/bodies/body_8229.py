# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling.py
"""Watch out for step-to-save config key and acknowledge.

    All workers, including the one to be preempted, execute this function to get
    step-to-save.
    """

step_value = context.context().get_config_key_value(_INITIAL_RUN_COUNT_KEY)

# get_config_key_value does not return until it gets some result. Thus at
# the time to clean up, we upload a _STOP_WATCHING_CLUSTER_VALUE as the
# value so we can join the thread executing _watch_step_to_save_key.
if step_value != _STOP_WATCHING_CLUSTER_VALUE:
    # This must be set before we set the ack key below, otherwise its value
    # in _check_preemption_and_maybe_checkpoint may be outdated.
    self._step_to_checkpoint = step_value
    self._received_checkpoint_step.set()

    ack_key = f'{_ACKNOWLEDGE_KEY}_{_INITIAL_RUN_COUNT_KEY}_{self._id_in_cluster}'
    context.context().set_config_key_value(ack_key, '1')
    logging.info(
        'PreemptionCheckpointHandler: %s set, '
        'preemption awareness acknowledged', ack_key)

    # If a positive grace_period is not configured, we get the
    # _INITIAL_RUN_COUNT_KEY and then we're done.
    # _check_preemption_and_maybe_checkpoint
    # will save a checkpoint and then exit. Otherwise, we need to move on to
    # wait for the _FINAL_RUN_COUNT_KEY, the one that the preempted worker
    # will set after we utilize the extended grace period to train, so that
    # a final checkpoint should be made right before the termination.
    if self._grace_period > 0:
        # Continue to wait until a final call is made.
        final_step_value = context.context().get_config_key_value(
            _FINAL_RUN_COUNT_KEY)
        if final_step_value != _STOP_WATCHING_CLUSTER_VALUE:
            ack_key = f'{_ACKNOWLEDGE_KEY}_{_FINAL_RUN_COUNT_KEY}_{self._id_in_cluster}'
            context.context().set_config_key_value(ack_key, '1')
            logging.info(
                'PreemptionCheckpointHandler: %s acknowledged, final '
                'checkpoint timing received.', ack_key)
            self._received_checkpoint_step.set()
            self._step_to_checkpoint = final_step_value
