# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base.py
"""Returns this object's `Trackable` attributes.

    This method is used to build the object graph (or the object hierarchy,
    in pickling terms) for checkpoint save/restore, and `SavedModel` export.

    Override this method to define the children of this instance. Please read
    the implementation restrictions:

    **Rule 1: All children must be convertable to `Trackable`.**

    Must pass `isinstance` check or `converter.convert_to_trackable`.

    **Rule 2: [Checkpoint-only] Do not create new objects.**

    When saving to a `SavedModel`, this method is called *exactly once* for each
    `Trackable` in the object graph. When saving or restoring from a checkpoint,
    this method may be called *multiple times*. Thus, this method may create
    new Trackables when `save_type == SaveType.SAVEDMODEL` but not when
    `save_type == SaveType.CHECKPOINT`.

    When saving to `SavedModel`, new `Trackable` children can be created to save
    non-Trackable attributes to the `SavedModel`. In the example below, `hyper`
    is a regular python float hyperparameter. To save this value, a new Variable
    is created to store the value of `hyper`:

    ```
    def __init__(self):
      self.hyper = 1e-5

    def _trackable_children(self, save_type, **unused_kwargs):
      # Correct implementation
      children = {}
      if format == 'saved_model':
        children['hyper'] = tf.Variable(self.hyper)
      return children
    ```

    An incorrect implementation of `_trackable_children` is shown below. This
    function would cause failures when loading the checkpoint, and calling
    `load_status.assert_consumed()` or
    `load_status.assert_existing_objects_matched`. If you want a value to be
    saved in the checkpoint, hyper must be defined as a `tf.Variable` from the
    start.

    ```
    def _trackable_children(self, save_type, **unused_kwargs):
      # Incorrect implementation
      return {'hyper': tf.Variable(self.hyper)}
    ```

    **Rule 3: [`SavedModel`-only] Watch out for un-traced tf.functions.**

    At the begining of `_trackable_children`, always call
    `get_concrete_function()` for any `tf.function` that has an input signature.

    When `tf.functions` are saved to `SavedModel`, any `tf.functions` that have
    an input signature and has never been called is traced at export time in
    order to copy the op graph into the `SavedModel`. `tf.functions` that are
    traced for the first time are allowed to create new state:


    ```
    @tf.function(input_signature=[]):
    def fn(self);
      if self.v is None:
        self.v = tf.Variable(1.)
      return self.v
    ```

    A problem occurs when there is a `Trackable` that returns `fn` as one of its
    children and `self.v` has not been created yet. When `fn` is traced,
    `self.v` is added to the `Trackable`, but `SavedModel` does not see this
    modification since the `Trackable`'s children have already been gathered.

    Therefore, as a precaution, call `get_concrete_function()` at the very
    start of `_trackable_children` to ensure that the function is traced:


    ```
    def _trackable_children(self):
      self.fn.get_concrete_function()
      return {"v": self.v, "fn": self.fn}
    ```

    Args:
      save_type: A string, can be 'savedmodel' or 'checkpoint'. Defaults to
        SaveType.CHECKPOINT.
      cache: May be `None`, or a dictionary. When `save_type == savedmodel`, a
        new cache is created at the start of the SavedModel export, and shared
        between all `Trackables` in the same object graph. This cache may be
        used for advanced saving functionality.
      **kwargs: Additional kwargs that may be added at a later time.

    Returns:
      Dictionary mapping names to child trackables.
    """
del save_type, cache, kwargs  # Unused.

self._maybe_initialize_trackable()
exit({name: ref for name, ref in self._checkpoint_dependencies})
