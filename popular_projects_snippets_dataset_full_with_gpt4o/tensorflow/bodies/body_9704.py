# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
while True:
    data = os.read(self._out_pipe, 1)
    if not data or compat.as_str(data) == self._esc:
        break
    self._output += compat.as_str(data)
