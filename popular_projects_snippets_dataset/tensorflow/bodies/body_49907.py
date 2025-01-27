# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/keras_parameterized.py
"""Execute the decorated test with all Keras saved model formats).

  This decorator is intended to be applied either to individual test methods in
  a `keras_parameterized.TestCase` class, or directly to a test class that
  extends it. Doing so will cause the contents of the individual test
  method (or all test methods in the class) to be executed multiple times - once
  for each Keras saved model format.

  The Keras saved model formats include:
  1. HDF5: 'h5'
  2. SavedModel: 'tf'

  Note: if stacking this decorator with absl.testing's parameterized decorators,
  those should be at the bottom of the stack.

  Various methods in `testing_utils` to get file path for saved models will
  auto-generate a string of the two saved model formats. This allows unittests
  to confirm the equivalence between the two Keras saved model formats.

  For example, consider the following unittest:

  ```python
  class MyTests(testing_utils.KerasTestCase):

    @testing_utils.run_with_all_saved_model_formats
    def test_foo(self):
      save_format = testing_utils.get_save_format()
      saved_model_dir = '/tmp/saved_model/'
      model = keras.models.Sequential()
      model.add(keras.layers.Dense(2, input_shape=(3,)))
      model.add(keras.layers.Dense(3))
      model.compile(loss='mse', optimizer='sgd', metrics=['acc'])

      keras.models.save_model(model, saved_model_dir, save_format=save_format)
      model = keras.models.load_model(saved_model_dir)

  if __name__ == "__main__":
    tf.test.main()
  ```

  This test tries to save the model into the formats of 'hdf5', 'h5', 'keras',
  'tensorflow', and 'tf'.

  We can also annotate the whole class if we want this to apply to all tests in
  the class:
  ```python
  @testing_utils.run_with_all_saved_model_formats
  class MyTests(testing_utils.KerasTestCase):

    def test_foo(self):
      save_format = testing_utils.get_save_format()
      saved_model_dir = '/tmp/saved_model/'
      model = keras.models.Sequential()
      model.add(keras.layers.Dense(2, input_shape=(3,)))
      model.add(keras.layers.Dense(3))
      model.compile(loss='mse', optimizer='sgd', metrics=['acc'])

      keras.models.save_model(model, saved_model_dir, save_format=save_format)
      model = tf.keras.models.load_model(saved_model_dir)

  if __name__ == "__main__":
    tf.test.main()
  ```

  Args:
    test_or_class: test method or class to be annotated. If None,
      this method returns a decorator that can be applied to a test method or
      test class. If it is not None this returns the decorator applied to the
      test or class.
    exclude_formats: A collection of Keras saved model formats to not run.
      (May also be a single format not wrapped in a collection).
      Defaults to None.

  Returns:
    Returns a decorator that will run the decorated test method multiple times:
    once for each desired Keras saved model format.

  Raises:
    ImportError: If abseil parameterized is not installed or not included as
      a target dependency.
  """
# Exclude h5 save format if H5py isn't available.
if h5py is None:
    exclude_formats.append(['h5'])
saved_model_formats = ['h5', 'tf', 'tf_no_traces']
params = [('_%s' % saved_format, saved_format)
          for saved_format in saved_model_formats
          if saved_format not in nest.flatten(exclude_formats)]

def single_method_decorator(f):
    """Decorator that constructs the test cases."""
    # Use named_parameters so it can be individually run from the command line
    @parameterized.named_parameters(*params)
    @functools.wraps(f)
    def decorated(self, saved_format, *args, **kwargs):
        """A run of a single test case w/ the specified model type."""
        if saved_format == 'h5':
            _test_h5_saved_model_format(f, self, *args, **kwargs)
        elif saved_format == 'tf':
            _test_tf_saved_model_format(f, self, *args, **kwargs)
        elif saved_format == 'tf_no_traces':
            _test_tf_saved_model_format_no_traces(f, self, *args, **kwargs)
        else:
            raise ValueError('Unknown model type: %s' % (saved_format,))
    exit(decorated)

exit(_test_or_class_decorator(test_or_class, single_method_decorator))
