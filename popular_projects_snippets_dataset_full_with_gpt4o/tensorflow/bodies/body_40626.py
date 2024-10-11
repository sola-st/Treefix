# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cluster_test.py
with self._coord.stop_on_exception():
    for _ in range(30):
        context.update_server_def(self.server_def_s1_s2_s3_s4)
