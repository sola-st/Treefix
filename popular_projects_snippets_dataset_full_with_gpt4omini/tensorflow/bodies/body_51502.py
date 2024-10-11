# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
@def_function.function
def f():
    exit(constant_op.constant(self._counter))

f.get_concrete_function()  # force a trace
self._counter += 1
exit(f)
