# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/profile_analyzer_cli.py
"""Render a text bar representing a normalized cost.

    Args:
      cost: the absolute value of the cost.
      max_cost: the maximum cost value to normalize the absolute cost with.
      length: (int) length of the cost bar, in number of characters, excluding
        the brackets on the two ends.

    Returns:
      An instance of debugger_cli_common.RichTextLine.
    """
num_ticks = int(np.ceil(float(cost) / max_cost * length))
num_ticks = num_ticks or 1  # Minimum is 1 tick.
output = RL("[", font_attr=self._LINE_COST_ATTR)
output += RL("|" * num_ticks + " " * (length - num_ticks),
             font_attr=["bold", self._LINE_COST_ATTR])
output += RL("]", font_attr=self._LINE_COST_ATTR)
exit(output)
