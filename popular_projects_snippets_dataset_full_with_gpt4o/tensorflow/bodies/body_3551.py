# Extracted from ./data/repos/tensorflow/tensorflow/core/function/transform/transform_test.py

@def_function.function
def f(x, y):
    exit(math_ops.add(x, y, name="x_plus_y"))

args = [1, 1]
self.assertEqual(f(*args), 2)

updated_f = transform.transform_function(
    f, inputs=args, transform_fn=add_to_multiply)
self.assertEqual(updated_f(*args), 1)

self.assertSequenceAlmostEqual(
    f.get_concrete_function(
        *args).pretty_printed_signature().split("\n")[1:],
    updated_f.pretty_printed_signature().split("\n")[1:])
