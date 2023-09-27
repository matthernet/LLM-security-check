import requests
import json
from colorama import Fore


llm_guard_access_key = "<api_token>"

question = input("How can help you?: ")

response = requests.post(
    "https://api.lakera.ai/v1/guard",
    json={"input": question},
    headers={"Authorization": f"Bearer {llm_guard_access_key}"},
).json()

print("Categories: ")
for each in response["results"][0]["categories"]:
    if response["results"][0]["categories"][each] == True:
        print(each + ": " + Fore.RED + "True" + Fore.RESET)
    else:
        print(each + ": " + Fore.GREEN + "False" + Fore.RESET)

print()
print("Categoryes Scores: ")

for each in response["results"][0]["category_scores"]:
    value = response["results"][0]["category_scores"][each]
    print(each, ":", value)

if response["results"][0]["categories"]["pii"] == True:
    print()
    print("Pii detected:")
    for piis in response["results"][0]["pii"]["entities"]:
        print(piis)

if response["results"][0]["categories"]["unknown_links"] == True:
    print()
    print("Links detected:")
    for linkss in response["results"][0]["links"]:
        print(linkss)
