# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
"""Handles a command by dispatching it to a registered command handler.

    Args:
      prefix: Command prefix, as a str, e.g., "print".
      argv: Command argument vector, excluding the command prefix, represented
        as a list of str, e.g.,
        ["tensor_1"]
      screen_info: A dictionary containing screen info, e.g., {"cols": 100}.

    Returns:
      An instance of RichTextLines or None. If any exception is caught during
      the invocation of the command handler, the RichTextLines will wrap the
      error type and message.

    Raises:
      ValueError: If
        1) prefix is empty, or
        2) no command handler is registered for the command prefix, or
        3) the handler is found for the prefix, but it fails to return a
          RichTextLines or raise any exception.
      CommandLineExit:
        If the command handler raises this type of exception, this method will
        simply pass it along.
    """
if not prefix:
    raise ValueError("Prefix is empty")

resolved_prefix = self._resolve_prefix(prefix)
if not resolved_prefix:
    raise ValueError("No handler is registered for command prefix \"%s\"" %
                     prefix)

handler = self._handlers[resolved_prefix]
try:
    output = handler(argv, screen_info=screen_info)
except CommandLineExit as e:
    raise e
except SystemExit as e:
    # Special case for syntax errors caught by argparse.
    lines = ["Syntax error for command: %s" % prefix,
             "For help, do \"help %s\"" % prefix]
    output = RichTextLines(lines)

except BaseException as e:  # pylint: disable=broad-except
    lines = ["Error occurred during handling of command: %s %s:" %
             (resolved_prefix, " ".join(argv)), "%s: %s" % (type(e), str(e))]

    # Include traceback of the exception.
    lines.append("")
    lines.extend(traceback.format_exc().split("\n"))

    output = RichTextLines(lines)

if not isinstance(output, RichTextLines) and output is not None:
    raise ValueError(
        "Return value from command handler %s is not None or a RichTextLines "
        "instance" % str(handler))

exit(output)
