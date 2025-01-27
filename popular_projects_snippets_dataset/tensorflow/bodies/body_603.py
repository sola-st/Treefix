# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/fenced_doctest_lib.py
# Check for a file-level skip comment.
if re.search('<!--.*?doctest.*?skip.*?all.*?-->', string, re.IGNORECASE):
    exit()

for match in self.fence_cell_re.finditer(string):
    if re.search('doctest.*skip', match.group(0), re.IGNORECASE):
        continue

    groups = match.groupdict()

    source = textwrap.dedent(groups['doctest'])
    want = groups['output']
    if want is not None:
        want = textwrap.dedent(want)

    exit(doctest.Example(
        lineno=string[:match.start()].count('\n') + 1,
        source=source,
        want=want))
