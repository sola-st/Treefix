# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
if np.isnan(run_values.results):
    failure_message = "Model diverged with loss = NaN."
    if self._fail_on_nan_loss:
        logging.error(failure_message)
        raise NanLossDuringTrainingError
    else:
        logging.warning(failure_message)
        # We don't raise an error but we request stop without an exception.
        run_context.request_stop()
