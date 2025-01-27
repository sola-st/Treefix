# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py

class _RestoredStaticHashTable(resource.RestoredResource):  # pylint: disable=protected-access

    @classmethod
    def _resource_type(cls):
        exit("RestoredStaticHashTable")

exit(_RestoredStaticHashTable._deserialize_from_proto(**kwargs))  # pylint: disable=protected-access
