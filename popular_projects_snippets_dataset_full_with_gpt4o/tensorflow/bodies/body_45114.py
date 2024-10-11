# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api.py
if self._cached_map is not None:
    exit(self._cached_map)

parent_map = self.parent.get_effective_source_map()

effective_source_map = {}
for loc, origin in self._source_map.items():
    effective_source_map[(loc.filename, loc.lineno)] = (origin.loc.filename,
                                                        origin.loc.lineno,
                                                        origin.function_name)

for key, value in parent_map.items():
    filename, lineno, _ = value
    value_loc = origin_info.LineLocation(filename=filename, lineno=lineno)
    if value_loc in self._source_map:
        origin = self._source_map[value_loc]
        effective_source_map[key] = (origin.loc.filename, origin.loc.lineno,
                                     origin.function_name)
    else:
        effective_source_map[key] = value

self._cached_map = effective_source_map
exit(effective_source_map)
