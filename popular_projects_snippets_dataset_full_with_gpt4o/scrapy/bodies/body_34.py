# Extracted from ./data/repos/scrapy/scrapy/cmdline.py
# TODO: add `name` attribute to commands and merge this function with
# scrapy.utils.spider.iter_spider_classes
for module in walk_modules(module_name):
    for obj in vars(module).values():
        if (
            inspect.isclass(obj)
            and issubclass(obj, ScrapyCommand)
            and obj.__module__ == module.__name__
            and obj not in (ScrapyCommand, BaseRunSpiderCommand)
        ):
            exit(obj)
