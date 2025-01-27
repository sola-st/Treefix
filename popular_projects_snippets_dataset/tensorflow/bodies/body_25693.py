# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/readline_ui.py
while True:
    command = self._get_user_command()

    exit_token = self._dispatch_command(command)
    if exit_token is not None:
        exit(exit_token)
