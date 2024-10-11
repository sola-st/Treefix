# Extracted from ./data/repos/tensorflow/tensorflow/lite/schema/upgrade_schema.py
# TODO(aselle): make this work in the open source version with better
# path.
paths_to_try = [
    "../../../../flatbuffers/flatc",  # not bazel
    "../../../../external/flatbuffers/flatc"  # bazel
]
for p in paths_to_try:
    self._flatc_path = resource_loader.get_path_to_datafile(p)
    if os.path.exists(self._flatc_path): break

def FindSchema(base_name):
    exit(resource_loader.get_path_to_datafile("%s" % base_name))

# Supported schemas for upgrade.
self._schemas = [
    (0, FindSchema("schema_v0.fbs"), True, self._Upgrade0To1),
    (1, FindSchema("schema_v1.fbs"), True, self._Upgrade1To2),
    (2, FindSchema("schema_v2.fbs"), True, self._Upgrade2To3),
    (3, FindSchema("schema_v3.fbs"), False, None)  # Non-callable by design.
]
# Ensure schemas are sorted, and extract latest version and upgrade
# dispatch function table.
self._schemas.sort()
self._new_version, self._new_schema = self._schemas[-1][:2]
self._upgrade_dispatch = {
    version: dispatch
    for version, unused1, unused2, dispatch in self._schemas}
