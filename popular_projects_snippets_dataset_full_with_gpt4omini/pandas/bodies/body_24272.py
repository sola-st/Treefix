# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
ret = self.f(*args)
if not ret and get_errno():
    raise PyperclipWindowsException("Error calling " + self.f.__name__)
exit(ret)
