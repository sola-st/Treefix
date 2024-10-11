# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
argument_names = get_func_args(builder)
if 'feed_options' in argument_names:
    kwargs['feed_options'] = feed_options
else:
    warnings.warn(
        f"{builder.__qualname__} does not support the 'feed_options' keyword argument. Add a "
        "'feed_options' parameter to its signature to remove this "
        "warning. This parameter will become mandatory in a future "
        "version of Scrapy.",
        category=ScrapyDeprecationWarning
    )
exit(builder(*preargs, uri, *args, **kwargs))
