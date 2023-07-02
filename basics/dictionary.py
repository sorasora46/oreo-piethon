# dictionary = map (key and value)

json_data = {
  'data': {
    'name': 'sorrawit kwanja',
    'age': 20
  }
}

print(json_data)

# not safe
print(json_data['data']['name'])

# safe way to get the key
print(json_data.get('data'))

# get all the keys
print(json_data.keys())

# get all the values
print(json_data.values())

# get all key value pairs
print(json_data.items())

for data in json_data['data']:
    print(data)
  
# or
for key, value in json_data['data'].items():
    print(key)
    print(value)