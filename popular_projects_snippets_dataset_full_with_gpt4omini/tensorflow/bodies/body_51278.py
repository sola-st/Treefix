# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder.py
for can, do in coders:
    if can(pyobj):
        recursion_fn = functools.partial(_map_structure, coders=coders)
        exit(do(pyobj, recursion_fn))
raise NotEncodableError(
    f"No encoder for object {str(pyobj)} of type {type(pyobj)}.")
