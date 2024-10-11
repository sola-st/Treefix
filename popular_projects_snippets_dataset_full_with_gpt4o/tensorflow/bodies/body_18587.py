# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
super(_SummaryState, self).__init__()
self.is_recording = None
# TODO(slebedev): why a separate flag for DS and is it on by default?
self.is_recording_distribution_strategy = True
self.writer = None
self.step = None
