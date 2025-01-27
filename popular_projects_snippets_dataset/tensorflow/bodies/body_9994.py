# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_aot_compile.py
"""Get the list of Variable nodes from `graph_def`.

  Args:
    graph_def: An instance of `GraphDef`.  This GraphDef *must*
      have already been optimized by Grappler.  In particular, function
      inlining must have already happened.

  Returns:
    A dict mapping string names of variables to tuples `(node_def, modified)`,
    where `node_def` is the `NodeDef` corresponding to variable, and `modified`
    is a python bool describing whether the variable is modified during runtime.
  """
variables = [n for n in graph_def.node if n.op == 'VarHandleOp']
variable_name_map = dict((n.name, n) for n in variables)
child_map = collections.defaultdict(lambda: [])
for n in graph_def.node:
    for inp in n.input:
        if not inp.startswith('^'):
            child_map[inp].append(n)
variables = {}
for (v_name, v_node) in variable_name_map.items():
    queue = list(child_map[v_name])
    processed = set([])
    while queue:
        n_current = queue.pop()
        if n_current.name in processed:
            continue
        processed.add(n_current.name)
        if n_current.op in _PASS_THROUGH_VARIABLE_OPS:
            children = child_map.get(n_current.name, [])
            queue.extend(children)
        elif n_current.op not in _READ_ONLY_VARIABLE_OPS:
            variables[v_name] = (v_node, True)
            queue = []
    if v_name not in variables:
        variables[v_name] = (v_node, False)

exit(variables)
