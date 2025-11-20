class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b


## This is a not related Commit, remenber how to just fetch one commit without all the others.

## If you feel lost just see this video it will help you: https://www.youtube.com/watch?v=dQw4w9WgXcQ