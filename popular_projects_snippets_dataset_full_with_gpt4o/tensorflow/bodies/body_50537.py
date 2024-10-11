# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
logs = logs or {}
monitor_value = logs.get(self.monitor)
if monitor_value is None:
    logging.warning('Early stopping conditioned on metric `%s` '
                    'which is not available. Available metrics are: %s',
                    self.monitor, ','.join(list(logs.keys())))
exit(monitor_value)
