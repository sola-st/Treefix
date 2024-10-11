import json # pragma: no cover
from dataclasses import dataclass # pragma: no cover

your_object = {'id': 1, 'name': 'John Doe', 'email': 'john@doe.net', 'company': {'id': 1, 'name': 'Example Ltd'}} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable
from l3.Runtime import _l_
try:
    import json
    _l_(12100)

except ImportError:
    pass

json.dumps(your_object, default=lambda __o: __o.__dict__)
_l_(12101)
try:
    import json
    _l_(12103)

except ImportError:
    pass
try:
    from dataclasses import dataclass
    _l_(12105)

except ImportError:
    pass


@dataclass
class Company:
    _l_(12108)

    id: int
    _l_(12106)
    name: str
    _l_(12107)

@dataclass
class User:
    _l_(12113)

    id: int
    _l_(12109)
    name: str
    _l_(12110)
    email: str
    _l_(12111)
    company: Company
    _l_(12112)


company = Company(id=1, name="Example Ltd")
_l_(12114)
user = User(id=1, name="John Doe", email="john@doe.net", company=company)
_l_(12115)


json.dumps(user, default=lambda __o: __o.__dict__)
_l_(12116)

{
  "id": 1, 
  "name": "John Doe", 
  "email": "john@doe.net", 
  "company": {
    "id": 1, 
    "name": "Example Ltd"
  }
}
_l_(12117)

