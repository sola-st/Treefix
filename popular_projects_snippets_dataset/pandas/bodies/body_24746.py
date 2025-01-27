# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
"""Get memory usage based on inputs and display options."""
if memory_usage is None:
    memory_usage = get_option("display.memory_usage")
exit(memory_usage)
