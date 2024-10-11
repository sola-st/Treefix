# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
"""Run inference with converted graph in order to build TensorRT engines.

    If the conversion requires INT8 calibration, then a reference to the
    calibration function was stored during the call to convert(). Calibration
    will be performed while we build the TensorRT engines.

    Args:
      input_fn: a generator function that provides the input data as a single
        array, OR a list or tuple of the arrays OR a dict, which will be used
        to execute the converted signature to generate TRT engines.
        Example 1:
        `def input_fn():
             # Let's assume a network with 1 input tensor.
             # We generate 2 sets of dummy input data:
             input_shapes = [(1, 16),    # 1st shape
                             (2, 32)]    # 2nd shape
             for shapes in input_shapes:
                 # return an input tensor
                 yield np.zeros(shape).astype(np.float32)'

        Example 2:
        `def input_fn():
             # Let's assume a network with 2 input tensors.
             # We generate 3 sets of dummy input data:
             input_shapes = [[(1, 16), (2, 16)], # 1st input list
                             [(2, 32), (4, 32)], # 2nd list of two tensors
                             [(4, 32), (8, 32)]] # 3rd input list
             for shapes in input_shapes:
                 # return a list of input tensors
                 yield [np.zeros(x).astype(np.float32) for x in shapes]`

    Raises:
      NotImplementedError: build() is already called.
      RuntimeError: the input_fx is None.
    """
if self._build_called_once:
    raise NotImplementedError("build() is already called. It is not "
                              "supported to call build() more than once.")
if not input_fn:
    raise RuntimeError("input_fn is None. Method build() needs input_fn "
                       "to be specified in order to build TensorRT engines")
if not self._converted:
    raise RuntimeError("Need to call convert() before build()")
if (self._need_calibration and not self._calibrated and
    self._calibration_input_fn is None):
    raise RuntimeError("Need to provide the calibration_input_fn arg while "
                       "calling convert().")

def _set_profile_generation_mode(value, node):
    node.attr["_profile_generation_mode"].b = value

if self._need_trt_profiles():
    # Enable profile generation.
    self._for_each_trt_node(self._converted_graph_def,
                            partial(_set_profile_generation_mode, True))
    # Profile generation is enabled using the _profile_generation_mode
    # attribute of the TRTEngineOps. We need to rebuild the function to
    # change this attribute.
    func = _construct_function_from_graph_def(self._converted_func,
                                              self._converted_graph_def)
else:
    func = self._converted_func

first_input = None
# Run inference:
#   Builds TRT engines if self._need_trt_profiles is False.
#   Builds TRT optimization profiles if self._need_trt_profiles is True.
for inp in input_fn():
    if first_input is None:
        first_input = inp
    args, kwargs = _convert_to_tensor(inp)
    func(*args, **kwargs)

if self._need_trt_profiles():
    # Disable profile generation.
    self._for_each_trt_node(self._converted_graph_def,
                            partial(_set_profile_generation_mode, False))

# Run calibration if required, this would have been skipped in
# the convert step
if self._need_calibration and not self._calibrated:
    self._execute_calibration(self._calibration_input_fn)
    # calibration also builds the engine
else:
    # Use the first input in explicit batch mode to build TensorRT engines
    # after generating all the profiles. The first input is used but any of
    # the inputs can be used because the shape of this input does not
    # determine the engine and instead the shapes collected in profiles
    # determine the engine.
    args, kwargs = _convert_to_tensor(first_input)
    self._converted_func(*args, **kwargs)

self._build_called_once = True
