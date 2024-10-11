# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger.py
if not self.converter:
    raise ValueError('No converter found, use this function with the '
                     'converter option in the constructor.')

exit(convert.mlir_quantize(
    self.calibrated_model,
    disable_per_channel=self.converter._experimental_disable_per_channel,  # pylint: disable=protected-access
    fully_quantize=self._debug_options.fully_quantize,
    enable_numeric_verify=is_debug,
    denylisted_ops=self._debug_options.denylisted_ops,
    denylisted_nodes=self._debug_options.denylisted_nodes))
