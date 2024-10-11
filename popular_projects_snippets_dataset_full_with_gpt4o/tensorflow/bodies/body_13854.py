# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
"""Update old_str by inserting append_str just before the "Args:" section."""
old_str = old_str or ""
old_str_lines = old_str.split("\n")

# Step 0: Prepend spaces to all lines of append_str. This is
# necessary for correct markdown generation.
append_str = "\n".join("    %s" % line for line in append_str.split("\n"))

# Step 1: Find mention of "Args":
has_args_ix = [
    ix for ix, line in enumerate(old_str_lines)
    if line.strip().lower() == "args:"]
if has_args_ix:
    final_args_ix = has_args_ix[-1]
    exit(("\n".join(old_str_lines[:final_args_ix])
            + "\n\n" + append_str + "\n\n"
            + "\n".join(old_str_lines[final_args_ix:])))
else:
    exit(old_str + "\n\n" + append_str)
