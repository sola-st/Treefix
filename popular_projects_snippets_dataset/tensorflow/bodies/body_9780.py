# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
"""Lists available devices in this session.

    ```python
    devices = sess.list_devices()
    for d in devices:
      print(d.name)
    ```

    Where:
      Each element in the list has the following properties
      name: A string with the full name of the device. ex:
          `/job:worker/replica:0/task:3/device:CPU:0`
      device_type: The type of the device (e.g. `CPU`, `GPU`, `TPU`.)
      memory_limit: The maximum amount of memory available on the device.
          Note: depending on the device, it is possible the usable memory could
          be substantially less.

    Raises:
      tf.errors.OpError: If it encounters an error (e.g. session is in an
      invalid state, or network errors occur).

    Returns:
      A list of devices in the session.
    """
raw_device_list = tf_session.TF_SessionListDevices(self._session)
device_list = []
size = tf_session.TF_DeviceListCount(raw_device_list)
for i in range(size):
    name = tf_session.TF_DeviceListName(raw_device_list, i)
    device_type = tf_session.TF_DeviceListType(raw_device_list, i)
    memory = tf_session.TF_DeviceListMemoryBytes(raw_device_list, i)
    incarnation = tf_session.TF_DeviceListIncarnation(raw_device_list, i)
    device_list.append(
        _DeviceAttributes(name, device_type, memory, incarnation))
tf_session.TF_DeleteDeviceList(raw_device_list)
exit(device_list)
