# Extracted from ./data/repos/tensorflow/tensorflow/core/function/transform/transform.py
"""Applies a transformation to a tf.function to produce a new callable.

  When `transform_fn` is specified, the underlying `FunctionDef` is modified
  according to the `transform_fn`.

  When `mlir_pipeline` is specified, the underlying `FunctionDef` is converted
  to an MLIR representation and transformed based on the rules of the
  `mlir_pipeline`.

  If both are provided, `mlir_pipeline` is applied followed by `transform_fn`.

  Optionally, `transform_fn` could be a list of transformation functions and
  `mlir_pipeline` could be a a list of MLIR transformations. The transformations
  will be applied in order of the list. For each nested `FunctionDef`, MLIR
  transformations will be applied before Python function based transformations.


  Example:
  ```python
  def edit_fn(fndef):
    for node in fndef.node_def:
      if node.name == "x_plus_y":
        node.name = "x_times_y"
        node.op = "Mul"
      for idx, inp in enumerate(node.input):
        if inp == "x_plus_y:z:0":
          node.input[idx] = "x_times_y:z:0"

  @tf.function(input_signature=[
      tf.TensorSpec((), dtype=tf.float32),
      tf.TensorSpec((), dtype=tf.float32)
  ])
  def add(x, y):
    return tf.add(x, y, name="x_plus_y")

  multiply = transform_function(add, transform_fn=edit_fn)
  assert multiply(1.0, 2.0) == 2.0
  ```

  Args:
    f: The target tf.function.
    inputs: The inputs or input_signature of the tf.function. This does not need
      to be specified if the `input_signature` was specified in the tf.function
      decorator.
    kw_inputs: The keyword inputs of the tf.function. This does not need to be
      specified if the `input_signature` was specified in the tf.function
      decorator.
    transform_fn: A single transformation function or a list of transformation
      functions to apply on the `FunctionDef`.
    mlir_pipeline: A single MLIR pass or a list of MLIR passes to transform the
      `FunctionDef`.
    nested_fn_transforms: A dict of Python function based transformations to
      apply on functions in the library of `f`. The keys are the names of the
      library functions being targeted for transformation.
    nested_mlir_transforms: A dict of MLIR pass based transformations to apply
      on functions in the library of `f`. The keys are the names of the library
      functions being targeted for transformation.

  Returns:
    The transformed function.
  """
# Early exit if no transformations need to be applied.
if transform_fn is None and mlir_pipeline is None:
    exit(f)

if transform_fn is None:
    transform_fns = []
elif isinstance(transform_fn, list):
    transform_fns = transform_fn
else:
    transform_fns = [transform_fn]

if mlir_pipeline is None:
    mlir_pipelines = []
elif isinstance(mlir_pipeline, list):
    mlir_pipelines = mlir_pipeline
else:
    mlir_pipelines = [mlir_pipeline]

nested_fn_transforms = (
    nested_fn_transforms if nested_fn_transforms is not None else {})
nested_mlir_transforms = (
    nested_mlir_transforms if nested_mlir_transforms is not None else {})

# Extract the `ConcreteFunction` from the `tf.function.`
if inputs is not None or kw_inputs is not None:
    inputs = [] if inputs is None else inputs
    kw_inputs = {} if kw_inputs is None else kw_inputs
    cf = f.get_concrete_function(*inputs, **kw_inputs)
else:
    cf = f.get_concrete_function()

# Promote all library functions to the parent scope so that any replicated
# functions can also re-use them.
graph = ops.get_default_graph()
for edf in cf.graph._functions.values():  # pylint: disable=protected-access
    edf.add_to_graph(graph, overwrite=False)

# Initialize the `runtime_client`.
eager_ctx = runtime_client.GlobalPythonEagerContext()
rt = runtime_client.Runtime(eager_ctx)

# Apply the MLIR passes if provided.
for mlir_pipeline in mlir_pipelines:
    rt.TransformFunction(cf.function_def.signature.name, mlir_pipeline)

# Get the most up-to-date FunctionDef for the tf.function. This should only
# be read after applying any specified mlir_pipelines as they directly
# transform the FunctionDef in the runtime.
fndef = rt.GetFunctionProto(cf.function_def.signature.name)

# Apply any transformations if provided.
for transform_fn in transform_fns:
    transform_fn(fndef)

# Apply a transform to any of the nested _EagerDefinedFunctions(EDF) if
# `nested_fn_transforms` or `nested_mlir_transforms` is provided.
if nested_fn_transforms or nested_mlir_transforms:
    nested_functions = cf.graph._functions  # pylint: disable=protected-access

    # Store the new transformed functions.
    transformed_nested_functions = {}

    # Store a mapping between the old nested function names and the new
    # transformed function names.
    nested_transforms_map = {}

    # Transform every nested function specified in `nested_fn_transforms` and
    # `nested_mlir_transforms`.
    for edf_name in nested_mlir_transforms.keys() | nested_fn_transforms.keys():
        if edf_name in nested_functions:
            edf_transform_fn = nested_fn_transforms.get(edf_name, [])
            edf_mlir_pipeline = nested_mlir_transforms.get(edf_name, [])
            transformed_edf = transform_eager_defined_function(
                rt, nested_functions[edf_name], edf_transform_fn, edf_mlir_pipeline)
            transformed_edf.add_to_graph(graph, overwrite=True)
            transformed_edf_name = compat.as_str(transformed_edf.name)
            transformed_nested_functions[transformed_edf_name] = transformed_edf
            nested_transforms_map[edf_name] = transformed_edf_name

    # Update the `FunctionDef` to map to the newly created EDFs.
    for node in fndef.node_def:
        for attr_value in node.attr.values():
            if attr_value.HasField("func"):
                attr_value.func.name = nested_transforms_map[attr_value.func.name]

  # Register the updated fndef with the runtime.
rt.CreateFunction(fndef)

# Create a new FuncGraph from the modified FunctionDef.
structured_input_signature = cf.structured_input_signature
structured_outputs_signature = (
    func_graph_module.convert_structure_to_signature(cf.structured_outputs))
with graph.as_default():
    func_graph = function_def_lib.function_def_to_graph(
        fndef,
        structured_input_signature=structured_input_signature,
        structured_outputs=structured_outputs_signature,
        propagate_device_spec=True)

# Set handle data.
for i, output in enumerate(cf.outputs):
    func_graph_output = func_graph.outputs[i]
    if isinstance(output, ops.Tensor) and isinstance(func_graph_output,
                                                     ops.Tensor):
        func_graph_output.set_shape(output.shape)
        handle_data_util.copy_handle_data(output, func_graph_output)

  # We delete the `_input_shapes` attribute to avoid any intermediate
  # ShapeInference information from being carried over as the user's
  # transformations can invalidate them.
if "_input_shapes" in fndef.attr:
    del fndef.attr["_input_shapes"]

# Replicate custom gradients to the new Graph.
with ops.init_scope():
    _replicate_gradient_functions(cf._func_graph, func_graph)  # pylint: disable=protected-access

# pylint: disable=protected-access
# Get the new ConcreteFunction.
updated_cf = function_lib.ConcreteFunction(
    func_graph, attrs=fndef.attr, spec=cf._function_spec)

# Set arg_keywords and positional_args
updated_cf._arg_keywords = cf._arg_keywords
updated_cf._num_positional_args = cf._num_positional_args
saved_model_utils.restore_captures(updated_cf, cf.captured_inputs)
# pylint: enable=protected-access

# Register the ConcreteFunction with the python Graph.
if nested_fn_transforms or nested_mlir_transforms:
    for transformed_edf in transformed_nested_functions.values():
        transformed_edf.add_to_graph(updated_cf.graph, overwrite=True)
updated_cf.add_to_graph(graph, overwrite=True)

exit(updated_cf)
