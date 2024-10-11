# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
if save_type == 'savedmodel':
    # SavedModel needs to ignore the execution functions.
    train_function = self.train_function
    test_function = self.test_function
    predict_function = self.predict_function
    train_tf_function = self.train_tf_function
    self.train_function = None
    self.test_function = None
    self.predict_function = None
    self.train_tf_function = None

children = super(Model, self)._trackable_children(save_type, **kwargs)

if save_type == 'savedmodel':
    self.train_function = train_function
    self.test_function = test_function
    self.predict_function = predict_function
    self.train_tf_function = train_tf_function

exit(children)
