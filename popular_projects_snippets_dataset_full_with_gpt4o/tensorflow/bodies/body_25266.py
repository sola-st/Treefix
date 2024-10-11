# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
"""Register a callable as a command handler.

    Args:
      prefix: Command prefix, i.e., the first word in a command, e.g.,
        "print" as in "print tensor_1".
      handler: A callable of the following signature:
          foo_handler(argv, screen_info=None),
        where argv is the argument vector (excluding the command prefix) and
          screen_info is a dictionary containing information about the screen,
          such as number of columns, e.g., {"cols": 100}.
        The callable should return:
          1) a RichTextLines object representing the screen output.

        The callable can also raise an exception of the type CommandLineExit,
        which if caught by the command-line interface, will lead to its exit.
        The exception can optionally carry an exit token of arbitrary type.
      help_info: A help string.
      prefix_aliases: Aliases for the command prefix, as a list of str. E.g.,
        shorthands for the command prefix: ["p", "pr"]

    Raises:
      ValueError: If
        1) the prefix is empty, or
        2) handler is not callable, or
        3) a handler is already registered for the prefix, or
        4) elements in prefix_aliases clash with existing aliases.
        5) help_info is not a str.
    """

if not prefix:
    raise ValueError("Empty command prefix")

if prefix in self._handlers:
    raise ValueError(
        "A handler is already registered for command prefix \"%s\"" % prefix)

# Make sure handler is callable.
if not callable(handler):
    raise ValueError("handler is not callable")

# Make sure that help info is a string.
if not isinstance(help_info, str):
    raise ValueError("help_info is not a str")

# Process prefix aliases.
if prefix_aliases:
    for alias in prefix_aliases:
        if self._resolve_prefix(alias):
            raise ValueError(
                "The prefix alias \"%s\" clashes with existing prefixes or "
                "aliases." % alias)
        self._alias_to_prefix[alias] = prefix

    self._prefix_to_aliases[prefix] = prefix_aliases

# Store handler.
self._handlers[prefix] = handler

# Store help info.
self._prefix_to_help[prefix] = help_info
