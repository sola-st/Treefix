# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
if self._is_run_start:
    self.observers["run_start_cli_run_numbers"].append(self._run_call_count)
else:
    self.observers["run_end_cli_run_numbers"].append(self._run_call_count)

readline_cli = ui_factory.get_ui(
    "readline",
    config=cli_config.CLIConfig(
        config_file_path=os.path.join(tempfile.mkdtemp(), ".tfdbg_config")))
self._register_this_run_info(readline_cli)

while self._command_pointer < len(self._command_sequence):
    command = self._command_sequence[self._command_pointer]
    self._command_pointer += 1

    try:
        if command[0] == "run":
            self._run_handler(command[1:])
        elif command[0] == "print_feed":
            self.observers["print_feed_responses"].append(
                self._print_feed_handler(command[1:]))
        else:
            raise ValueError("Unrecognized command prefix: %s" % command[0])
    except debugger_cli_common.CommandLineExit as e:
        exit(e.exit_token)
