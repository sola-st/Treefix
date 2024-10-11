# Extracted from https://stackoverflow.com/questions/8609192/what-is-the-difference-between-null-true-and-blank-true-in-django
class TestModel(models.Model):
    field1 = models.CharField(max_length=100, null=True)
    field2 = models.CharField(max_length=100, blank=True)   # it's not a correct way
    field3 = models.CharField(max_length=100, null=True, blank=True)

CREATE TABLE TestModel (
     `id`        INT(10)        NOT     NULL      AUTO_INCREMENT,

     `field1`    VARCHAR(100)   NULL    DEFAULT   NULL,
     `field2`    VARCHAR(100)   NOT     NULL,
     `field3`    VARCHAR(100)   NULL    DEFAULT   NULL,
)

db:   db   field is accepts null value
form: form field is `required`

NB: DB IS ACCEPTS NULL VALUE, BUT FORM FIELD IS REQUIRED. SO FORM IS 
SUBMITTED WHEN THIS FIELD HAVE SOME VALUE. it's good.

db:   db   field is not accepts null value
form: form field is `optional`

NB: FORM IS VALID WITHOUT ANY VALUE, BUT DB IS NOT ACCEPTS NULL VALUE.
SO THE FORM IS SUBMITTED WITHOUT ANY VALUE THEN BOOM. it's worst.

db:   db   field is accepts null value
form: form field is `optional`

NB: HERE FORM FIELD IS OPTIONAL & FORM IS VALID WITHOUT ANY VALUE 
& DB ALSO ACCEPTS NULL VALUE. SO, IT'S BEST TO USE `null=True && blank=True`

