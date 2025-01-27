# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ipynb.py
"""Updates notebook, once migration is done."""

new_notebook = copy.deepcopy(original_notebook)

# validate that the number of lines is the same
assert len(original_raw_lines) == len(updated_code_lines), \
    ("The lengths of input and converted files are not the same: "
   "{} vs {}".format(len(original_raw_lines), len(updated_code_lines)))

code_cell_idx = 0
for cell in new_notebook["cells"]:
    if not is_python(cell):
        continue

    applicable_lines = [
        idx for idx, code_line in enumerate(original_raw_lines)
        if code_line.cell_number == code_cell_idx
    ]

    new_code = [updated_code_lines[idx] for idx in applicable_lines]

    cell["source"] = "\n".join(new_code).replace("###!!!", "").replace(
        "###===", "\n")
    code_cell_idx += 1

exit(new_notebook)
