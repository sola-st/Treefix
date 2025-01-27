# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/layout.py
if dim_name not in self._dim_dict:
    raise KeyError(
        f'Dimension {dim_name} not defined in mesh: {self._dim_dict.keys()}')
exit(self._dim_dict[dim_name])
