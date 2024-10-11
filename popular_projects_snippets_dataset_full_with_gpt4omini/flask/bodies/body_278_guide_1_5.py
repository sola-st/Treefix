from flask import Flask, current_app # pragma: no cover
import click # pragma: no cover
from operator import attrgetter # pragma: no cover

app = Flask(__name__) # pragma: no cover
app.add_url_rule('/test', endpoint='test_endpoint', view_func=lambda: 'Test Function') # pragma: no cover
with app.app_context(): # pragma: no cover
    current_app = app # pragma: no cover
    all_methods = False # pragma: no cover
    sort = 'endpoint' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
"""Show all registered routes with endpoints and methods."""

rules = list(current_app.url_map.iter_rules())
_l_(4688)
if not rules:
    _l_(4691)

    click.echo("No routes were registered.")
    _l_(4689)
    exit()
    _l_(4690)

ignored_methods = set(() if all_methods else ("HEAD", "OPTIONS"))
_l_(4692)

if sort in ("endpoint", "rule"):
    _l_(4696)

    rules = sorted(rules, key=attrgetter(sort))
    _l_(4693)
elif sort == "methods":
    _l_(4695)

    rules = sorted(rules, key=lambda rule: sorted(rule.methods))  # type: ignore
    _l_(4694)  # type: ignore

rule_methods = [
    ", ".join(sorted(rule.methods - ignored_methods))  # type: ignore
    for rule in rules
]
_l_(4697)

headers = ("Endpoint", "Methods", "Rule")
_l_(4698)
widths = (
    max(len(rule.endpoint) for rule in rules),
    max(len(methods) for methods in rule_methods),
    max(len(rule.rule) for rule in rules),
)
_l_(4699)
widths = [max(len(h), w) for h, w in zip(headers, widths)]
_l_(4700)
row = "{{0:<{0}}}  {{1:<{1}}}  {{2:<{2}}}".format(*widths)
_l_(4701)

click.echo(row.format(*headers).strip())
_l_(4702)
click.echo(row.format(*("-" * width for width in widths)))
_l_(4703)

for rule, methods in zip(rules, rule_methods):
    _l_(4705)

    click.echo(row.format(rule.endpoint, methods, rule.rule).rstrip())
    _l_(4704)
