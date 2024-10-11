# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py

def thread_fn(i, graph, run_event, pause_event):
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
            pause_event.set()
            run_event.wait()

graph = ops.get_default_graph()
run_events = [threading.Event() for _ in range(2)]
pause_events = [threading.Event() for _ in range(2)]
threads = [
    threading.Thread(
        target=thread_fn, args=(i, graph, run_events[i], pause_events[i]))
    for i in range(2)
]

# Start first thread.
threads[0].start()
pause_events[0].wait()
# Start next thread once the first thread has paused.
threads[1].start()
pause_events[1].wait()
# Resume both threads.
run_events[0].set()
run_events[1].set()
threads[0].join()
threads[1].join()
