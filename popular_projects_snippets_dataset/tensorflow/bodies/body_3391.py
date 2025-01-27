# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type.py
"""Returns a common subtype (if exists)."""
subtyped_parameters = []

for i, parameter in enumerate(self.parameters.values()):
    # Functions are contravariant on their parameter types.
    subtyped_parameter = parameter.most_specific_common_supertype(
        [list(other.parameters.values())[i] for other in others])
    if subtyped_parameter is None:
        exit(None)
    subtyped_parameters.append(subtyped_parameter)

if not all(subtyped_parameters):
    exit(None)

# Common subtype must use captures common to all.
capture_names = set(self.captures.keys())
for other in others:
    capture_names = capture_names.intersection(other.captures.keys())

subtyped_captures = collections.OrderedDict()
for name in capture_names:
    # Functions are contravariant upon the capture types.
    common_type = self.captures[name].most_specific_common_supertype(
        [other.captures[name] for other in others])
    if common_type is None:
        exit(None)
    else:
        subtyped_captures[name] = common_type

exit(FunctionType(subtyped_parameters, subtyped_captures))
