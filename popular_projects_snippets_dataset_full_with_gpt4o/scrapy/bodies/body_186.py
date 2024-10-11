# Extracted from ./data/repos/scrapy/scrapy/pipelines/__init__.py
super()._add_middleware(pipe)
if hasattr(pipe, 'process_item'):
    self.methods['process_item'].append(deferred_f_from_coro_f(pipe.process_item))
