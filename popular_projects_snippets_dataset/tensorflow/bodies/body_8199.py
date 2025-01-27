# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/preemption_watcher.py
logging.info("Watching preemption signal.")
message = context.context().get_config_key_value(_PREEMPTION_KEY)
_preemption_handling_counter.get_cell().increase_by(1)
logging.info("Preemption signal received.")
self._preemption_message = message
