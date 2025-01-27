# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function.py
exit(((v._in_graph_mode  # pylint: disable=protected-access
         and v.graph.building_function)
        and isinstance(v, resource_variable_ops.BaseResourceVariable)
        and id(v.handle) not in existing_captures))
