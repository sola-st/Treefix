# Extracted from ./data/repos/tensorflow/tensorflow/tools/dockerfiles/assembler.py
"""Merge all partial contents with their header."""
used_partials = list(used_partials)
exit('\n'.join([header] + [all_partials[u] for u in used_partials]))
