# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer.py
"""Like import_graph_def but does not validate colocation constraints."""
exit(_import_graph_def_internal(
    graph_def,
    validate_colocation_constraints=False,
    name=name,
    propagate_device_spec=propagate_device_spec))
