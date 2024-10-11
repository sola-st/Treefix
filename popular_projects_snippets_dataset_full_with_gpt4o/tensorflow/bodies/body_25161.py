# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
"""Check RichTextLines output from invalid/erroneous commands.

  Args:
    tst: A test_util.TensorFlowTestCase instance.
    out: The RichTextLines object to be checked.
    command_prefix: The command prefix of the command that caused the error.
    args: The arguments (excluding prefix) of the command that caused the error.
  """

tst.assertGreater(len(out.lines), 2)
tst.assertStartsWith(out.lines[0],
                     "Error occurred during handling of command: %s %s" %
                     (command_prefix, " ".join(args)))
