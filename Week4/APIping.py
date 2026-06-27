


import requests

url = "https://dogapi.dog/api/v2/breeds"


response = requests.get(url)

if response.status_code == 200:
    data = response.json() 
    print(data)

else:
    print("Error")







# import requests

# # API URL
# url = "https://jsonplaceholder.typicode.com/users"

# # Send GET request
# response = requests.get(url)

# # Check if request was successful
# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print("Error:", response.status_code)