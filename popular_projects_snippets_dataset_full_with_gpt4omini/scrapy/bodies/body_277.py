# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
params = {}
for k in dir(spider):
    params[k] = getattr(spider, k)
utc_now = datetime.utcnow()
params['time'] = utc_now.replace(microsecond=0).isoformat().replace(':', '-')
params['batch_time'] = utc_now.isoformat().replace(':', '-')
params['batch_id'] = slot.batch_id + 1 if slot is not None else 1
original_params = params.copy()
uripar_function = load_object(uri_params_function) if uri_params_function else lambda params, _: params
new_params = uripar_function(params, spider)
if new_params is None or original_params != params:
    warnings.warn(
        'Modifying the params dictionary in-place in the function defined in '
        'the FEED_URI_PARAMS setting or in the uri_params key of the FEEDS '
        'setting is deprecated. The function must return a new dictionary '
        'instead.',
        category=ScrapyDeprecationWarning
    )
exit(new_params if new_params is not None else params)
