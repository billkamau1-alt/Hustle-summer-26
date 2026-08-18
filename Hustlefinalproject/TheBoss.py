# The Boss (Manager)
from Blueprint import Workouts
class workoutmanager:
    def __init__(self):
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(workout)

    def show_workouts(self):
      for i, workout in enumerate(self.workouts, 1):
            print(f"{i}. {workout.name} - Runtime: {workout.runtime}, Calories: {workout.calories}")
    def total_runtime(self):
        return sum(w.runtime for w in self.workouts if w.runtime is not None)
        
    def total_calories(self):
        return sum(w.calories for w in self.workouts if w.calories is not None)

    def say_no_to_bad_number(self, number, maximum):
        if number < 1 or number > maximum:
            print("Invalid input. Please enter a valid number.")
            return None
        return number
    

    def menu(self):
        while True:
            print("\n---Workout Manager---")
            print("1. Add Workout")
            print("2. Show Workouts")
            print("3. Total Runtime")
            print("4. Total Calories")
            print("5. Exit")

            choice = self.say_no_to_bad_number(int(input("Enter your choice: ")), 5)

            if not choice:
                continue

            if choice == 1:
                name = input("Enter workout name: ")
                runtime = int(input("Enter runtime: "), 20)
                calories = int(input("Enter calories: "), 35)
                workout = Workouts(name, runtime, calories)
                self.add_workout(workout)
            elif choice == 2:
                self.show_workouts()
            elif choice == 3:
                print(f"Total Runtime: {self.total_runtime()}")
            elif choice == 4:
                print(f"Total Calories: {self.total_calories()}")
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please try again.")

manager = workoutmanager()

workout = Workouts("Workout Manager", 1, 50)
manager.add_workout(workout) 
manager.menu()