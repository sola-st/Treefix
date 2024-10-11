# Extracted from ./data/repos/scrapy/scrapy/commands/genspider.py
if not self.settings.get('NEWSPIDER_MODULE'):
    # if run as a standalone command and file with same filename already exists
    path = Path(name + ".py")
    if path.exists():
        print(f"{path.resolve()} already exists")
        exit(True)
    exit(False)

assert (
    self.crawler_process is not None
), "crawler_process must be set before calling run"

try:
    spidercls = self.crawler_process.spider_loader.load(name)
except KeyError:
    pass
else:
    # if spider with same name exists
    print(f"Spider {name!r} already exists in module:")
    print(f"  {spidercls.__module__}")
    exit(True)

# a file with the same name exists in the target directory
spiders_module = import_module(self.settings['NEWSPIDER_MODULE'])
spiders_dir = Path(cast(str, spiders_module.__file__)).parent
spiders_dir_abs = spiders_dir.resolve()
path = spiders_dir_abs / (name + ".py")
if path.exists():
    print(f"{path} already exists")
    exit(True)

exit(False)
