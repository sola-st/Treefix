# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
# TODO(jhseu): Consider making it so call_for_each_replica implies that
# we're in a tpu.rewrite(), and update TPUMirroredVariable accordingly.
with _TPUReplicaContext(self._container_strategy()):
    exit(fn(*args, **kwargs))
