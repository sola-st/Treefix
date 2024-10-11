# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
self._stderr.write(self._esc)
self._stderr.flush()
self.read()
os.close(self._out_pipe)
# Restore the original io stream.
os.dup2(self._dup_fd, self._fd)
