from models.ingredient import Ingredient
from models.dish import Dish
import csv


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.load_data(source_path)

    def load_data(self, source_path):
        with open(source_path, "r") as file:
            reader_menu = csv.reader(file)
            header, *data = reader_menu
            for row in data:
                dish_name = row[0]
                dish_price = float(row[1])
                dish_ing_name = row[2]
                dish_ing_qtd = float(row[3])

                new_ingredient = Ingredient(dish_ing_name)
                is_dish_new = self.find_dish_by_name(dish_name)

                if is_dish_new:
                    new_dish = Dish(dish_name, dish_price)
                    self.dishes.add(new_dish)

                new_dish.add_ingredient_dependency(
                    new_ingredient, dish_ing_qtd
                )

    def find_dish_by_name(self, dish_name):
        for dish in self.dishes:
            if dish.name == dish_name:
                return False
        return True


# [
# [dish,price,ingredient,recipe_amount],
# [lasanha presunto,25.90,queijo mussarela,15],
# [lasanha presunto,25.90,tomate,10],
# [lasanha presunto,25.90,farinha de trigo,10],
# [lasanha presunto,25.90,sal,5],
# [lasanha presunto,25.90,água,10],
# [lasanha presunto,25.90,presunto,15],
# [lasanha berinjela,27.00,queijo mussarela,15],
# lasanha berinjela,27.00,tomate,10
# lasanha berinjela,27.00,farinha de trigo,10
# lasanha berinjela,27.00,sal,5
# lasanha berinjela,27.00,água,10
# lasanha berinjela,27.00,berinjela,15
# ]
