import json


def load_recipe(json_string):
    """Wandelt einen JSON-kodierten String in ein Python-Dictionary um."""
    return json.loads(json_string)


def adjust_recipe(recipe, num_people):
    """Passt die Mengenangaben eines Rezepts an die gegebene Anzahl an Personen an."""
    original_servings = recipe['servings']
    factor = num_people / original_servings

    adjusted_ingredients = {
        ingredient: int(amount * factor)
        for ingredient, amount in recipe['ingredients'].items()
    }

    adjusted_recipe = {
        'title': recipe['title'],
        'ingredients': adjusted_ingredients,
        'servings': num_people
    }

    return adjusted_recipe


if __name__ == '__main__':
    recipe_json = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}'

    recipe = load_recipe(recipe_json)

    adjusted_recipe = adjust_recipe(recipe, 2)

    print(json.dumps(adjusted_recipe, indent=4))