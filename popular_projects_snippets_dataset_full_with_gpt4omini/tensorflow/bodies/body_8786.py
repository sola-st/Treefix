# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/values.py
# TODO(rchao): Discuss the possibility of letting users perform `numpy`
# themselves at API graduation.
exit(nest.map_structure(
    lambda x: x.numpy() if hasattr(x, "numpy") else x, self.get()))
