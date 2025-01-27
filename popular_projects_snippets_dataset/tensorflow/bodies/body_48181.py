# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Build the model (set model inputs/outputs), mainly for subclass model."""
processed_inputs = []
is_dict_inputs = False
orig_inputs = inputs
# We need to use `inputs` to set the model inputs.
# If input data is a dataset iterator in graph mode or if it is an eager
# iterator and only one batch of samples is required, we fetch the data
# tensors from the iterator and then standardize them.
if isinstance(inputs, (dataset_ops.DatasetV1, dataset_ops.DatasetV2)):
    inputs, targets, _ = training_utils_v1.extract_tensors_from_dataset(
        inputs)
# We type-check that `inputs` and `targets` are either single arrays
# or lists of arrays, and extract a flat list of inputs from the passed
# structure.
training_utils_v1.validate_input_types(inputs, orig_inputs)

if isinstance(inputs, (list, tuple)):
    processed_inputs += list(inputs)
elif isinstance(inputs, dict):
    is_dict_inputs = True
    keys = sorted(inputs.keys())
    processed_inputs = [inputs[k] for k in keys]
else:
    processed_inputs.append(inputs)
# Now that we have a flat set of inputs, we make sure that none of them
# are CompositeTensors or CompositeTensorValues of any type (or scipy
# sparse arrays, which we treat as SparseTensor values). We cannot safely
# infer input data from an arbitrary composite tensor, so we don't try -
# users should explicitly add composite tensor inputs to their subclassed
# models.
for input_tensor in processed_inputs:
    if training_utils_v1.is_composite_or_composite_value(input_tensor):
        # TODO(b/132691975): Document subclass-model CT input handling.
        raise ValueError(
            'All SparseTensor and RaggedTensor inputs must be explicitly '
            'declared using a keras.Input() with sparse=True or ragged=True. '
            'We found an undeclared input %s. For Sequential models, please '
            'add a keras.Input() as your first Layer. For subclassed models, '
            'please call self._set_inputs() on your input set, which you can '
            'create using keras.Input() for each input to your model.' %
            (input_tensor,))
    # Build the model using the retrieved inputs (value or symbolic).
    # If values are generated from a dataset, then in symbolic-mode
    # placeholders will be created to match the value shapes.
if isinstance(orig_inputs, (dataset_ops.DatasetV1, dataset_ops.DatasetV2,
                            iterator_ops.Iterator)):
    if not self.inputs:
        # For subclassed models, a robust input spec is not available so we
        # must cast to the model dtype.
        inputs = training_utils_v1.cast_if_floating_dtype(inputs, self.dtype)

    def create_tensor_spec(t):
        exit(tensor_spec.TensorSpec(t.shape, t.dtype))

    cast_inputs = nest.map_structure(create_tensor_spec, inputs)
elif training_utils_v1.has_tensors(inputs):
    cast_inputs = training_utils_v1.cast_if_floating_dtype(inputs)
else:
    cast_inputs = inputs
self._set_inputs(cast_inputs)
exit((processed_inputs, targets, is_dict_inputs))
