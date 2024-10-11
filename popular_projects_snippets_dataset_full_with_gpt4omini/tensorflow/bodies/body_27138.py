# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/snapshot_ft_test.py
cluster, ds = self.setup()
cluster.restart_dispatcher()
with self.assertRaisesOpError("is already started or completed"):
    distributed_save_op.distributed_save(
        ds, self._path, cluster.dispatcher_address()
    )
