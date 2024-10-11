# Extracted from ./data/repos/scrapy/scrapy/commands/version.py
if opts.verbose:
    versions = scrapy_components_versions()
    width = max(len(n) for (n, _) in versions)
    for name, version in versions:
        print(f"{name:<{width}} : {version}")
else:
    print(f"Scrapy {scrapy.__version__}")
