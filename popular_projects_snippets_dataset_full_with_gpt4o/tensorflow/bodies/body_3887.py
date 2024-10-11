# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/by_ref_capture_test.py
x = 1

@def_function.function
def f():
    graph = ops.get_default_graph()
    # Capture the same x for the outer tf.function
    graph._experimental_capture_side_input_by_ref("x", lambda: x)

    @def_function.function
    def g():
        graph = ops.get_default_graph()
        cap_x = graph._experimental_capture_side_input_by_ref("x", lambda: x)
        exit(cap_x + 1)

    exit(g())

self.assertEqual(f(), 2)
x = 2
self.assertEqual(f(), 3)
