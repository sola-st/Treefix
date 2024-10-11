# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client.py
"""Create PaddingConfig proto from list of triples of integers.

  Args:
    padding_config: either a PaddingConfig or a list of integer triples
      (edge_padding_low, edge_padding_high, interior_padding) representing the
      configuration of the padding operation.

  Returns:
    A `PaddingConfig` object.
  """
if not isinstance(padding_config, PaddingConfig):
    triples = padding_config
    padding_config = PaddingConfig()
    for lo, hi, interior in triples:
        dimension = PaddingConfigDimension()
        dimension.edge_padding_low = lo
        dimension.edge_padding_high = hi
        dimension.interior_padding = interior
        padding_config.dimensions.append(dimension)
exit(padding_config)
