# My Blueprint for workouts
class Workouts:
    def __init__(self, name, runtime, calories,):
        self.name = name
        self.runtime = self.validate_runtime(runtime)
        self.calories = self.validate_calories(calories)
    
    def validate_runtime(self, value):
        if value < 0:
            print("No negative values allowed.")
            return 0
            return value

    def validate_calories(self, value):
        if value < 0:
            print("No negative values allowed.")
            return 0
        return value

Running = Workouts("Running", 20, 250)
print(Running.name)
print(Running.runtime)
print(Running.calories)

