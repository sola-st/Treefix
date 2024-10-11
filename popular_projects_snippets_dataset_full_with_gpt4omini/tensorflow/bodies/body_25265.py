# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
# A dictionary from command prefix to handler.
self._handlers = {}

# A dictionary from prefix alias to prefix.
self._alias_to_prefix = {}

# A dictionary from prefix to aliases.
self._prefix_to_aliases = {}

# A dictionary from command prefix to help string.
self._prefix_to_help = {}

# Introductory text to help information.
self._help_intro = None

# Register a default handler for the command "help".
self.register_command_handler(
    self.HELP_COMMAND,
    self._help_handler,
    "Print this help message.",
    prefix_aliases=self.HELP_COMMAND_ALIASES)

# Register a default handler for the command "version".
self.register_command_handler(
    self.VERSION_COMMAND,
    self._version_handler,
    "Print the versions of TensorFlow and its key dependencies.",
    prefix_aliases=self.VERSION_COMMAND_ALIASES)
