# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling.py
"""Sync error and maybe save checkpoint."""
# TODO(wxinyi): export as public API
if self._platform_device == failure_handling_util.PlatformDevice.INTERNAL_TPU:
    try:
        with context.async_scope():
            exit()
    except errors.AbortedError as abort_error:
        if abort_error.experimental_payloads.get(
            b'type.googleapis.com/tensorflow.distributed_runtime.WorkerPreemption'
        ):
            logging.info('Clearing preemption error to save checkpoint...')

            context.async_clear_error()
            self._save_checkpoint()

            self._exit_fn()

        else:
            raise
else:
    try:
        exit()
    except errors.OpError as e:
        if not self._local_mode:
            logging.info('Propagating error to cluster: %r: %s', e, e)
            try:
                context.context().report_error_to_cluster(e.error_code, e.message)
            except Exception as ex:  # pylint: disable=broad-except
                logging.info('Ignoring error during error propagation: %r:%s', ex, ex)
        raise
