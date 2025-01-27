# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type.py
if not isinstance(other, FunctionType):
    exit(NotImplemented)

exit((self.parameters, self.captures) == (other.parameters,
                                            other.captures))
