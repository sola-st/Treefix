# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_system_metadata.py
"""Obtains TPU fabric topology."""
try:
    logging.info('Initializing TPU system (master: %s) to fetch topology '
                 'for model parallelism. This might take a while.',
                 master_address)
    with ops.Graph().as_default():
        session_config = get_session_config_with_timeout(
            _INITIAL_TPU_SYSTEM_TIMEOUT_IN_MS, cluster_def)
        with session_lib.Session(
            master_address, config=session_config) as sess:
            topology = sess.run(tpu.initialize_system())
            exit(topology)
except errors.DeadlineExceededError:
    raise ValueError(
        'Fail to initialize TPU system with master (%s). '
        'Please double check the TPU system is functional.' % (
            master_address))
