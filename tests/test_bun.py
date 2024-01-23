from praktikum.bun import Bun


class TestBun:
    def test_get_name_bun(self):
        bun = Bun('Бриошь', 99)
        assert bun.get_name() == 'Бриошь'

    def test_get_price_bun(self):
        bun = Bun('Бриошь', 99)
        assert bun.get_price() == 99
