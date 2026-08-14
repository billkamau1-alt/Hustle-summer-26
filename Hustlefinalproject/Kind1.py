#Kind 1 (Cardio Workout)
from Blueprint import Workouts
class CardioWorkouts(Workouts):
    def __init__(self, name, runtime, calories, intensity):
        super().__init__(name, runtime, calories)
        self.intensity = intensity
    
    def __str__(self):
        return f"{super().__str__()} - Intensity: {self.intensity}"

CardioWorkouts = CardioWorkouts("cardio", 30, 400, "High")
print(CardioWorkouts.name)
print(CardioWorkouts.runtime)
print(CardioWorkouts.calories)
print(CardioWorkouts.intensity)