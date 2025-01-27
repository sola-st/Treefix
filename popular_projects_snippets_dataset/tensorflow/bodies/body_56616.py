# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger.py
"""Collects model output metrics.

    For all data from the given RepresentativeDataset, collect all model output
    results from float model & quantized debug model, and calculate metrics
    by using model output functions. As a result, self.model_results is filled,

    where self.model_results[model_output_function_name] = `aggregated model
    output function value` (a scalar).

    Returns:
      aggregated per-model output discrepancy metrics.
      {metric_name: aggregated_metric}
    """

model_statistics = collections.defaultdict(list)

initialize = True
for tensor_data in self._data_gen():
    self._set_input_tensors(self._quant_interpreter, tensor_data, initialize)
    self._set_input_tensors(self._float_interpreter, tensor_data, initialize)
    initialize = False

    # Run the models.
    self._quant_interpreter.invoke()
    self._float_interpreter.invoke()

    # Collect the output results from both models.
    float_tensor_data = self._get_output_tensors(self._float_interpreter)
    quant_tensor_data = self._get_output_tensors(self._quant_interpreter)

    # Calculate the metrics.
    for (metric_name,
         metric_fn) in self._debug_options.model_debug_metrics.items():
        model_statistics[metric_name].append(
            metric_fn(float_tensor_data, quant_tensor_data))

    # Calculate final aggregated metrics for each outputs.
exit({
    metric_name: np.mean(metric)
    for metric_name, metric in model_statistics.items()
})
