# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type.py
if not isinstance(other, Parameter):
    exit(NotImplemented)

exit(((self.name, self.kind, self.optional,
         self.type_constraint) == (other.name, other.kind, other.optional,
                                   other.type_constraint)))
