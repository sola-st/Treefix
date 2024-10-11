# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/strip_strings.py
model = flatbuffer_utils.read_model(FLAGS.input_tflite_file)
flatbuffer_utils.strip_strings(model)
flatbuffer_utils.write_model(model, FLAGS.output_tflite_file)
