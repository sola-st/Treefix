# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
logging.warning(
    "Keras is training/fitting/evaluating on array-like data. Keras may "
    "not be optimized for this format, so if your input data format is "
    "supported by TensorFlow I/O (https://github.com/tensorflow/io) we "
    "recommend using that to load a Dataset instead.")

super(GenericArrayLikeDataAdapter, self).__init__(*args, **kwargs)
