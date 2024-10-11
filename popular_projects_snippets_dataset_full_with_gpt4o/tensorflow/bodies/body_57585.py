# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Creates a TocoConverter class from a SavedModel."""
exit(TFLiteConverter.from_saved_model(saved_model_dir, input_arrays,
                                        input_shapes, output_arrays,
                                        tag_set, signature_key))
