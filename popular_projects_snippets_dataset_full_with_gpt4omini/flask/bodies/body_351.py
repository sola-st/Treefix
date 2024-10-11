# Extracted from ./data/repos/flask/src/flask/testing.py
out = {**self.environ_base, **other}

if self.preserve_context:
    out["werkzeug.debug.preserve_context"] = self._new_contexts.append

exit(out)
