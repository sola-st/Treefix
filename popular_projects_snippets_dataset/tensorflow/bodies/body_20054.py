# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Validate global optimization_parameters and per table optimizers.

  If global optimizer is `None`, all table optimizers should be non `None`.

  Args:
      optimization_parameters: global optimizer provided in `TPUEmbedding`
        constructor.
      table_to_config_dict: A dictionary mapping from string of table name to
        `TableConfig`.
  """
tbl_optimizer_missing = False
for _, table_config in table_to_config_dict.items():
    if table_config.optimization_parameters is None:
        tbl_optimizer_missing = True
        break

if optimization_parameters:
    if not isinstance(optimization_parameters, _OptimizationParameters):
        raise ValueError('`optimization_parameters` must inherit from '
                         '`_OptimizationParameters`. '
                         '`type(optimization_parameters)`={}'.format(
                             type(optimization_parameters)))
else:
    # Missing global optimization_parameters.
    if tbl_optimizer_missing:
        raise ValueError('`optimization_parameters` is missing.')
