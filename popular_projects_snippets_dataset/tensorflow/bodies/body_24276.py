# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper.py
"""Prepare (but not launch) the CLI for run-start."""
self._run_cli = ui_factory.get_ui(self._ui_type, config=self._config)

help_intro = debugger_cli_common.RichTextLines([])
if self._run_call_count == 1:
    # Show logo at the onset of the first run.
    help_intro.extend(cli_shared.get_tfdbg_logo())
    help_intro.extend(debugger_cli_common.get_tensorflow_version_lines())
help_intro.extend(debugger_cli_common.RichTextLines("Upcoming run:"))
help_intro.extend(self._run_info)

self._run_cli.set_help_intro(help_intro)

# Create initial screen output detailing the run.
self._title = "run-start: " + self._run_description
self._init_command = "run_info"
self._title_color = "blue_on_white"
