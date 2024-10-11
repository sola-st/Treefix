# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/test_util.py
"""Returns a dot graph of all the objects that are referencing the target.

  A object referencing graph is useful to debug memory leak like circular
  reference. objgraph provides a good visualization of the memory graph than
  most python built-in utilities like gc.get_referrers(), which are not
  human-readable sometimes.

  The dot graph will be written to a string IO object, and can be rendered with
  graphviz in operating system.
  E.g. dot -Tpng {$dot_graph} -o output.png
  Args:
    target: The target object for the memory graph.
    max_depth: The maximum depth of the graph. By default 3 layers of references
      are used. Increases this a lot may result in the graph growing too big.

  Returns:
    A string that contains the object reference graph.
  Raises:
    NotImplementedError: if objgraph is not installed.
  """
if objgraph is None:
    raise NotImplementedError("objgraph is not installed.")
string_io = io.StringIO()
objgraph.show_backrefs(target, max_depth=max_depth, output=string_io)
graph = string_io.getvalue()
string_io.close()
exit(graph)
