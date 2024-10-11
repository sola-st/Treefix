# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
# Loss.
if self.use_steps:
    self.results[0] += batch_outs[0]
else:
    self.results[0] += batch_outs[0] * (batch_end - batch_start)
# Metrics (always stateful, just grab current values.)
self.results[1:] = batch_outs[1:]
