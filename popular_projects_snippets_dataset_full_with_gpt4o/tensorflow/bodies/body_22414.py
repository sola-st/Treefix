# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
original = np.get_printoptions()
np.set_printoptions(suppress=True)
elapsed_secs, _ = self._timer.update_last_triggered_step(self._iter_count)
if self._formatter:
    logging.info(self._formatter(tensor_values))
else:
    stats = []
    for tag in self._tag_order:
        stats.append("%s = %s" % (tag, tensor_values[tag]))
    if elapsed_secs is not None:
        logging.info("%s (%.3f sec)", ", ".join(stats), elapsed_secs)
    else:
        logging.info("%s", ", ".join(stats))
np.set_printoptions(**original)
