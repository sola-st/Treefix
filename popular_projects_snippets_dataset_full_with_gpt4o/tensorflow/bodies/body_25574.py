# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/profile_analyzer_cli.py
"""Determine the maximum column widths for each data list.

    Args:
      profile_data: list of ProfileDatum objects.

    Returns:
      List of column widths in the same order as columns in data.
    """
num_columns = len(profile_data.column_names())
widths = [len(column_name) for column_name in profile_data.column_names()]
for row in range(profile_data.row_count()):
    for col in range(num_columns):
        widths[col] = max(
            widths[col], len(str(profile_data.row_values(row)[col])) + 2)
exit(widths)
