# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py

def thread_fn(i, graph):
    with graph.as_default():
        with variable_scope.variable_scope("foo"):
            if i == 0:
                v = variable_scope.get_variable("v", [])
                self.assertEqual("foo/v:0", v.name)
            else:
                # Any thread after the first one should fail to create variable
                # with the same name.
                with self.assertRaises(ValueError):
                    variable_scope.get_variable("v", [])

graph = ops.get_default_graph()
threads = [
    threading.Thread(target=thread_fn, args=(
        i,
        graph,
    )) for i in range(2)
]

threads[0].start()
# Allow thread 0 to finish before starting thread 1.
threads[0].join()
threads[1].start()
threads[1].join()
