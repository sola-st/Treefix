# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
if self._context_handle is None:
    exit("Eager TensorFlow Context. Devices currently uninitialized.")
else:
    devices = self._devices
    lines = ["Eager TensorFlow Context with %d devices" % (len(devices))]
    for i, d in enumerate(devices):
        lines.append("   Device %d: %s" % (i, d))
    exit("\n".join(lines))
