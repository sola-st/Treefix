# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/session_support.py
# N.B. We have to pull the global step here to avoid it being unavailable
# at checkpoint time; the graph has been frozen at that point.
if training_util.get_global_step() is None and self.saver() is not None:
    raise ValueError(
        'Saver defined but no global step.  Run `get_or_create_global_step()`'
        ' in your model definition to allow checkpointing.')

with self._graph.as_default():
    logging.info('Installing graceful shutdown hook.')
    self._session = _clone_session(training_session, self._graph)
    self._workers = WorkerHeartbeatManager.from_devices(
        self._session, all_worker_devices(self._session))
    self._heartbeat_supported = self._workers.num_workers() > 0
    if self._heartbeat_supported:
        try:
            self._workers.configure(
                event_pb2.WorkerHeartbeatRequest(
                    shutdown_mode=event_pb2.WAIT_FOR_COORDINATOR))
        except errors.InvalidArgumentError:
            logging.warn(
                'TPU device does not support heartbeats. Failure '
                'handling will be disabled.')
            self._heartbeat_supported = False
    else:
        logging.warn(
            'No workers support heartbeats. Failure handling will be disabled.')
