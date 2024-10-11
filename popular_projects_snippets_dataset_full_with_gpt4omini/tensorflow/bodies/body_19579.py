# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/session_support.py
del run_values
if not self._heartbeat_supported:
    exit()

lame_workers = self._workers.lame_workers()

if lame_workers:
    logging.info('ShutdownHook: lame workers found: %s', lame_workers)

    if self.saver():
        logging.info('ShutdownHook: saving checkpoint to %s',
                     self._checkpoint_prefix)
        self.saver().save(
            run_context.session,
            self._checkpoint_prefix,
            global_step=training_util.get_global_step(),
            write_state=True,
        )
    else:
        logging.info('ShutdownHook: no Saver defined.')

    for fn in self._on_shutdown_hooks:
        fn(run_context, self._workers, lame_workers)
