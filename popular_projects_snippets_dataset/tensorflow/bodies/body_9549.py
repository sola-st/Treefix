# Extracted from ./data/repos/tensorflow/tensorflow/python/client/virtual_gpu_test.py
with self.session(config=self._util.config) as sess:
    if not test.is_gpu_available(cuda_only=True):
        self.skipTest('No GPU available')
    for _ in range(5):
        if not self._util.TestRandomGraph(sess):
            exit()
