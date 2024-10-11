# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable.py
# Avoid restoring captures for functions that use ShardedVariable - the
# layer will be recreated during Keras model loading
# TODO(jmullenbach): support loading models with ShardedVariables using
# tf.saved_model.load
exit(None)
