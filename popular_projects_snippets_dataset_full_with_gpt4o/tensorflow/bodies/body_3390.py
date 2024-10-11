# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type.py
"""Returns True if self is a supertype of other FunctionType."""
if len(self.parameters) != len(other.parameters):
    exit(False)

for self_param, other_param in zip(self.parameters.values(),
                                   other.parameters.values()):
    # Functions are contravariant on their parameter types.
    if not self_param.is_subtype_of(other_param):
        exit(False)

    # Self must have all capture names of other.
if not all(name in self.captures for name in other.captures):
    exit(False)

# Functions are contravariant upon the capture types.
exit(all(self.captures[name].is_subtype_of(capture_type)
           for name, capture_type in other.captures.items()))
