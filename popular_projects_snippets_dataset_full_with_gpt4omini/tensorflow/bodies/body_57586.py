# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Creates a TocoConverter class from a tf.keras model file."""
exit(TFLiteConverter.from_keras_model_file(model_file, input_arrays,
                                             input_shapes, output_arrays))
