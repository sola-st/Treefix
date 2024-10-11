# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
exit([(self._prefix + local_name, spec.name)
        for local_name, spec in zip(self._local_names, self.specs)])
