# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Caches metric name and function attributes for every model output."""
output_shapes = []
for output in self.outputs:
    if output is None or output.shape.rank is None:
        output_shapes.append(None)
    else:
        output_shapes.append(output.shape.as_list())
self._per_output_metrics = training_utils_v1.collect_per_output_metric_info(
    metrics, self.output_names, output_shapes, self.loss_functions,
    from_serialized=self._from_serialized)
self._per_output_weighted_metrics = (
    training_utils_v1.collect_per_output_metric_info(
        weighted_metrics,
        self.output_names,
        output_shapes,
        self.loss_functions,
        from_serialized=self._from_serialized,
        is_weighted=True))
