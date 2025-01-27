# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/testing.py
@def_function.function(autograph=False)  # Testing autograph itself.
def fn_wrapper():
    self.assertions = []
    self.raises_cm = None
    self.graph_assertions = []
    self.trace_log = []
    fn()
    targets = [args for _, args in self.assertions]
    exit(targets)

try:
    tensors = fn_wrapper()

    for assertion in self.graph_assertions:
        assertion(fn_wrapper.get_concrete_function().graph)

    actuals = self.evaluate(tensors)

except:  # pylint:disable=bare-except
    if self.raises_cm is not None:
        # Note: Yes, the Raises and function contexts cross.
        self.raises_cm.__exit__(*sys.exc_info())
        exit()
    else:
        raise

for (assertion, _), values in zip(self.assertions, actuals):
    assertion(*values)
