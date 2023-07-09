from models.ingredient import Ingredient, Restriction
from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    dish = Dish("Spaghetti Carbonara", 15.99)
    assert dish.name == "Spaghetti Carbonara"
    assert dish.price == 15.99

    assert repr(dish) == "Dish('Spaghetti Carbonara', R$15.99)"

    dish_2 = Dish("Spaghetti Carbonara", 15.99)
    assert dish == dish_2
    dish_3 = Dish("Lasagna", 12.99)
    assert dish != dish_3

    assert hash(dish) == hash(dish_2)
    assert hash(dish) != hash(dish_3)

    ingredient_1 = Ingredient("bacon")
    ingredient_2 = Ingredient("queijo mussarela")
    dish.add_ingredient_dependency(ingredient_1, 100)
    dish.add_ingredient_dependency(ingredient_2, 200)
    assert dish.recipe == {ingredient_1: 100, ingredient_2: 200}

    restrictions = dish.get_restrictions()
    assert len(restrictions) == 3
    assert Restriction.LACTOSE in restrictions
    assert Restriction.ANIMAL_DERIVED in restrictions

    ingredients = dish.get_ingredients()
    assert len(ingredients) == 2
    assert ingredient_1 in ingredients
    assert ingredient_2 in ingredients

    with pytest.raises(TypeError):
        Dish("Invalid Dish", "15.99")

    with pytest.raises(ValueError):
        Dish("Invalid Dish", 0)
