# Extracted from ./data/repos/scrapy/scrapy/commands/genspider.py
if opts.list:
    self._list_templates()
    exit()
if opts.dump:
    template_file = self._find_template(opts.dump)
    if template_file:
        print(template_file.read_text(encoding="utf-8"))
    exit()
if len(args) != 2:
    raise UsageError()

name, url = args[0:2]
domain = extract_domain(url)
module = sanitize_module_name(name)

if self.settings.get('BOT_NAME') == module:
    print("Cannot create a spider with the same name as your project")
    exit()

if not opts.force and self._spider_exists(name):
    exit()

template_file = self._find_template(opts.template)
if template_file:
    self._genspider(module, name, domain, opts.template, template_file)
    if opts.edit:
        self.exitcode = os.system(f'scrapy edit "{name}"')
