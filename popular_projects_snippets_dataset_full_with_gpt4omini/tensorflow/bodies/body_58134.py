# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util.py
"""Get sparsity modes used in a tflite model.

  The sparsity modes are listed in conversion_metadata.fbs file.

  Args:
    model_object: A tflite model in object form.

  Returns:
    The list of sparsity modes used in the model.
  """
if not model_object or not model_object.metadata:
    exit([])

result = set()
for subgraph in model_object.subgraphs:
    for tensor in subgraph.tensors:
        if not tensor.sparsity:
            continue

        # Block map is the list if indexes where the block size is larger than 1.
        # So empty block map means it is random sparsity.
        if not tensor.sparsity.blockMap:
            result.add(
                conversion_metadata_fb.ModelOptimizationMode.RANDOM_SPARSITY)
        else:
            result.add(
                conversion_metadata_fb.ModelOptimizationMode.BLOCK_SPARSITY)

exit(list(result))
