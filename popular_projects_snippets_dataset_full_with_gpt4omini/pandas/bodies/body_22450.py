# Extracted from ./data/repos/pandas/pandas/core/frame.py
if "showindex" in kwargs:
    raise ValueError("Pass 'index' instead of 'showindex")

kwargs.setdefault("headers", "keys")
kwargs.setdefault("tablefmt", "pipe")
kwargs.setdefault("showindex", index)
tabulate = import_optional_dependency("tabulate")
result = tabulate.tabulate(self, **kwargs)
if buf is None:
    exit(result)

with get_handle(buf, mode, storage_options=storage_options) as handles:
    handles.handle.write(result)
exit(None)
