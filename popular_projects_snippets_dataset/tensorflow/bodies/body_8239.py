# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/gce_failure_handler_test.py
if _is_oss():
    rpc_layer = 'grpc'
else:
    rpc_layer = 'grpc+loas'
checkpoint_dir = os.path.join(self.get_temp_dir(), 'fh_ckpt/')

if mwms_mode == 'multi_worker':
    has_chief = False
    cluster_spec = multi_worker_test_base.create_cluster_spec(
        has_chief=has_chief,
        num_workers=CLUSTER_SIZE)
    maintenance_event = multi_process_runner.manager().Event()
    training_finished = multi_process_runner.manager().Event()
    training_restarted = multi_process_runner.manager().Event()

    mpr = multi_process_runner.MultiProcessRunner(
        self.worker_fn,
        cluster_spec,
        args=(checkpoint_dir, cluster_spec, input_arg, maintenance_event,
              training_finished, False, training_restarted),
        rpc_layer=rpc_layer,
        return_output=True,
        dependence_on_chief=has_chief)

    logging.info('Cluster starting.')
    mpr.start()

    raise_if_not_all_exit(0, mpr)

    if not training_finished.is_set():
        logging.info('restarting workers')
        training_restarted.set()
        for worker_id in range(CLUSTER_SIZE):
            mpr.start_single_process('worker', worker_id, cluster_spec)
        logging.info('workers restarted')

    mpr.join(timeout=250)
    self.assertTrue(training_finished.is_set())

else:
    maintenance_event = threading.Event()
    training_finished = threading.Event()
    training_restarted = threading.Event()

    cluster_spec = server_lib.ClusterSpec({})
    caught_exit = False
    try:
        self.worker_fn(checkpoint_dir, cluster_spec, input_arg,
                       maintenance_event, training_finished, False,
                       training_restarted)
    except SystemExit as exit_error:
        caught_exit = True
        # We cannot use assertRaise instead, since termination is not always
        # triggered.
        self.assertEqual(exit_error.code, 143)  # pylint:disable=g-assert-in-except

    if maintenance_event.is_set() and not training_finished.is_set():
        self.assertTrue(caught_exit)

        logging.info('restarting workers')
        training_restarted.set()
        self.worker_fn(checkpoint_dir, cluster_spec, input_arg,
                       maintenance_event, training_finished, False,
                       training_restarted)

    self.assertTrue(training_finished.is_set())
