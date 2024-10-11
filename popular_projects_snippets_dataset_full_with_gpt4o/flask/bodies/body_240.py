# Extracted from ./data/repos/flask/src/flask/json/tag.py
self.tags: t.Dict[str, JSONTag] = {}
self.order: t.List[JSONTag] = []

for cls in self.default_tags:
    self.register(cls)
