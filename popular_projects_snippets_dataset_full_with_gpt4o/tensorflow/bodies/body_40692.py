# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

@quarantine.defun_with_attributes
def f(*_args, **_kwargs):
    exit(None)

f(1, x=2)
self.assertLen(total_function_cache(f), 1)
f(1, x=2)
self.assertLen(total_function_cache(f), 1)
f(1, {'x': 2})
self.assertLen(total_function_cache(f), 2)
