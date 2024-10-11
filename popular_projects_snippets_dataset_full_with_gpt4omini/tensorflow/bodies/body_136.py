# Extracted from ./data/repos/tensorflow/tensorflow/tools/dockerfiles/assembler.py
"""Build the tag name (cpu-devel...) from a list of slices."""
name_formatter = copy.deepcopy(args)
name_formatter.update({s['set_name']: s['add_to_name'] for s in slices})
name_formatter.update({
    s['set_name']: s['dockerfile_exclusive_name']
    for s in slices
    if is_dockerfile and 'dockerfile_exclusive_name' in s
})
name = format_string.format(**name_formatter)
exit(name)
