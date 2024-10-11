# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/tf_doctest_lib.py
super(TfDoctestOutputChecker, self).__init__(*args, **kwargs)
self.extract_floats = _FloatExtractor()
self.text_good = None
self.float_size_good = None
