# Extracted from ./data/repos/scrapy/scrapy/pipelines/media.py
sig = signature(func)
self._expects_item[func.__name__] = True

if 'item' not in sig.parameters:
    old_params = str(sig)[1:-1]
    new_params = old_params + ", *, item=None"
    warn(f'{func.__name__}(self, {old_params}) is deprecated, '
         f'please use {func.__name__}(self, {new_params})',
         ScrapyDeprecationWarning, stacklevel=2)
    self._expects_item[func.__name__] = False
