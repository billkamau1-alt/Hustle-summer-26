# Kind 2 (Lift workout)
from Blueprint import Workouts
class Liftworkout(Workouts):
    def __init__(self, name, runtime, calories, lift):
        super().__init__(name,runtime,calories)
        self.lift = lift # could be a weight or type of lift
    def __str__(self):
        return f"{super().__str__()} - lift: {self.lift}"
    
Liftworkouts = Liftworkout("Lift", 50, 500, "Bench Press")
print(Liftworkouts.name)
print(Liftworkouts.runtime)
print(Liftworkouts.calories)
print(Liftworkouts.lift)