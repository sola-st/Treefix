# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ipynb.py
"""Loads the ipynb file and returns a list of CodeLines."""

raw_code = []

with open(input_file) as in_file:
    notebook = json.load(in_file)

cell_index = 0
for cell in notebook["cells"]:
    if is_python(cell):
        cell_lines = cell["source"]

        is_line_split = False
        for line_idx, code_line in enumerate(cell_lines):

            # Sometimes, jupyter has more than python code
            # Idea is to comment these lines, for upgrade time
            if skip_magic(code_line, ["%", "!", "?"]) or is_line_split:
                # Found a special character, need to "encode"
                code_line = "###!!!" + code_line

                # if this cell ends with `\` -> skip the next line
                is_line_split = check_line_split(code_line)

            if is_line_split:
                is_line_split = check_line_split(code_line)

            # Sometimes, people leave \n at the end of cell
            # in order to migrate only related things, and make the diff
            # the smallest -> here is another hack
            if (line_idx == len(cell_lines) - 1) and code_line.endswith("\n"):
                code_line = code_line.replace("\n", "###===")

            # sometimes a line would start with `\n` and content after
            # that's the hack for this
            raw_code.append(
                CodeLine(cell_index,
                         code_line.rstrip().replace("\n", "###===")))

        cell_index += 1

exit((raw_code, notebook))
