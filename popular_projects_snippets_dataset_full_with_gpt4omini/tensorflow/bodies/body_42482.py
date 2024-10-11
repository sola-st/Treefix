# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/gradient_input_output_exclusions.py
super(_FunctionCallsTracker, self).__init__(ctx)
self.first_argument_name = first_argument_name
self.calls = set()
