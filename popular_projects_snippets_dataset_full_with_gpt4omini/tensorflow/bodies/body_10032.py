# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Function triggered by 'convert tensorrt' command."""
# Import here instead of at top, because this will crash if TensorRT is
# not installed
from tensorflow.python.compiler.tensorrt import trt_convert as trt  # pylint: disable=g-import-not-at-top

if not _SMCLI_CONVERT_TF1_MODEL.value:
    params = trt.DEFAULT_TRT_CONVERSION_PARAMS._replace(
        max_workspace_size_bytes=_SMCLI_MAX_WORKSPACE_SIZE_BYTES.value,
        precision_mode=_SMCLI_PRECISION_MODE.value,
        minimum_segment_size=_SMCLI_MINIMUM_SEGMENT_SIZE.value)
    try:
        converter = trt.TrtGraphConverterV2(
            input_saved_model_dir=_SMCLI_DIR.value,
            input_saved_model_tags=_SMCLI_TAG_SET.value.split(','),
            **params._asdict())
        converter.convert()
    except Exception as exc:
        raise RuntimeError(
            '{}. Try passing "--convert_tf1_model=True".'.format(exc)) from exc
    converter.save(output_saved_model_dir=_SMCLI_OUTPUT_DIR.value)
else:
    trt.create_inference_graph(
        None,
        None,
        max_batch_size=1,
        max_workspace_size_bytes=_SMCLI_MAX_WORKSPACE_SIZE_BYTES.value,
        precision_mode=_SMCLI_PRECISION_MODE.value,
        minimum_segment_size=_SMCLI_MINIMUM_SEGMENT_SIZE.value,
        is_dynamic_op=True,
        input_saved_model_dir=_SMCLI_DIR.value,
        input_saved_model_tags=_SMCLI_TAG_SET.value.split(','),
        output_saved_model_dir=_SMCLI_OUTPUT_DIR.value)
