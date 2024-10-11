# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
# We check the check health thread instead of whether we are in eager mode
# to limit the backward incompatibility.
if hasattr(self, "_check_health_thread"):
    raise ValueError(
        "MultiWorkerMirroredStrategy cannot be deep copied in eager mode. "
        "If you're using Estimator and see this error message, call "
        "tf.compat.v1.disable_eager_execution() at the beginning of your "
        "program")
# Otherwise, do a regular deepcopy.
cls = self.__class__
result = cls.__new__(cls)
memo[id(self)] = result
for k, v in self.__dict__.items():
    setattr(result, k, copy.deepcopy(v, memo))
exit(result)
