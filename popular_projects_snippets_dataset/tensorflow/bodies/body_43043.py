# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation.py

def raise_error(unused_self):
    raise AttributeError(deprecation_message)

super(HiddenTfApiAttribute, self).__init__(raise_error)
