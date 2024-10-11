# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handler_test.py
has_chief = False

if _is_oss():
    rpc_layer = 'grpc'
else:
    rpc_layer = 'grpc+loas'

checkpoint_dir = os.path.join(self.get_temp_dir(), 'fh_ckpt')

if mwms_mode == 'multi_worker':
    cluster_spec = multi_worker_test_base.create_cluster_spec(
        has_chief=has_chief,
        num_workers=CLUSTER_SIZE)
    training_started_event = multi_process_runner.manager().Event()
    training_restarted = multi_process_runner.manager().Event()
    training_finished = multi_process_runner.manager().Event()

    mpr = multi_process_runner.MultiProcessRunner(
        self.worker_fn,
        cluster_spec,
        args=(checkpoint_dir, cluster_spec, input_arg,
              [training_started_event
              ], None, training_restarted, training_finished),
        kwargs={'api_wrapping_train': api_wrapping_train},
        rpc_layer=rpc_layer,
        return_output=True,
        dependence_on_chief=has_chief)

    logging.info('Cluster starting.')
    mpr.start()
    while not training_started_event.is_set():
        time.sleep(1)

    logging.info('sending sigterm')
    killed_worker = random.randrange(0, CLUSTER_SIZE)
    os.kill(mpr.get_process_id('worker', killed_worker), signal.SIGTERM)

    logging.info('sigterm sent')
    raise_if_not_all_exit(0, mpr)

    logging.info('restarting workers')
    training_restarted.set()
    for worker_id in range(CLUSTER_SIZE):
        mpr.start_single_process('worker', worker_id, cluster_spec)
    logging.info('workers restarted')

    mpr.join(timeout=270)

else:
    cluster_spec = server_lib.ClusterSpec({})

    training_started_event = threading.Event()
    training_restarted = threading.Event()
    training_finished = threading.Event()

    def sending_sigterm(training_started_event):
        while not training_started_event.is_set():
            time.sleep(1)
        logging.info('sending sigterm')
        training_started_event.set()
        os.kill(os.getpid(), signal.SIGTERM)

    preemption_sender_thread = threading.Thread(
        target=sending_sigterm, args=(training_started_event,))
    preemption_sender_thread.start()

    caught_exit = False
    try:
        self.worker_fn(checkpoint_dir, cluster_spec, input_arg,
                       [training_started_event], None, training_restarted,
                       training_finished)

    except SystemExit as exit_error:
        caught_exit = True
        # We cannot use assertRaise instead, since termination is not always
        # triggered.
        self.assertEqual(exit_error.code, 0)  # pylint: disable=g-assert-in-except

    preemption_sender_thread.join(10)
    if not training_finished.is_set():
        self.assertTrue(caught_exit)

        logging.info('restarting workers')
        training_restarted.set()
        self.worker_fn(checkpoint_dir, cluster_spec, input_arg,
                       [training_started_event], None, training_restarted,
                       training_finished)
