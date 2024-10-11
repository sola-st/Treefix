# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/python/modify_model_interface.py
input_type = mmi_constants.STR_TO_TFLITE_TYPES[FLAGS.input_type]
output_type = mmi_constants.STR_TO_TFLITE_TYPES[FLAGS.output_type]

mmi_lib.modify_model_interface(FLAGS.input_tflite_file,
                               FLAGS.output_tflite_file, input_type,
                               output_type)

print('Successfully modified the model input type from FLOAT to '
      '{input_type} and output type from FLOAT to {output_type}.'.format(
          input_type=FLAGS.input_type, output_type=FLAGS.output_type))
