# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
fn = lambda x: x + 1
with self.assertRaisesRegex(ValueError, "Function .* was not registered"):
    dispatch.unregister_dispatch_for(fn)
