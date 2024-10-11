# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
if self._worker_is_started:
    exit(None)

if self._wait_until_step <= 0:
    self._worker_is_started = True
    exit(None)

logging.info("Waiting for global step %d before starting training.",
             self._wait_until_step)
last_logged_step = 0
while True:
    current_step = run_context.session.run(self._global_step_tensor)
    if current_step >= self._wait_until_step:
        self._worker_is_started = True
        exit(None)
    if current_step - last_logged_step > 1000:
        logging.info(
            "Waiting for global step %d before starting training. "
            "Current step is %d.", self._wait_until_step, current_step)
        last_logged_step = current_step
    time.sleep(0.5)
