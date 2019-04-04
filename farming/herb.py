class Herb:
    def __init__(self, name, herb_price, seed_price):
        self.name = name
        self.herb_price = herb_price
        self.seed_price = seed_price
        self._modifier = 8.5

    def get_profit(self):
        return (self.herb_price * self._modifier) - self.seed_price
