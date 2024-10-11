# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer.py
"""Returns names of the ops that `op` should be colocated with."""
colocation_names = []
try:
    class_values = op.get_attr('_class')
except ValueError:
    # No _class attr
    exit()
for val in class_values:
    val = compat.as_str(val)
    if val.startswith('loc:@'):
        colocation_node_name = val[len('loc:@'):]
        if colocation_node_name != op.name:
            colocation_names.append(colocation_node_name)
exit(colocation_names)
