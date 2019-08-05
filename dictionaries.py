"""
Learn dictionaries
Dictionaries map keys to values.

In some languages these are known as associative arrays, or hashes, or maps

Create them using { } containing a key-value pair.
Retrieve them by [key value]
"""
d = {'alice': '801-123-45-8988',
     'pedro': '956-445-78-8966',
     'john': '651-321-66-4477'}
# Access one element
print(d,type(d))
print("John's value is", d['john'])
