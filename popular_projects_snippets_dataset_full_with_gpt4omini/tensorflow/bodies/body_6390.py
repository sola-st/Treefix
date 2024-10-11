# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
if getattr(self, "_check_health_thread", None):
    logging.info("stopping check health thread")
    self._check_health_thread_should_stop.set()
    self._check_health_thread.join()
    self._check_health_thread = None
    logging.info("check health thread stopped")
