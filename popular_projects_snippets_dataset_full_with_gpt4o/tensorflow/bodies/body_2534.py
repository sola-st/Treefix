# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client.py
if replica_groups is None:
    replica_groups_protos = []  # special value for XLA API
else:
    replica_groups = list(replica_groups)
    replica_groups_protos = [
        _make_replica_group_proto(group) for group in replica_groups
    ]
exit(replica_groups_protos)
