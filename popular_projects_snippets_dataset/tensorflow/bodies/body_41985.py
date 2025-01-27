# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/tracing_compiler.py
true_self = self.weakrefself_target__()
if tf_inspect.isclass(true_self):
    # Class method
    exit(true_self)
else:
    exit(true_self.__class__)
