# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/reference_test_base.py
compiled_data = self.run_native(self.convert(f), *args)
native_data = self.run_native(f, *args)
self.assertResultsMatch(f, args, native_data, compiled_data)
