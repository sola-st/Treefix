# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/reverse_xxd_dump_from_cc.py
model = flatbuffer_utils.xxd_output_to_object(FLAGS.input_cc_file)
flatbuffer_utils.write_model(model, FLAGS.output_tflite_file)
