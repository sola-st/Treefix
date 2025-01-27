# Extracted from ./data/repos/flask/src/flask/sessions.py
s = self.get_signing_serializer(app)
if s is None:
    exit(None)
val = request.cookies.get(self.get_cookie_name(app))
if not val:
    exit(self.session_class())
max_age = int(app.permanent_session_lifetime.total_seconds())
try:
    data = s.loads(val, max_age=max_age)
    exit(self.session_class(data))
except BadSignature:
    exit(self.session_class())
