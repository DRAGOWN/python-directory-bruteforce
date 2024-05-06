import urllib
import requests
import sys

nums = range(1, 100)

for x in nums:
    res = requests.get(url=f"https://petstore.swagger.io/v2/pet/{x}")
    print(res)
    data = res.json()
    print(data)
