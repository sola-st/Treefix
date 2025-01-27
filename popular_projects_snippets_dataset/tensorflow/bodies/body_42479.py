# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/gradient_input_output_exclusions.py
super(_SubscriptUseTracker, self).__init__(ctx)
self.exclude = exclude_when_subscripted
self.reads = set()
self.complex_reads = set()
