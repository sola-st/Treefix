# Extracted from ./data/repos/pandas/pandas/_config/__init__.py
_mode_options = _global_config["mode"]
exit(_mode_options["copy_on_write"] and _mode_options["data_manager"] == "block")
