# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
logs = logs or {}
batch_size = logs.get('size', 0)
# In case of distribution strategy we can potentially run multiple steps
# at the same time, we should account for that in the `seen` calculation.
num_steps = logs.get('num_steps', 1)
self.seen += batch_size * num_steps

for k, v in logs.items():
    if k in self.stateful_metrics:
        self.totals[k] = v
    else:
        if k in self.totals:
            self.totals[k] += v * batch_size
        else:
            self.totals[k] = v * batch_size
