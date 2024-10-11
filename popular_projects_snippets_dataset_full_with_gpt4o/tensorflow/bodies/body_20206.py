# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2_utils.py
"""Set the table descriptor from the table data."""
table_descriptor.name = self.name

# For small tables, we pad to the number of hosts so that at least one
# id will be assigned to each host.
table_descriptor.vocabulary_size = max(self.vocabulary_size, num_hosts)
table_descriptor.dimension = self.dim

parameters = table_descriptor.optimization_parameters

# We handle the learning rate separately here and don't allow the
# optimization class to handle this, as it doesn't know about dynamic
# rates.
if callable(self.optimizer.learning_rate):
    parameters.learning_rate.dynamic.tag = (
        learning_rate_index[self.optimizer.learning_rate])
else:
    parameters.learning_rate.constant = self.optimizer.learning_rate

if self.optimizer.low_dimensional_packing_status:
    parameters.low_dimensional_packing_status = (
        optimization_parameters_pb2.LowDimensionalPackingStatus.Status.ENABLED
    )
# Use optimizer to handle the rest of the parameters.
self.optimizer._set_optimization_parameters(parameters)  # pylint: disable=protected-access
if self.quantization_config:
    self.quantization_config._set_optimization_parameters(parameters)  # pylint: disable=protected-access
