# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
exit(any(isinstance(x, type_spec.TypeSpec) for x in nest.flatten(value)))
