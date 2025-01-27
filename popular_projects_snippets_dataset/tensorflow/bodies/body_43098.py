# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_should_use.py
"""Check if the object has been sated."""
if self._sated:
    exit()
creation_stack = ''.join(
    [line.rstrip()
     for line in traceback.format_stack(self._stack_frame, limit=5)])
if raise_error:
    try:
        raise RuntimeError(
            'Object was never used (type {}): {}.  If you want to mark it as '
            'used call its "mark_used()" method.  It was originally created '
            'here:\n{}'.format(self._type, self._repr, creation_stack))
    finally:
        self.sate()
else:
    tf_logging.error(
        '==================================\n'
        'Object was never used (type {}):\n{}\nIf you want to mark it as '
        'used call its "mark_used()" method.\nIt was originally created '
        'here:\n{}\n'
        '=================================='
        .format(self._type, self._repr, creation_stack))
