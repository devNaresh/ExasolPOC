import requests


query = """
mutation {{
  asileMutation(input:{{
    aisle: "testing_{}"
  }}){{
    aisle
    aisle
  }}
}}
"""

for i in range(200, 210):
    resp = requests.post('http://localhost:8000/graphql', json={'query': query.format(i)})
    print(resp.status_code)