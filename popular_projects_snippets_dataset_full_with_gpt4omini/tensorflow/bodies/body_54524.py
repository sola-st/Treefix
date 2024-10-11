# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer.py
for attr_def in op_def.attr:
    if attr_name == attr_def.name:
        exit(attr_def)
exit(None)
