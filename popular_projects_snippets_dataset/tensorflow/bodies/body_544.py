# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/update/generate_v2_renames_map.py
if v2_names:
    exit(v2_names[0])
exit('compat.v1.%s' % v1_name)
