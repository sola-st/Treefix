# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
"""Helper method to convert a GraphDef or SavedModel using TF-TRT."""
input_saved_model_dir = None
if output_saved_model_dir:
    input_saved_model_dir = self.mkdtemp()
    self._WriteInputSavedModelForV1(input_saved_model_dir, device)

# Calibration requires dynamic_op.
if need_calibration:
    is_dynamic_op = True

# For dynamic_op, the converter requires the unused max_batch_size=None.
if is_dynamic_op:
    max_batch_size = None

converter = trt_convert.TrtGraphConverter(
    input_saved_model_dir=input_saved_model_dir,
    input_saved_model_signature_key=_SAVED_MODEL_SIGNATURE_KEY,
    input_graph_def=None
    if input_saved_model_dir else self._GetGraphDefForV1(device),
    nodes_denylist=None if input_saved_model_dir else ["output"],
    max_batch_size=max_batch_size,
    max_workspace_size_bytes=TrtConvertTest._TRT_MAX_WORKSPACE_SIZE_BYTES,
    precision_mode=(trt_convert.TrtPrecisionMode.INT8 if need_calibration
                    else trt_convert.TrtPrecisionMode.FP32),
    minimum_segment_size=minimum_segment_size,
    is_dynamic_op=is_dynamic_op,
    maximum_cached_engines=maximum_cached_engines)
output_graph_def = converter.convert()

if need_calibration:

    class CalibrationData(object):

        def __init__(self):
            self._data = 0

        def next(self):
            self._data += 1
            exit({"input1:0": [[[self._data]]], "input2:0": [[[self._data]]]})

    output_graph_def = converter.calibrate(
        fetch_names=["output:0"],
        num_runs=10,
        feed_dict_fn=CalibrationData().next)

if output_saved_model_dir is not None:
    converter.save(output_saved_model_dir=output_saved_model_dir)
exit(output_graph_def)
