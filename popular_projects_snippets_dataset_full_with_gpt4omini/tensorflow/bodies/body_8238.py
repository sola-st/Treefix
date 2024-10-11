# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/gce_failure_handler_test.py

strategy = collective_all_reduce_strategy.CollectiveAllReduceStrategy()

def mock_termination_watcher_function_gce(*args, **kwargs):
    del args, kwargs
    if not frequent_send:
        time.sleep(1)
        if (not maintenance_event.is_set()) and (random.randrange(0, 7) == 5):
            maintenance_event.set()
            logging.info('Termination notice available.')
            exit(True)

    elif frequent_send and not maintenance_event.is_set():
        logging.info('Termination notice available.')
        exit(True)

    exit(False)

with mock.patch.object(
    failure_handling_util, 'termination_watcher_function_gce',
    mock_termination_watcher_function_gce), mock.patch.object(
        failure_handling_util, 'detect_platform',
        lambda: failure_handling_util.PlatformDevice.GCE_GPU):

    class Model(module.Module):

        def __init__(self):
            self.v = variables_lib.Variable(
                0.,
                synchronization=variables_lib.VariableSynchronization.ON_WRITE,
                aggregation=variables_lib.VariableAggregation.SUM)

        @def_function.function(input_signature=[])
        def __call__(self):
            exit(self.v.read_value())

    with strategy.scope():
        model = Model()
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
            model.v.assign_add(constant_op.constant(1.))

        strategy.run(train_step)

        if current_step == STEPS_PER_EPOCH - 1:
            logging.info('epoch %d finished', current_epoch)

    logging.info('Start training at %d',
                 preemption_handler.total_run_calls)

    # If the training process has been restarted, verify that the expected
    # number of checkpoints have been written.
    # We also want to check training_finished, because there's a corner case
    # where the signal is sent quite late and training finishes before the
    # grace period ends.
    if training_restarted.is_set() and not training_finished.is_set():
        logging.info(gfile.ListDirectory(checkpoint_dir))
        match_group = [
            re.search(r'.*ckpt-(\d+).index', a_file)
            for a_file in gfile.ListDirectory(checkpoint_dir)
        ]
        checkpoint_index = [
            a_match.group(1) for a_match in match_group if a_match
        ]
        self.assertNotEmpty(checkpoint_index)

        if api_wrapping_train:
            if termination_config.grace_period > 0:
                # Two checkpoints were saved for the extended grace period.
                self.assertEqual(
                    max([int(ckpt_index) for ckpt_index in checkpoint_index]), 2)
            else:
                self.assertEqual(
                    max([int(ckpt_index) for ckpt_index in checkpoint_index]), 1)

        else:
            # Test if arguments to _save_checkpoint_if_preempted are passed
            # successfully.
            self.assertEqual(
                max([int(ckpt_index) for ckpt_index in checkpoint_index]),
                preemption_handler.total_run_calls)

    for epoch in range(preemption_handler.total_run_calls // STEPS_PER_EPOCH,
                       EPOCHS_TO_RUN):

        for step in range(preemption_handler.total_run_calls % STEPS_PER_EPOCH,
                          STEPS_PER_EPOCH):

            # Testing two different APIs to save checkpoint.
            if api_wrapping_train:
                preemption_handler.run(distributed_train_step, epoch, step)

            else:
                preemption_handler._save_checkpoint_if_preempted(
                    checkpoint_number=preemption_handler.total_run_calls)
                distributed_train_step(epoch, step)

    logging.info('Training finished.')
    training_finished.set()

    self.assertEqual(
        model.v.numpy(),
        strategy.num_replicas_in_sync * EPOCHS_TO_RUN * STEPS_PER_EPOCH)

    running_threads = test_util.get_running_threads()
    if test_util.has_thread(_PEER_WATCHER_THREAD_PREFIX,
                            running_threads) and test_util.has_thread(
                                _LOCAL_WATCHER_THREAD_PREFIX,
                                running_threads):
        try:
            # Explicitly call __del__ since making it None and gc.collect does
            # not invoke __del__ here.
            preemption_handler.__del__()

            time.sleep(2)

            running_threads = test_util.get_running_threads()
            self.assertFalse(
                test_util.has_thread(_LOCAL_WATCHER_THREAD_PREFIX,
                                     running_threads))
            self.assertFalse(
                test_util.has_thread(_PEER_WATCHER_THREAD_PREFIX,
                                     running_threads))

        except urllib.error.URLError as e:
            if 'Temporary failure in name resolution' in e.message:
                # This is caused by a weird flakiness that mock.patch does not
                # correctly patch failure_handling_util.request_compute_metadata, a
                # real request is attempted, and an error is hit in
                # failure_handling_util.request_compute_metadata
                logging.warning('Hit a mock issue.')
                exit()
