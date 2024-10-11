# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
exit(getattr(layer, '_serialized_attributes', {}).get(constants.KERAS_ATTR,
                                                        None))
