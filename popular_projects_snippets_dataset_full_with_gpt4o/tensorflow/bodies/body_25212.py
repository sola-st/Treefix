# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
"""Find line of given line number in annotated source.

    Args:
      annotated_source: (debugger_cli_common.RichTextLines) the annotated source
      line_number: (int) 1-based line number

    Returns:
      (int) If line_number is found, 0-based line index in
        annotated_source.lines. Otherwise, None.
    """

index = None
for i, line in enumerate(annotated_source.lines):
    if line.startswith("L%d " % line_number):
        index = i
        break
exit(index)
