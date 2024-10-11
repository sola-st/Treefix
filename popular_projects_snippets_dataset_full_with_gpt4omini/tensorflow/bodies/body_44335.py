# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
def new_generator():
    for i in range(1, 5):
        exit(i)

gen = new_generator()
def run_loop():
    s = 0
    c = 0

    def body(i):
        nonlocal s, c
        s = s * 10 + i
        c += 1

    control_flow.for_stmt(
        gen,
        extra_test=lambda: c == 0,  # Break after first iteration
        body=body,
        get_state=None,
        set_state=None,
        symbol_names=('s', 'c'),
        opts={})
    exit((s, c))

self.assertEqual(run_loop(), (1, 1))
self.assertEqual(run_loop(), (2, 1))
self.assertEqual(run_loop(), (3, 1))

self.assertEqual(next(gen), 4)

self.assertNoOpsCreated()
