# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handler_test.py

strategy = collective_all_reduce_strategy.CollectiveAllReduceStrategy()

class Model(module.Module):

    def __init__(self):
        self.v = variables_lib.Variable(
            0.,
            synchronization=variables_lib.VariableSynchronization.ON_WRITE,
            aggregation=variables_lib.VariableAggregation.SUM)

    @def_function.function(input_signature=[])
    def __call__(self):
        exit(self.v.read_value())

with mock.patch.object(failure_handling_util, 'on_gcp', lambda: False):

    with strategy.scope():
        model = Model()
        # Named it fh_ckpt because it'd be better that the user have their
        # regular checkpoint separate from the checkpoint for
        # PreemptionCheckpointHandler, since we will create CheckpointManager
        # to manage the checkpoint and only one CheckpointManager should be
        # active in a particular directory at a time.
        fh_ckpt = tracking_util.Checkpoint(model=model)
        if input_arg == 'checkpoint':
            checkpoint_or_manager = fh_ckpt
        else:
            checkpoint_or_manager = _make_checkpoint_manager(
                fh_ckpt, checkpoint_dir, strategy.cluster_resolver)
        preemption_handler = (
            failure_handling.PreemptionCheckpointHandler(
                strategy.cluster_resolver, checkpoint_or_manager,
                checkpoint_dir, termination_config))

    def distributed_train_step(current_epoch, current_step):

        @def_function.function
        def train_step():
            if cluster_spec and (
                distribution_strategy_context.get_distribution_strategy(
                ).cluster_resolver.task_id == raise_app_error_on_worker):
                raise errors_impl.ResourceExhaustedError(
                    node_def=None, op=None, message='Running out of resources')

            model.v.assign_add(constant_op.constant(1.))

        strategy.run(train_step)

        if current_step == STEPS_PER_EPOCH - 1:
            logging.info('epoch %d finished', current_epoch)

    logging.info('Start training at %d',
                 preemption_handler.total_run_calls)

    # If the training process has been restarted, verify that the expected
    # number of checkpoints have been written.
    # we also want to check training_finished, because there's a corner case
    # where the signal is sent quite late and training finishes before the
    # grace period ends.
    if training_restarted and training_restarted.is_set(
    ) and not training_finished.is_set():
        logging.info('training restarted')
        match_group = [
            re.search(r'.*ckpt-(\d+).index', a_file)
            for a_file in gfile.ListDirectory(checkpoint_dir)
        ]
        checkpoint_index = [
            a_match.group(1) for a_match in match_group if a_match
        ]
        if getattr(termination_config, 'grace_period', 0):
            # Two checkpoints were saved for the extended grace period.
            self.assertEqual(int(checkpoint_index[0]), 2)
        else:
            self.assertEqual(int(checkpoint_index[0]), 1)

    for epoch in range(
        preemption_handler.total_run_calls // STEPS_PER_EPOCH,
        EPOCHS_TO_RUN):

        for step in range(
            preemption_handler.total_run_calls % STEPS_PER_EPOCH,
            STEPS_PER_EPOCH):
            if api_wrapping_train:
                preemption_handler.run(distributed_train_step, epoch, step)
            else:
                preemption_handler._save_checkpoint_if_preempted()
                distributed_train_step(epoch, step)
        # Add some randomness to when preemption actually happens. We should
        # trigger it for sure if the training is coming to an end and it hasn't
        # been triggered yet.
        if epoch >= EPOCHS_TO_RUN - 2:
            trigger_it = True
        else:
            trigger_it = False

        self._maybe_trigger_a_preemption(training_started_event, trigger_it)

    training_finished.set()

    logging.info('Training finished.')

    self.assertEqual(
        model.v.numpy(),
        strategy.num_replicas_in_sync * EPOCHS_TO_RUN * STEPS_PER_EPOCH)
