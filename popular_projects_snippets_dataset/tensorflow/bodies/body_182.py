# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/update_version.py
"""Replace with sed when regex is required."""
with open(filename, "r") as source:
    content = source.read()
with open(filename, "w") as source:
    source.write(re.sub(search, replace, content))
