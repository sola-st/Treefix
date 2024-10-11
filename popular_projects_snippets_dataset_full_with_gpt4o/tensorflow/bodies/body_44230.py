# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/reference_test_base.py
if self.all_inputs_tensors:
    args = self._as_tensors(args)
compiled_data = self.run_native(self.function(f, xla=xla), *args)
if not self.allow_exceptions:
    _, _, compiled_err = compiled_data
    if compiled_err is not None:
        self.fail(str(compiled_err))
native_data = self.run_native(f, *args)
self.assertResultsMatch(f, args, native_data, compiled_data)
