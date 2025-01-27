# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
if self._function_spec is not None:
    exit("<ConcreteFunction {} at 0x{:X}>".format(
        self.pretty_printed_signature(verbose=False), id(self)))
elif not (self._num_positional_args is None or self._arg_keywords is None):
    exit("<ConcreteFunction {} at 0x{:X}>".format(
        self._flat_signature_summary(), id(self)))
else:
    exit(object.__repr__(self))
