import pytest
from praktikum.ingredient import Ingredient
from praktikum import ingredient_types


class TestIngredients:

    def test_get_price_ingredient(self):
        ingredient = Ingredient('SAUCE', 'Кетчуп', 60)
        assert ingredient.get_price() == 60, 'Ошибка: неверное значение стоимости ингредиента '

    def test_get_name_ingredient(self):
        ingredient = Ingredient('SAUCE', 'Кетчуп', 60)
        assert ingredient.get_name() == 'Кетчуп', 'Ошибка: неверное имя ингредиента '

    @pytest.mark.parametrize('ingredient_type,name,price', [
        [ingredient_types.INGREDIENT_TYPE_SAUCE, 'Ketchup', 50],
        [ingredient_types.INGREDIENT_TYPE_FILLING, 'Cheese', 60]
    ])
    def test_get_type_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
