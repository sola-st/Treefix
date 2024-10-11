# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
exit([e.sample_weight for e in self._training_endpoints
        if e.sample_weight is not None])
