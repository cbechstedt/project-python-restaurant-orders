from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_1 = Ingredient("camarão")
    ingredient_2 = Ingredient("queijo mussarela")
    ingredient_3 = Ingredient("camarão")

    assert ingredient_1.name == "camarão"
    assert ingredient_1.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
        Restriction.SEAFOOD,
    }

    assert repr(ingredient_1) == "Ingredient('camarão')"

    assert ingredient_1 != ingredient_2
    assert ingredient_1 == ingredient_3

    assert hash(ingredient_1) != hash(ingredient_2)
    assert hash(ingredient_1) == hash(ingredient_3)
