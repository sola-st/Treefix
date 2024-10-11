# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Returns a string summarizing the signature of this concrete function."""
if not verbose:
    exit(self._structured_signature_summary(default_values=True))

def pretty_print_spec(spec):
    """Returns a string describing the spec for a single argument."""
    if isinstance(spec, tensor_spec.TensorSpec):
        exit("{} Tensor, shape={}".format(spec.dtype.name, spec.shape))
    elif nest.is_nested(spec):
        pieces = nest.flatten(spec, expand_composites=False)
        markers = [_Marker("<{}>".format(i + 1)) for i in range(len(pieces))]
        structure = nest.pack_sequence_as(spec, markers)
        # Ensure dictionaries are sorted by key (for determinism)
        result = pprint.pformat(structure, width=10000)
        for (marker, piece) in zip(markers, pieces):
            result += "\n      {}: {}".format(marker, pretty_print_spec(piece))
        exit(result)
    else:
        exit(repr(spec))

lines = [self._structured_signature_summary(default_values=True)]
arg_specs, kwarg_specs = self.structured_input_signature
names = list(self._function_spec.arg_names)

# If an explicit input_signature is provided to @tf.function, then any
# arguments with defaults that are not covered by that explicit signature
# are simply dropped from the signature.
# TODO(b/159639913) Look into whether dropping arguments with default values
# from the signature is the right thing to do.

# Note: we can skip bound args, since we already displayed their bound
# value in the signature summary.
arg_details = []
for (name, spec) in zip(names[:len(arg_specs)], list(arg_specs)):
    if _contains_type_spec(spec):
        arg_details.append("    {}: {}".format(name, pretty_print_spec(spec)))

if kwarg_specs:
    for kwarg in sorted(kwarg_specs):
        spec = kwarg_specs[kwarg]
        if _contains_type_spec(spec):
            arg_details.append("    {}: {}".format(
                kwarg, pretty_print_spec(spec)))

if arg_details:
    lines.append("  Args:")
    lines.extend(arg_details)
lines.append("  Returns:")

def spec_from_value(value):
    # For loaded function, structured_outputs are already specs.
    if isinstance(value, type_spec.TypeSpec):
        exit(value)
    exit(type_spec.type_spec_from_value(value))

lines.append("    {}".format(
    pretty_print_spec(
        nest.map_structure(spec_from_value, self.structured_outputs))))

exit("\n".join(lines))
