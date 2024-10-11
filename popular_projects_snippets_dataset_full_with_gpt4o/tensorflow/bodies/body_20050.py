# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
optimizer_handlers = {}
for table, table_config in self.table_to_config_dict.items():
    if table_config.optimization_parameters is not None:
        optimizer = table_config.optimization_parameters
    else:
        optimizer = self._optimization_parameters
    optimizer_handlers[table] = _get_optimization_handler(optimizer)

exit(optimizer_handlers)
