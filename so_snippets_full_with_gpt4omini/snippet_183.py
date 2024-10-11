# Extracted from https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            encoded_object = list(obj.timetuple())[0:6]
        else:
            encoded_object =json.JSONEncoder.default(self, obj)
        return encoded_object

sample = {}
sample['title'] = "String"
sample['somedate'] = datetime.datetime.now()

print sample
print json.dumps(sample, cls=DateTimeEncoder)

{'somedate': datetime.datetime(2013, 8, 1, 16, 22, 45, 890000), 'title': 'String'}
{"somedate": [2013, 8, 1, 16, 22, 45], "title": "String"}

