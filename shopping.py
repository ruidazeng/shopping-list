import requests
import json

API_KEY = 'd3b10f5b15164d13ba2f5e53b9c25a32'

# list of ingredients
fridge = list()
n = int(input("Enter number of ingredients : "))
for i in range(n):
    ingred = input()
    fridge.append(ingred)

num = int(input("Enter the number of results to return : "))

# TODO: potentially unsafe against injection attack
fridge = ",+".join(fridge)

# API endpoint to get recipe data
request1 = 'https://api.spoonacular.com/recipes/findByIngredients?ingredients='
request1 += fridge + '&number=' + str(num) + '&apiKey=' + API_KEY
response1 = requests.get(request1)

# check status code
if response1.status_code != 200:
    print('Response Status Code:', response1.status_code)
    quit()

recipes = response1.json()

result = dict()
for recipe in recipes:
    title = recipe['title']
    # make ingredient list for each title
    result[title] = dict()
    missedIngredients = list(recipe['missedIngredients'])
    if not missedIngredients:
        pass # no unused
    # print(missedIngredients)
    for mi in missedIngredients:
        id = mi['id']
        name = mi['name']
        # API endpoint to get ingredient data
        request2 = 'https://api.spoonacular.com/food/ingredients/' + str(id)
        request2 += '/information' + '?apiKey=' + API_KEY
        response2 = requests.get(request2)

        info = response2.json()
        result[title][name] = info['aisle'].lower()


print('\nChange++ Shopping List:')
result = json.dumps(result, indent=4)
print(result)
