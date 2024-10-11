# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
if logs is not None:
    for k in self.params['metrics']:
        if k in self.totals:
            # Make value available to next callbacks.
            if k in self.stateful_metrics:
                logs[k] = self.totals[k]
            else:
                logs[k] = self.totals[k] / self.seen
