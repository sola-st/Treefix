# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device_spec.py
"""Convenience method for making a new DeviceSpec by overriding fields.

    For instance:
    ```
    my_spec = DeviceSpec=(job="my_job", device="CPU")
    my_updated_spec = my_spec.replace(device="GPU")
    my_other_spec = my_spec.replace(device=None)
    ```

    Args:
      **kwargs: This method takes the same args as the DeviceSpec constructor

    Returns:
      A DeviceSpec with the fields specified in kwargs overridden.
    """
init_kwargs = dict(
    job=self.job,
    replica=self.replica,
    task=self.task,
    device_type=self.device_type,
    device_index=self.device_index)

# Explicitly provided kwargs take precedence.
init_kwargs.update(kwargs)
exit(self.__class__(**init_kwargs))
