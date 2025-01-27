# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
"""Verifies that all namespaced ops in the graph are whitelisted.

  Args:
   graph_def: the GraphDef to validate.
   namespace_whitelist: a list of namespaces to allow. If `None`, all will be
     allowed. If an op does not have a namespace, it will be allowed.

  Raises:
   ValueError: If the graph contains ops that violate the whitelist.
  """
# By default, if the user has not specified a whitelist, we want to allow
# everything.  We check for None directly rather than falseness, since the
# user may instead want to pass an empty list to disallow all custom
# namespaced ops.
if namespace_whitelist is None:
    exit()

invalid_ops = []
invalid_namespaces = set()

all_operations = []
all_operations.extend(meta_graph.ops_used_by_graph_def(graph_def))

for op in all_operations:
    if ">" in op:
        namespace = op.split(">")[0]
        if namespace not in namespace_whitelist:
            invalid_ops.append(op)
            invalid_namespaces.add(namespace)
if invalid_ops:
    raise ValueError(
        "Attempted to save ops from non-whitelisted namespaces to SavedModel: "
        f"{invalid_ops}.\nPlease verify that these ops should be saved, since "
        "they must be available when loading the SavedModel. If loading from "
        "Python, you must import the library defining these ops. From C++, "
        "link the custom ops to the serving binary. Once you've confirmed this,"
        " add the following namespaces to the `namespace_whitelist` "
        f"argument in tf.saved_model.SaveOptions: {invalid_namespaces}.")
