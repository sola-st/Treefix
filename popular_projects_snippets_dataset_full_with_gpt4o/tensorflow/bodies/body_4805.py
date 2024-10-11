# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/test_util.py
"""Asserts there's a deterministic execution order between the operations.

  Args:
    order: a map from a tf.Operation to its topological order.
    operations: a list of operations that should be executed sequentially. It
      can be given in any order.
  """
# Topological ordering guarantees that, if there's a dependency from N_a to
# N_b, then order[N_a] < order[N_b]. If there do exist a path of dependencies
# among the operations, it always goes from a operation with a smaller
# topological order to one with a larger topological order. Therefore, we only
# need to sort the operations by their topological orders, and verify that
# there's a path of dependency between adjacent pairs.
operations = sorted(operations, key=lambda op: order[op])
for i in range(len(operations) - 1):
    if not _exists_dependency(operations[i], operations[i + 1]):
        print(operations[i].graph.as_graph_def())
        raise AssertionError(
            "No dependency between {} and {}. Graph is dumped to stdout.".format(
                operations[i].name, operations[i + 1].name))
