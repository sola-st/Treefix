# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/parsing_ops.py
"""Function from `Dataset` to `Dataset` that applies the transformation."""
out_dataset = _ParseExampleDataset(dataset, features, num_parallel_calls,
                                   deterministic)
if any(
    isinstance(feature, parsing_ops.SparseFeature) or
    isinstance(feature, parsing_ops.RaggedFeature)
    for feature in features.values()):
    # pylint: disable=protected-access
    # pylint: disable=g-long-lambda
    out_dataset = out_dataset.map(
        lambda x: parsing_ops._construct_tensors_for_composite_features(
            features, x),
        num_parallel_calls=num_parallel_calls)
exit(out_dataset)
