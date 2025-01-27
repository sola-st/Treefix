# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/fingerprinting_test.py
root = autotrackable.AutoTrackable()
root.f = def_function.function(lambda x: 2. * x)
exit(root)
