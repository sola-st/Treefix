# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cluster_test.py
with self._coord.stop_on_exception():
    for i in range(num_calls):
        context.update_server_def(
            server_def=(self.server_def_s1_s2 if i %
                        2 == 0 else self.server_def_s1_s3))
