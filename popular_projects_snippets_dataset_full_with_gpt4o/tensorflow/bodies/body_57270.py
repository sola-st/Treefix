# Extracted from ./data/repos/tensorflow/tensorflow/lite/toco/python/toco_from_protos.py
"""Runs the converter."""
with open(FLAGS.model_proto_file, "rb") as model_file:
    model_str = model_file.read()

with open(FLAGS.toco_proto_file, "rb") as toco_file:
    toco_str = toco_file.read()

with open(FLAGS.model_input_file, "rb") as input_file:
    input_str = input_file.read()

debug_info_str = None
if FLAGS.debug_proto_file:
    with open(FLAGS.debug_proto_file, "rb") as debug_info_file:
        debug_info_str = debug_info_file.read()

enable_mlir_converter = FLAGS.enable_mlir_converter

output_str = _pywrap_toco_api.TocoConvert(
    model_str,
    toco_str,
    input_str,
    False,  # extended_return
    debug_info_str,
    enable_mlir_converter)
open(FLAGS.model_output_file, "wb").write(output_str)
sys.exit(0)
