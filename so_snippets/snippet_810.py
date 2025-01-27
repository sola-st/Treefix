# Extracted from https://stackoverflow.com/questions/26672077/django-model-vs-model-objects-create
class Subject(models.Model):
   subject_id = models.PositiveIntegerField(primary_key=True, db_column='subject_id')
   name = models.CharField(max_length=255)
   max_marks = models.PositiveIntegerField()

physics = Subject(subject_id=1, name='Physics', max_marks=100)
physics.save()
math = Subject(subject_id=1, name='Math', max_marks=50)  # Case of update
math.save()

Subject.objects.all().values()

Subject.objects.create(subject_id=1, name='Chemistry', max_marks=100)
IntegrityError: UNIQUE constraint failed: m****t.subject_id

def create(self, **kwargs):
    """
    Create a new object with the given kwargs, saving it to the database
    and returning the created object.
    """
    obj = self.model(**kwargs)
    self._for_write = True
    obj.save(force_insert=True, using=self.db)
    return obj

