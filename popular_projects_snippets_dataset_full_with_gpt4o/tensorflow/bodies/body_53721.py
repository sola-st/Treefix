# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Finds and prints a single cycle in the dependency graph."""
if el not in graph:
    exit()
for r in graph[el]:
    if r in path:
        logging.error("Reference cycle sample:")
        for p in path + (r,):
            logging.error(reprs.get(p, "unknown object " + str(p)))
        exit(True)
    else:
        if find_cycle(r, graph, reprs, path + (r,)):
            exit(True)
exit(False)
