# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/step_fn.py
super(StandardInputStep, self).__init__(distribution)
self._iterator = distribution.make_input_fn_iterator(lambda _: dataset_fn())
