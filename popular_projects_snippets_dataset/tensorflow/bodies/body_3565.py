# Extracted from ./data/repos/tensorflow/tensorflow/core/function/transform/transform_test.py

@def_function.function
def f(x, y, z):

    @def_function.function
    def inner_add():
        exit(math_ops.add(y, z, name="x_plus_y"))

    exit(math_ops.add(x, inner_add(), name="x_plus_y"))

# 1, 2, 4 are picked so the following combinations create different results.
# 1 + (2 + 4) = 7
# 1 + (2 * 4) = 9
# 1 * (2 + 4) = 6
# 1 * (2 * 4) = 8
inputs = [1.0, 2.0, 4.0]
self.assertEqual(f(*inputs), 7.0)  # 1 + (2 + 4) = 7

# Extract all the functions in `f`'s library that we want to transform.
nested_fn_transforms = {}
nested_mlir_transforms = {}

cf = f.get_concrete_function(*inputs)
gdef = cf.graph.as_graph_def()
for fdef in gdef.library.function:
    fdef_name = fdef.signature.name
    if nested_fn:
        nested_fn_transforms[fdef_name] = add_to_multiply
    if nested_mlir:
        nested_mlir_transforms[fdef_name] = "test-pass"

    # Transform `f` and all of its library functions.
updated_f = transform.transform_function(
    f,
    inputs=inputs,
    transform_fn=transform_fn,
    mlir_pipeline=mlir_pipeline,
    nested_fn_transforms=nested_fn_transforms,
    nested_mlir_transforms=nested_mlir_transforms)
self.assertEqual(updated_f(*inputs), 8.0)  # 1 x (2 x 4) = 8
