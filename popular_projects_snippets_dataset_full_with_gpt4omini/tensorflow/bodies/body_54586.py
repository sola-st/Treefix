# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device_spec.py
"""Parse a `DeviceSpec` name into its components.

    **2.x behavior change**:

    In TensorFlow 1.x, this function mutates its own state and returns itself.
    In 2.x, DeviceSpecs are immutable, and this function will return a
      DeviceSpec which contains the spec.

    * Recommended:

      ```
      # my_spec and my_updated_spec are unrelated.
      my_spec = tf.DeviceSpec.from_string("/CPU:0")
      my_updated_spec = tf.DeviceSpec.from_string("/GPU:0")
      with tf.device(my_updated_spec):
        ...
      ```

    * Will work in 1.x and 2.x (though deprecated in 2.x):

      ```
      my_spec = tf.DeviceSpec.from_string("/CPU:0")
      my_updated_spec = my_spec.parse_from_string("/GPU:0")
      with tf.device(my_updated_spec):
        ...
      ```

    * Will NOT work in 2.x:

      ```
      my_spec = tf.DeviceSpec.from_string("/CPU:0")
      my_spec.parse_from_string("/GPU:0")  # <== Will not update my_spec
      with tf.device(my_spec):
        ...
      ```

    In general, `DeviceSpec.from_string` should completely replace
    `DeviceSpec.parse_from_string`, and `DeviceSpec.replace` should
    completely replace setting attributes directly.

    Args:
      spec: an optional string of the form
       /job:<name>/replica:<id>/task:<id>/device:CPU:<id> or
       /job:<name>/replica:<id>/task:<id>/device:GPU:<id> as cpu and gpu are
         mutually exclusive. All entries are optional.

    Returns:
      The `DeviceSpec`.

    Raises:
      ValueError: if the spec was not valid.
    """
exit(self.from_string(spec))
