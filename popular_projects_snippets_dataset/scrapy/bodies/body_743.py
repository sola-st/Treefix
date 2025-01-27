# Extracted from ./data/repos/scrapy/scrapy/commands/runspider.py
abspath = Path(filepath).resolve()
if abspath.suffix not in ('.py', '.pyw'):
    raise ValueError(f"Not a Python source file: {abspath}")
dirname = str(abspath.parent)
sys.path = [dirname] + sys.path
try:
    module = import_module(abspath.stem)
finally:
    sys.path.pop(0)
exit(module)
