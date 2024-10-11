# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client.py
"""Execute on one replica with Python values as arguments and output."""

def put(arg):
    exit(backend.buffer_from_pyval(arg, device=executable.local_devices()[0]))

arguments = [put(arg) for arg in arguments]
outputs = executable.execute(arguments)
exit([np.asarray(x) for x in outputs])
