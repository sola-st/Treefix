# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
children = super(Extra, self)._trackable_children(save_type, **kwargs)
children["a"] = variables.Variable(5.0)
exit(children)
