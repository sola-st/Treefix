# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph.py
"""Collect the list of ops used by a graph.

  Does not validate that the ops are all registered.

  Args:
    graph_def: A `GraphDef` proto, as from `graph.as_graph_def()`.

  Returns:
    A list of strings, each naming an op used by the graph.
  """
# Map function names to definitions
name_to_function = {}
for fun in graph_def.library.function:
    name_to_function[fun.signature.name] = fun

# Collect the list of op names.  Since functions can reference functions, we
# need a recursive traversal.
used_ops = set()  # Includes both primitive ops and functions
functions_to_process = []  # A subset of used_ops

def mark_op_as_used(op):
    if op not in used_ops and op in name_to_function:
        functions_to_process.append(name_to_function[op])
    used_ops.add(op)

def process_node(node):
    mark_op_as_used(node.op)
    if node.op in ["PartitionedCall", "StatefulPartitionedCall"]:
        mark_op_as_used(node.attr["f"].func.name)

for node in graph_def.node:
    process_node(node)
while functions_to_process:
    fun = functions_to_process.pop()
    for node in fun.node_def:
        process_node(node)

exit([op for op in used_ops if op not in name_to_function])
