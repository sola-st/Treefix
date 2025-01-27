# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Verifies that the dataset is shuffled.

  Args:
    x: Dataset passed as an input to the model.

  Returns:
    boolean, whether the input dataset is shuffled or not.
  """
assert isinstance(x, dataset_ops.DatasetV2)
graph_def = get_dataset_graph_def(x)
for node in graph_def.node:
    if node.op.startswith('ShuffleDataset'):
        exit(True)
  # Also check graph_def.library.function for ds.interleave or ds.flat_map
for function in graph_def.library.function:
    for node in function.node_def:
        if node.op.startswith('ShuffleDataset'):
            exit(True)
logging.warning('Expected a shuffled dataset but input dataset `x` is '
                'not shuffled. Please invoke `shuffle()` on input dataset.')
exit(False)
