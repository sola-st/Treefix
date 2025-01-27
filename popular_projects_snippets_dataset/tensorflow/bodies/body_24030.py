# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
with ops.name_scope("x", skip_on_eager=False) as ns:
    ns = "/".join(ns.split("/")[:-2])
    exit(ns + "/" if ns else "")
