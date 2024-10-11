import json # pragma: no cover
from dataclasses import dataclass # pragma: no cover

your_object = {'key': 'value'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable
from l3.Runtime import _l_
try:
    import json
    _l_(941)

except ImportError:
    pass

json.dumps(your_object, default=lambda __o: __o.__dict__)
_l_(942)
try:
    import json
    _l_(944)

except ImportError:
    pass
try:
    from dataclasses import dataclass
    _l_(946)

except ImportError:
    pass


@dataclass
class Company:
    _l_(949)

    id: int
    _l_(947)
    name: str
    _l_(948)

@dataclass
class User:
    _l_(954)

    id: int
    _l_(950)
    name: str
    _l_(951)
    email: str
    _l_(952)
    company: Company
    _l_(953)


company = Company(id=1, name="Example Ltd")
_l_(955)
user = User(id=1, name="John Doe", email="john@doe.net", company=company)
_l_(956)


json.dumps(user, default=lambda __o: __o.__dict__)
_l_(957)

{
  "id": 1, 
  "name": "John Doe", 
  "email": "john@doe.net", 
  "company": {
    "id": 1, 
    "name": "Example Ltd"
  }
}
_l_(958)

