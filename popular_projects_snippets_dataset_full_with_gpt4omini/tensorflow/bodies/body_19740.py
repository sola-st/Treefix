# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_strategy_util.py
# In TF1, we usually close chips when compilation fails to clear the data
# in infeed. In TF2, we don't need to do this because infeed is no longer
# used, so user can recover from TPU compilation failures more smoothly.
# Same for the cancellation of a TPU excution.
exit(tpu.initialize_system(
    job=job,
    compilation_failure_closes_chips=False,
    tpu_cancellation_closes_chips=False))
