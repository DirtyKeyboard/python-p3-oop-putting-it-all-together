#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, color="Unknown", material="Unknown", condition="Unknown"):
        self.brand = brand
        self.color = color
        self._size = 0
        self.material = material
        self.condition = condition

    def get_size(self):
        return self._size
    
    def set_size(self, size):
        if type(size) == int:
            self._size = size
        else:
            print("size must be an integer")
    size = property(get_size, set_size)

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = 'New'