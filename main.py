"""
Dieses Modul verwaltet ein JSON-basiertes Kochbuch und passt die Mengenangaben
von Rezepten an eine gegebene Anzahl von Personen an. Alle Funktionen sind
pure functions und verwenden nur unveränderliche Daten.
"""

import json

def load_recipe(json_string):
    """Wandelt einen JSON-kodierten String in ein Python-Dictionary um."""
    return json.loads(json_string)

def adjust_recipe(recipe_data, num_people):
    """Passt die Mengenangaben eines Rezepts an die gegebene Anzahl an Personen an."""
    original_servings = recipe_data['servings']
    factor = num_people / original_servings

    adjusted_ingredients = {
        ingredient: int(amount * factor)
        for ingredient, amount in recipe_data['ingredients'].items()
    }

    adjusted_recipe_data = {
        'title': recipe_data['title'],
        'ingredients': adjusted_ingredients,
        'servings': num_people
    }

    return adjusted_recipe_data

if __name__ == '__main__':
    recipe_json = (
        '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, '
        '"Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}'
    )

    loaded_recipe = load_recipe(recipe_json)

    adjusted_recipe_for_two = adjust_recipe(loaded_recipe, 2)

    print(json.dumps(adjusted_recipe_for_two, indent=4))

