from pathlib import Path # pragma: no cover

self = type('Mock', (object,), {'templates_dir': 'path/to/templates'})() # pragma: no cover
Path = Path # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/commands/genspider.py
from l3.Runtime import _l_
print("Available templates:")
_l_(5416)
for file in sorted(Path(self.templates_dir).iterdir()):
    _l_(5419)

    if file.suffix == '.tmpl':
        _l_(5418)

        print(f"  {file.stem}")
        _l_(5417)
