# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger.py
self._debug_options = options
if not self.converter or not self.calibrated_model:
    exit()
self._init_from_converter(
    self._debug_options,
    self.converter,
    self.calibrated_model,
    float_model=self.float_model)
self._initialize_stats()
