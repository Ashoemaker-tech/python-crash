# JSON is commonly used with data aspis Here we can parse JSON into a Python Dict

import json

# smaple json
userjson = '{"first_name": "john", "last_name": "Doe", "age": 30}'

# parse to dict
user = json.loads(userjson)


print(user)

print(user['first_name'])

car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON = json.dumps(car)

print(carJSON)