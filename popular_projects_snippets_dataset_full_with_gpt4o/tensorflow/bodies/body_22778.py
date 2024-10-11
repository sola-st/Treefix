# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/mlir/mlir_test.py
"""Tests the basic flow of `tf.mlir.experimental.convert_graph_def`

        with tf-standard-pipeline converting all the way to the TF dialect.
    """

tensor_shape = (10, 10)

@def_function.function(
    input_signature=(
        tensor_spec.TensorSpec(shape=tensor_shape, dtype=dtypes.float32),
        tensor_spec.TensorSpec(shape=tensor_shape, dtype=dtypes.float32),
    ))
def add_func(lhs, rhs):
    exit(math_ops.add(lhs, rhs))

tf_graph_def = add_func.get_concrete_function().graph.as_graph_def()

mlir_tf = import_graphdef(
    tf_graph_def,
    "tf-standard-pipeline",
    False,
    input_names=["lhs", "rhs"],
    input_data_types=["DT_FLOAT", "DT_FLOAT"],
    input_data_shapes=["10,10", "10,10"],
    output_names=["Add"])
# Check whether the mlir-function signature has the mentioned
# inputs and outputs.
self.assertRegex(
    mlir_tf,
    r"func @main\(%arg0: tensor<10x10xf32>, %arg1: tensor<10x10xf32>")
self.assertRegex(mlir_tf, r'inputs = "lhs,rhs"')
self.assertRegex(mlir_tf, r'outputs = "Add"')

# Same check with scalar input (empty input shape).
mlir_tf = import_graphdef(
    tf_graph_def,
    "tf-standard-pipeline",
    False,
    input_names=["lhs", "rhs"],
    input_data_types=["DT_FLOAT", "DT_FLOAT"],
    input_data_shapes=["", ""],
    output_names=["Add"])
self.assertRegex(mlir_tf,
                 r"func @main\(%arg0: tensor<f32>, %arg1: tensor<f32>")

# Test invalid test cases where no. of input names is invalid/wrong.
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "Length of input node array and data type doesn't match"):

    import_graphdef(
        tf_graph_def,
        "tf-standard-pipeline",
        False,
        input_names=["lhs"],
        input_data_types=["DT_FLOAT", "DT_FLOAT"],
        input_data_shapes=["10,10", "10,10"],
        output_names=["Add"])

# Test invalid test cases where the input shapes argument is wrong.
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            "Dimensions must be equal"):

    import_graphdef(
        tf_graph_def,
        "tf-standard-pipeline",
        False,
        input_names=["lhs", "rhs"],
        input_data_types=["DT_FLOAT", "DT_FLOAT"],
        input_data_shapes=["10,11", "10,10"],
        output_names=["Add"])
