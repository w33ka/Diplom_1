from unittest.mock import Mock
import pytest

from praktikum.burger import Burger


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Бриошь'
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun, (f'Ошибка: булка не установлена (ожидалась: {mock_bun}, '
                                        f'фактическая: {burger.bun})')

    @pytest.mark.parametrize("ingredient_type, name, price", [
        ('FILLING', 'Cheese', 50),
        ('SAUCE', 'Ketchup', 60),
    ])
    def test_add_ingredient(self, ingredient_type, name, price):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = ingredient_type
        mock_ingredient.get_name.return_value = name
        mock_ingredient.get_price.return_value = price

        burger.add_ingredient(mock_ingredient)

        assert mock_ingredient in burger.ingredients, (
            f'Ошибка: ингредиент не добавлен (ожидался: {mock_ingredient},'
            f' фактический список: {burger.ingredients})'
        )

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.ingredients = [mock_ingredient]
        burger.remove_ingredient(0)
        assert mock_ingredient not in burger.ingredients, 'Ошибка:Ингридиент не удален'

    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        burger.ingredients = [mock_ingredient1, mock_ingredient2]
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ingredient2, mock_ingredient1], 'Ошибка: порядок ингредиентов не соблюден'

    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        mock_ingredient1 = Mock()
        mock_ingredient1.get_price.return_value = 50
        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = 60
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        expected_price = 310
        assert burger.get_price() == expected_price, 'Ошибка: неверная цена'

    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Бриошь'
        mock_bun.get_price.return_value = 100

        mock_ingredient1 = Mock()
        mock_ingredient1.get_type.return_value = 'FILLING'
        mock_ingredient1.get_name.return_value = 'Сыр'
        mock_ingredient1.get_price.return_value = 50

        mock_ingredient2 = Mock()
        mock_ingredient2.get_type.return_value = 'SAUCE'
        mock_ingredient2.get_name.return_value = 'Кетчуп'
        mock_ingredient2.get_price.return_value = 60

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        expected_receipt = '(==== Бриошь ====)\n= filling Сыр =\n= sauce Кетчуп =\n(==== Бриошь ====)\n\nPrice: 310'
        assert burger.get_receipt() == expected_receipt, 'Ошибка: неверный формат чека'
