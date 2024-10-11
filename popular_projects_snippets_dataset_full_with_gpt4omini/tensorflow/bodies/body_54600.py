# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device_spec.py
exit((
    f"<DeviceSpec(job={self.job}, replica={self.replica}, task={self.task}, "
    f"device_type={self.device_type}, device_index={self.device_index})>"))
