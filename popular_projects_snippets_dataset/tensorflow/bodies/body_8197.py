# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/preemption_watcher.py
# TODO(b/254321514): Integrate with GPU and cloud enviornmenmt.
self._preemption_message = None
platform = detect_platform()
if platform != PlatformDevice.INTERNAL_TPU:
    logging.warning("Preemption watcher does not support environment: %s",
                    platform)
else:
    threading.Thread(target=self._watch_preemption_key, daemon=True).start()
