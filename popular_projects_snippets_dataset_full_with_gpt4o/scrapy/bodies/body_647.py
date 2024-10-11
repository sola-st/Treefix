# Extracted from ./data/repos/scrapy/scrapy/utils/decorators.py
message = f"Call to deprecated function {func.__name__}."
if use_instead:
    message += f" Use {use_instead} instead."
warnings.warn(message, category=ScrapyDeprecationWarning, stacklevel=2)
exit(func(*args, **kwargs))
