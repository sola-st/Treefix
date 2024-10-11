# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
try:
    calibration_table = gen_trt_ops.get_calibration_data_op(
        _get_canonical_engine_name(node.name))
    node.attr["calibration_data"].s = calibration_table.numpy()
except (errors.UnknownError, errors.NotFoundError):
    logging.warning("Warning calibration error for %s", node.name)
