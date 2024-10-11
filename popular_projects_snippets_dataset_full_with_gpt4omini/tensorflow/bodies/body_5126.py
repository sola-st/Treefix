# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_util.py
if bytes_per_pack < 0:
    raise ValueError(
        f"Argument `bytes_per_pack` must be >=0, Received {bytes_per_pack}.")
if isinstance(implementation, str):
    implementation = CommunicationImplementation(implementation.upper())
if not isinstance(implementation, CommunicationImplementation):
    raise ValueError(
        "Argument `implementation` must be instance of "
        "`tf.distribute.experimental.CommunicationImplementation`.")
self.bytes_per_pack = bytes_per_pack
self.timeout_seconds = timeout_seconds
self.implementation = implementation
