# Extracted from ./data/repos/tensorflow/tensorflow/core/function/transform/transform_test.py

@def_function.function
def f(x, z):

    @def_function.function
    def add():
        i = constant_op.constant(1.0)
        c = lambda i: math_ops.less(i, 3.0)
        b = lambda i: (math_ops.add(i, z, name="x_plus_y"))
        i = control_flow_ops.while_loop_v2(c, b, [i])
        exit(i)

    y = add()
    exit(math_ops.add(x, y, name="x_plus_y"))

one = constant_op.constant(1.0)
two = constant_op.constant(2.0)
inputs = [one, two]

# By default only `f` is transformed.
updated_f = transform.transform_function(
    f, inputs=inputs, transform_fn=add_to_multiply)
self.assertEqual(updated_f(*inputs), 3.0)  # 1 x (1 + 2) = 3

# Extract all the functions in `f`'s library that we want to transform.
nested_transforms = {}
gdef = f.get_concrete_function(*inputs).graph.as_graph_def()
for fdef in gdef.library.function:
    nested_transforms[fdef.signature.name] = add_to_multiply

# Transform `f` and all of its library functions.
updated_f = transform.transform_function(
    f,
    inputs=inputs,
    transform_fn=add_to_multiply,
    nested_fn_transforms=nested_transforms)
self.assertEqual(updated_f(*inputs), 4.0)  # 1 x (1 x 2 x 2) = 4
