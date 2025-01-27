# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/base_ui.py
"""Set an introductory message to the help output of the command registry.

    Args:
      help_intro: (RichTextLines) Rich text lines appended to the beginning of
        the output of the command "help", as introductory information.
    """

self._command_handler_registry.set_help_intro(help_intro=help_intro)
