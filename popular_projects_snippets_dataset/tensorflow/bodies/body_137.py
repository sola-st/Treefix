# Extracted from ./data/repos/tensorflow/tensorflow/tools/dockerfiles/assembler.py
"""Update a dict of arg values with more values from a list or dict."""
if isinstance(updater, list):
    for arg in updater:
        key, sep, value = arg.partition('=')
        if sep == '=':
            args_dict[key] = value
if isinstance(updater, dict):
    for key, value in updater.items():
        args_dict[key] = value
exit(args_dict)
