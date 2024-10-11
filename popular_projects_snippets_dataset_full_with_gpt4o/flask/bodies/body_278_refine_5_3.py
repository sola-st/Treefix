from flask import Flask, current_app # pragma: no cover
from werkzeug.routing import Rule # pragma: no cover
import click # pragma: no cover
from operator import attrgetter # pragma: no cover

app = Flask(__name__) # pragma: no cover
with app.app_context(): # pragma: no cover
    current_app.url_map = type('Mock', (object,), {'iter_rules': lambda: [Rule('/home', endpoint='home.index', methods={'GET', 'POST'}), Rule('/about', endpoint='about.index', methods={'GET'})]})() # pragma: no cover
all_methods = False # pragma: no cover
sort = 'rule' # pragma: no cover

from flask import Flask, current_app # pragma: no cover
from werkzeug.routing import Rule # pragma: no cover
import click # pragma: no cover
from operator import attrgetter # pragma: no cover

app = Flask(__name__) # pragma: no cover
app.config['DEBUG'] = True # pragma: no cover
ctx = app.app_context() # pragma: no cover
ctx.push() # pragma: no cover
current_app.url_map = type('Mock', (object,), {'iter_rules': lambda self: [Rule('/home', endpoint='home.index', methods={'GET', 'POST'}), Rule('/about', endpoint='about.index', methods={'GET'})]})() # pragma: no cover
click.echo = lambda x: print(x) # pragma: no cover
all_methods = False # pragma: no cover
sort = 'rule' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
"""Show all registered routes with endpoints and methods."""

rules = list(current_app.url_map.iter_rules())
_l_(22525)
if not rules:
    _l_(22528)

    click.echo("No routes were registered.")
    _l_(22526)
    exit()
    _l_(22527)

ignored_methods = set(() if all_methods else ("HEAD", "OPTIONS"))
_l_(22529)

if sort in ("endpoint", "rule"):
    _l_(22533)

    rules = sorted(rules, key=attrgetter(sort))
    _l_(22530)
elif sort == "methods":
    _l_(22532)

    rules = sorted(rules, key=lambda rule: sorted(rule.methods))  # type: ignore
    _l_(22531)  # type: ignore

rule_methods = [
    ", ".join(sorted(rule.methods - ignored_methods))  # type: ignore
    for rule in rules
]
_l_(22534)

headers = ("Endpoint", "Methods", "Rule")
_l_(22535)
widths = (
    max(len(rule.endpoint) for rule in rules),
    max(len(methods) for methods in rule_methods),
    max(len(rule.rule) for rule in rules),
)
_l_(22536)
widths = [max(len(h), w) for h, w in zip(headers, widths)]
_l_(22537)
row = "{{0:<{0}}}  {{1:<{1}}}  {{2:<{2}}}".format(*widths)
_l_(22538)

click.echo(row.format(*headers).strip())
_l_(22539)
click.echo(row.format(*("-" * width for width in widths)))
_l_(22540)

for rule, methods in zip(rules, rule_methods):
    _l_(22542)

    click.echo(row.format(rule.endpoint, methods, rule.rule).rstrip())
    _l_(22541)
