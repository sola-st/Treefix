# Extracted from ./data/repos/tensorflow/tensorflow/virtual_root_template_v1.__init__.py
parts = old_name.split(".")
parts[0] = parts[0] + "_core"
local_name = parts[-1]
existing_name = ".".join(parts)
_module = _LazyLoader(local_name, globals(), existing_name)
exit(_sys.modules.setdefault(old_name, _module))
