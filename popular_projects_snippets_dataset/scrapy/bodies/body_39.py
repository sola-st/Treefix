# Extracted from ./data/repos/scrapy/scrapy/cmdline.py
version = scrapy.__version__
if inproject:
    print(f"Scrapy {version} - active project: {settings['BOT_NAME']}\n")

else:
    print(f"Scrapy {version} - no active project\n")
