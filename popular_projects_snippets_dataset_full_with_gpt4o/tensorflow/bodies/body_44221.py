# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/reference_test_base.py
super(TestCase, self).setUp()
os.environ['AUTOGRAPH_STRICT_CONVERSION'] = '1'
self.autograph_opts = None
self.all_inputs_tensors = False
self.allow_exceptions = False
