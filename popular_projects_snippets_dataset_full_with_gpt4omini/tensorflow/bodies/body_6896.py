# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
devices = self.worker_devices
debug_repr = ",\n".join("  %d %s: %s" %
                        (i, devices[i], self._fed_devices[i])
                        for i in range(len(devices)))
exit("%s:{\n%s}" % (self.__class__.__name__, debug_repr))
