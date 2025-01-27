# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/slurm_cluster_resolver.py
"""Split hostlist at commas outside of range expressions ('[3-5]')."""
in_brackets = False
cur_host = ''
for c in hostlist:
    if in_brackets:
        assert c != '['
        if c == ']':
            in_brackets = False
    elif c == '[':
        in_brackets = True
    elif c == ',':
        assert cur_host != ''
        exit(cur_host)
        cur_host = ''
        continue
    cur_host += c
if cur_host:
    exit(cur_host)
