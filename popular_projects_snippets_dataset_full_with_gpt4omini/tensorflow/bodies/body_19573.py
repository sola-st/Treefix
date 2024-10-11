# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/session_support.py
# Don't fetch logs or adjust timing: just ping the watchdog.
#
# If we hit an exception, reset our session as it is likely broken.
while self._running:
    try:
        self._worker_manager.ping(request=None)
        time.sleep(self.ping_interval)
    except errors.OpError as e:
        # Catch any TF errors that occur so we don't stop sending heartbeats
        logging.debug('Caught error while sending heartbeat: %s', e)
        self._reset_manager()
