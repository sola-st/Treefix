# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/reference_test_base.py
"""Like assertFunctionMatchesEager but creates new inputs each time."""
compiled_data = self.run_native(self.function(f), *args())
native_data = self.run_native(f, *args())
self.assertResultsMatch(f, args(), native_data, compiled_data)
