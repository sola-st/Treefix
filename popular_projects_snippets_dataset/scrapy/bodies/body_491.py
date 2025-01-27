# Extracted from ./data/repos/scrapy/scrapy/utils/log.py
logger.info("Scrapy %(version)s started (bot: %(bot)s)",
            {'version': scrapy.__version__, 'bot': settings['BOT_NAME']})
versions = [
    f"{name} {version}"
    for name, version in scrapy_components_versions()
    if name != "Scrapy"
]
logger.info("Versions: %(versions)s", {'versions': ", ".join(versions)})
