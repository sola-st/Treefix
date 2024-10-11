# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper.py
"""Launch the interactive command-line interface.

    Returns:
      The OnRunStartResponse specified by the user using the "run" command.
    """

self._register_this_run_info(self._run_cli)
response = self._run_cli.run_ui(
    init_command=self._init_command,
    title=self._title,
    title_color=self._title_color)

exit(response)
