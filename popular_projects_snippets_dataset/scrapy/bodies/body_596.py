# Extracted from ./data/repos/scrapy/scrapy/utils/template.py
path_obj = Path(path)
raw = path_obj.read_text('utf8')

content = string.Template(raw).substitute(**kwargs)

render_path = path_obj.with_suffix('') if path_obj.suffix == '.tmpl' else path_obj

if path_obj.suffix == '.tmpl':
    path_obj.rename(render_path)

render_path.write_text(content, 'utf8')
