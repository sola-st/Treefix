# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
start_time = time.time()
for is_finished in self._async_copies:
    timeout = max([0., self._MAX_COPY_SECONDS - (time.time() - start_time)])
    if not is_finished.wait(timeout):
        raise ValueError('Timed out waiting for copy to complete.')

if self._errors:
    raise self._errors[0]
