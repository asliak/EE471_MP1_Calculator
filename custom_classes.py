class Calculator(object):
    def __init__(self):
        self._current_val = 0
    
<<<<<<< HEAD
    def add(self, x, y):
        self._current_val = x + y

    def subtract(self, x, y):
        self._current_val = x - y

    def multiply(self, x, y):
        self._current_val = x * y
=======
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Divider can't be 0!")
        self._current_val = x / y
>>>>>>> feat/div
        return self._current_val