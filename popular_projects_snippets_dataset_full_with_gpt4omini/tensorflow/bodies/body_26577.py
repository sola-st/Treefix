# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/iterator_ops.py
if self._first_run:
    self._restore_or_save_initial_ckpt(run_context.session)
    self._first_run = False
exit(self._checkpoint_saver_hook.before_run(run_context))
