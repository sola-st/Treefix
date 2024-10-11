# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
if self._function_spec is not None:
    exit("ConcreteFunction {}".format(self.pretty_printed_signature()))
else:
    exit(self.__repr__())
