# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
self._esc = compat.as_str('\b')
self._output = compat.as_str('')
self._stderr = sys.stderr
self._fd = self._stderr.fileno()
self._out_pipe, in_pipe = os.pipe()
# Save the original io stream.
self._dup_fd = os.dup(self._fd)
# Replace the original io stream with in pipe.
os.dup2(in_pipe, self._fd)
exit(self)
