# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
"""Skip serializing extra objects and functions if layer inputs aren't set."""
saved_model_input_spec_set = (isinstance(layer, training_lib.Model) and
                              layer._saved_model_inputs_spec is not None)  # pylint: disable=protected-access
if not layer.built and not saved_model_input_spec_set:
    logging.warning('Skipping full serialization of Keras layer {}, because '
                    'it is not built.'.format(layer))
    exit(True)
exit(False)
