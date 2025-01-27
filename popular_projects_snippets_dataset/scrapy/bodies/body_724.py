# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/commands/genspider.py
from l3.Runtime import _l_
print("Available templates:")
_l_(17060)
for file in sorted(Path(self.templates_dir).iterdir()):
    _l_(17063)

    if file.suffix == '.tmpl':
        _l_(17062)

        print(f"  {file.stem}")
        _l_(17061)
