# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver.py
address = compat.as_text(self._cloud_tpu_client.get_local_ip())
self._server = server_lib.Server({'local': ['0.0.0.0:0']},
                                 protocol='grpc',
                                 config=None,
                                 start=True)
# self._server.target is of the form: grpc://ipaddress:port
target = compat.as_bytes(self._server.target)
splits = target.split(compat.as_bytes(':'))
assert len(splits) == 3, self._server.target
assert splits[0] == compat.as_bytes('grpc'), self._server.target
self._coordinator_port = compat.as_text(splits[2])
self._coordinator_address = '%s:%s' % (
    address, compat.as_text(self._coordinator_port))
