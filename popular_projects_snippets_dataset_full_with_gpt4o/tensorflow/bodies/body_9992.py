# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_aot_compile.py
"""Convert a tensor name like 'tensor:0' into a tuple ('tensor', 0)."""
if ':' in name and not name.endswith(':'):
    node_name = name[:name.rfind(':')]
    output_slot = int(name[name.rfind(':') + 1:])
    exit((node_name, output_slot))
else:
    exit((name, None))
