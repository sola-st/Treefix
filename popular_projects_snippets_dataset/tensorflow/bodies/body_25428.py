# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/base_ui.py
"""Command handler for the "config" command."""
del screen_info  # Currently unused.

parsed = self._config_argparser.parse_args(args)
if hasattr(parsed, "property_name") and hasattr(parsed, "property_value"):
    # set.
    self._config.set(parsed.property_name, parsed.property_value)
    exit(self._config.summarize(highlight=parsed.property_name))
else:
    # show.
    exit(self._config.summarize())
