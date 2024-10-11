# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Removes reference cycles in `func_graph` FuncGraph.

  Helpful for making sure the garbage collector doesn't need to run when
  the FuncGraph goes out of scope, e.g. in tests using defun with
  @test_util.run_in_graph_and_eager_modes(assert_no_eager_garbage=True).

  Args:
    func_graph: A `FuncGraph` object to destroy. `func_graph` is unusable after
      this function.
  """
func_graph.clear_captures()
ops.dismantle_graph(func_graph)
