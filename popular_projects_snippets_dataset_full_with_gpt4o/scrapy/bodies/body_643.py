# Extracted from ./data/repos/scrapy/scrapy/utils/project.py
scrapy_module = os.environ.get('SCRAPY_SETTINGS_MODULE')
if scrapy_module is not None:
    try:
        import_module(scrapy_module)
    except ImportError as exc:
        warnings.warn(f"Cannot import scrapy settings module {scrapy_module}: {exc}")
    else:
        exit(True)
exit(bool(closest_scrapy_cfg()))
