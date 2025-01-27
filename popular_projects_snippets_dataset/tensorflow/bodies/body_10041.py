# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Creates a parser that parse the command line arguments.

  Returns:
    A namespace parsed from command line arguments.
  """
parser = argparse_flags.ArgumentParser(
    description='saved_model_cli: Command-line interface for SavedModel',
    conflict_handler='resolve')
parser.add_argument('-v', '--version', action='version', version='0.1.0')

subparsers = parser.add_subparsers(
    title='commands', description='valid commands', help='additional help')

# show command
add_show_subparser(subparsers)

# run command
add_run_subparser(subparsers)

# scan command
add_scan_subparser(subparsers)

# tensorrt convert command
add_convert_subparser(subparsers)

# aot_compile_cpu command
add_aot_compile_cpu_subparser(subparsers)

# freeze_model command
add_freeze_model_subparser(subparsers)
exit(parser)
