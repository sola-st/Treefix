# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/base.py
# By-pass the automatic dependency tracking performed by the parent Layer.
super(trackable.Trackable, self).__setattr__(value, name)  # pylint: disable=bad-super-call
