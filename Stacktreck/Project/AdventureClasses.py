class Monster:
    def __init__(self, name, max_health, attack, defense, speed, hit, experience):
        self._name = name
        self._level = 1
        self._max_health = int(max_health)
        self._current_health = self._max_health
        self._max_mana = 5
        self._current_mana = self._max_mana
        self._attack = int(attack)
        self._defense = int(defense)
        self._speed = int(speed)
        self._hit = int(hit)
        self._potions = 0
        self._gold = 100
        self._experience = int(experience)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, value):
        self._level = value

    @property
    def max_health(self):
        return self._max_health
    
    @max_health.setter
    def max_health(self, value):
        self._max_health = value

    @property
    def current_health(self):
        return self._current_health

    @current_health.setter
    def current_health(self, value):
        self._current_health = value

    @property
    def max_mana(self):
        return self._max_mana
    
    @max_mana.setter
    def max_mana(self, value):
        self._max_mana = value

    @property
    def current_mana(self):
        return self._current_mana

    @current_mana.setter
    def current_mana(self, value):
        self._current_mana = value

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, value):
        self._attack = value

    @property
    def defense(self):
        return self._defense

    @defense.setter
    def defense(self, value):
        self._defense = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    @property
    def hit(self):
        return self._hit

    @hit.setter
    def hit(self, value):
        self._hit = value

    @property
    def potions(self):
        return self._potions

    @potions.setter
    def potions(self, value):
        self._potions = value

    @property
    def gold(self):
        return self._gold
    
    @gold.setter
    def gold(self, value):
        self._gold = value

    @property
    def experience(self):
        return self._experience
    
    @experience.setter
    def experience(self, value):
        self._experience = value


class ShopItems:
    def __init__(self, id, name, price, description):
        self._id = id
        self._name = name
        self._price = price
        self._description = description

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        self._price = value

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        self._description = value