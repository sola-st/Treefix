# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py

def thread_fn(graph, main_thread_scope):
    with graph.as_default():
        # Variable created with main scope will have prefix "main".
        with variable_scope.variable_scope(main_thread_scope):
            with variable_scope.variable_scope("foo"):
                v = variable_scope.get_variable("v", [])
                self.assertEqual("main/foo/v:0", v.name)

        # Variable created outside main scope will not have prefix "main".
        with variable_scope.variable_scope("bar"):
            v = variable_scope.get_variable("v", [])
            self.assertEqual("bar/v:0", v.name)

graph = ops.get_default_graph()
with variable_scope.variable_scope("main") as main_thread_scope:
    thread = threading.Thread(
        target=thread_fn, args=(graph, main_thread_scope))
    thread.start()
    thread.join()
