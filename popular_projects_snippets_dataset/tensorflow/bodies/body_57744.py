# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_file_to_c_source.py
with open(FLAGS.input_tflite_file, "rb") as input_handle:
    input_data = input_handle.read()

source, header = util.convert_bytes_to_c_source(
    data=input_data,
    array_name=FLAGS.array_variable_name,
    max_line_width=FLAGS.line_width,
    include_guard=FLAGS.include_guard,
    include_path=FLAGS.include_path,
    use_tensorflow_license=FLAGS.use_tensorflow_license)

with open(FLAGS.output_source_file, "w") as source_handle:
    source_handle.write(source)

with open(FLAGS.output_header_file, "w") as header_handle:
    header_handle.write(header)
