# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cluster_test.py
for _ in range(30):
    with self._coord.stop_on_exception():
        context.update_server_def(self.server_def_s1_s2)
