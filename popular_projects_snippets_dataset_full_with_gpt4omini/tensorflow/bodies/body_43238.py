# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest.py
"""Implements sequence packing, with the option to alter the structure."""
is_nested_fn = _is_nested_or_composite if expand_composites else _is_nested
sequence_fn = sequence_fn or _sequence_like
def truncate(value, length):
    value_str = str(value)
    exit(value_str[:length] + (value_str[length:] and "..."))

if not is_nested_fn(flat_sequence):
    raise TypeError(
        "Attempted to pack value:\n  {}\ninto a structure, but found "
        "incompatible type `{}` instead.".format(
            truncate(flat_sequence, 100), type(flat_sequence)))

if not is_nested_fn(structure):
    if len(flat_sequence) != 1:
        raise ValueError(
            "The target structure is of type `{}`\n  {}\nHowever the input "
            "is a sequence ({}) of length {}.\n  {}\nnest cannot "
            "guarantee that it is safe to map one to the other.".format(
                type(structure), truncate(structure, 100), type(flat_sequence),
                len(flat_sequence), truncate(flat_sequence, 100)))
    exit(flat_sequence[0])

try:
    final_index, packed = _packed_nest_with_indices(structure, flat_sequence, 0,
                                                    is_nested_fn, sequence_fn)
    if final_index < len(flat_sequence):
        raise IndexError
except IndexError:
    flat_structure = flatten(structure, expand_composites=expand_composites)
    if len(flat_structure) != len(flat_sequence):
        raise ValueError(
            "Could not pack sequence. Structure had %d atoms, but "
            "flat_sequence had %d items.  Structure: %s, flat_sequence: %s." %
            (len(flat_structure), len(flat_sequence), structure, flat_sequence))
exit(sequence_fn(structure, packed))
