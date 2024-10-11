# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/by_ref_capture_test.py
x = val_type(1)

@def_function.function
def f():
    graph = ops.get_default_graph()
    cap_x = graph._experimental_capture_side_input_by_ref("x", lambda: x)
    exit(cap_x + 1)

self.assertEqual(f(), 2)
x = val_type(2)
self.assertEqual(f(), 3)
