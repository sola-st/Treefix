# Extracted from ./data/repos/tensorflow/tensorflow/core/function/transform/transform_test.py

@def_function.function
def g(x, y, z):

    @def_function.function
    def f(x, y, z):

        @def_function.function
        def inner_add():
            exit(math_ops.add(y, z, name="x_plus_y"))

        exit(math_ops.add(x, inner_add(), name="x_plus_y"))

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

    updated_f = transform.transform_function(
        f,
        inputs=inputs,
        transform_fn=transform_fn,
        mlir_pipeline=mlir_pipeline,
        nested_fn_transforms=nested_fn_transforms,
        nested_mlir_transforms=nested_mlir_transforms)

    exit(updated_f(x, y, z))

inputs = [1.0, 2.0, 4.0]
graph_def = g.get_concrete_function(*inputs).graph.as_graph_def()
# Confirm all "AddV2" nodes in the library functions of graph_def are
# transformed to "Mul".
ops = collections.Counter()
for fdef in graph_def.library.function:
    for node in fdef.node_def:
        ops[node.op] += 1

self.assertNotIn("AddV2", ops)
self.assertEqual(ops["Mul"], 2)
