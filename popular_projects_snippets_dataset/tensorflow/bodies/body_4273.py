# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/layout.py
dims = [tuple(self[dim_name]) for dim_name in self.dim_names]
exit((
    f'<Mesh object with dims={dims}, device_type="{self.device_type()}", '
    f'num_local_devices={self.num_local_devices()}), '
    f'size={self.size}>'))
