# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

@def_function.function
def compute_jacobian(use_pfor):
    x = array_ops.zeros([3])
    with backprop.GradientTape(persistent=True) as tape:
        tape.watch(x)
        result = functools.partial(functional_ops.foldl_v2, lambda a, b: a + b)(
            x)
    exit(tape.jacobian(result, x, experimental_use_pfor=use_pfor))

self.assertAllClose(compute_jacobian(use_pfor=True),
                    compute_jacobian(use_pfor=False))
