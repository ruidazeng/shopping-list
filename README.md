>**If you have any questions regarding this repository, please contact Ruida Zeng at ruida dot zeng at vanderbilt dot edu**

# Creating a Shopping List using Spoonacular API

### Author's Notes
The most important criteria for the challenge is "functionality" (i.e. whether or not my code works according to the requirements). Hence, there are some vulnerabilities to injection attack in the code due to user input that have yet to be fixed.

Run the following command in terminal and follow the instructions:
```
python3 shopping.py
```

### The Challenge

Change++ is working with a non-profit that helps families save time and money on grocery shopping and meal prep. The company is looking for an application that should accomplish the following mission:

Given a list of ingredients that a user has in their fridge, return a list of recipe names for them to make, along with a “shopping list” of ingredients they are missing for each recipe.

You will use the Spoonacular API to write a program that accomplishes this. In order to use this API, you’ll need to create a free account. Once you do this, your API key can be found under My Console >> Profile >> Show/hide API key to see it. Keep in mind that there is a limit to how many API calls can be performed in a single day with a free account, so if you anticipate this being an issue you may want to allow more than one day to complete this project.

If you would like, feel free to explore the API; however, for the purposes of this program, we will only be asking you to use the following two endpoints:

Use this API endpoint to get recipe data: 
https://api.spoonacular.com/recipes/findByIngredients?ingredients=apples,+flour,+sugar&number=2

Use this API endpoint to get ingredient data:
https://api.spoonacular.com/food/ingredients/{id}/information

The first endpoint returns a list of recipes that can be made with the ingredients entered (apples, flour, and sugar). This endpoint is the exact one that should be called in your program.

The second endpoint retrieves information on specific ingredients based on ingredient id. You should parse through the first endpoint, retrieve all of the missed ingredients for each recipe, and use these ids to call the second endpoint. The specific information that we are looking for from the second endpoint data is the “aisle” field. The resulting shopping list should be a list of key-value pairs (ingredient and aisle):
{
	“cinnamon”: “spices and seasonings”,
	“oats”: “cereal”,
}

Your final output should be a list of recipe names with their corresponding shopping lists (the missing ingredients and the corresponding aisle find those ingredients):
{
	"Brown Butter Apple Crumble":
		{
			“cinnamon”: “spices and seasonings”,
			“oats”: “cereal”,
		},
	“Apple fritters”:
		{
			“beer”: “alcoholic beverages”,
			“eggs”: “milk, eggs, other dairy”,
			“Red-delicious-apple”: “produce”,
		},
}

