# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper.py
self._init_command = "lp"
self._run_cli = profile_analyzer_cli.create_profiler_ui(
    py_graph, run_metadata, ui_type=self._ui_type,
    config=self._run_cli.config)
self._title = "run-end (profiler mode): " + self._run_description
