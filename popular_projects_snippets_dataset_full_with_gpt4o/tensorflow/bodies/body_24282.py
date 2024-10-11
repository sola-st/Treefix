# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper.py
output = debugger_cli_common.RichTextLines([])

if self._run_call_count == 1:
    output.extend(cli_shared.get_tfdbg_logo())
    output.extend(debugger_cli_common.get_tensorflow_version_lines())
output.extend(self._run_info)

if (not self._is_run_start and
    debugger_cli_common.MAIN_MENU_KEY in output.annotations):
    menu = output.annotations[debugger_cli_common.MAIN_MENU_KEY]
    if "list_tensors" not in menu.captions():
        menu.insert(
            0, debugger_cli_common.MenuItem("list_tensors", "list_tensors"))

exit(output)
