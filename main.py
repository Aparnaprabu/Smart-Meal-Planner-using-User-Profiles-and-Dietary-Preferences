import pandas as pd

class UserProfile:
    def __init__(self, name, age, dietary_preference, calorie_requirement, dietary_restrictions):
        self.name = name
        self.age = age
        self.dietary_preference = dietary_preference
        self.calorie_requirement = calorie_requirement
        self.dietary_restrictions = dietary_restrictions
    
    def display_profile(self):
        print(f"User: {self.name}, Age: {self.age}, Preference: {self.dietary_preference}, \n Calorie Requirement: {self.calorie_requirement}, Restrictions: {self.dietary_restrictions}")

class Meal:
    def __init__(self, name, calories, protein, carbs, category):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.category = category
    
    def display_meal(self):
        print(f"{self.name} | Calories: {self.calories} | Protein: {self.protein}g | Carbs: {self.carbs}g | Category: {self.category}")

class MealPlan:
    def __init__(self, breakfast, lunch, dinner):
        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner
     
    def display_meal_plan(self):
        print("\nMeal Plan:")
        print("Breakfast:")
        for meal in self.breakfast:
            meal.display_meal()
        print("Lunch:")
        for meal in self.lunch:
            meal.display_meal()
        print("Dinner:")
        for meal in self.dinner:
            meal.display_meal()

class BSTNode:
    def __init__(self, user_profile):
        self.user_profile = user_profile
        self.left = None
        self.right = None

class DietaryBST:
    def __init__(self):
        self.root = None

    def insert(self, profile):
        self.root = self._insert_rec(self.root, profile)

    def _insert_rec(self, root, profile):
        if root is None:
            return BSTNode(profile)
        if profile.calorie_requirement < root.user_profile.calorie_requirement:
            root.left = self._insert_rec(root.left, profile)
        elif profile.calorie_requirement > root.user_profile.calorie_requirement:
            root.right = self._insert_rec(root.right, profile)
        return root

    def inorder_traversal(self):
        self._inorder_rec(self.root)
    
    def _inorder_rec(self, root):
        if root is not None:
            self._inorder_rec(root.left)
            root.user_profile.display_profile()
            self._inorder_rec(root.right)

class MealPlanner:
    @staticmethod
    def load_meal_database():
        try:
            df = pd.read_csv("/Users/dhirajsolleti/Downloads/DSA_DP.csv")
            print("CSV Columns:", df.columns.tolist())
            required_columns = ['food', 'Caloric Value', 'Protein', 'Carbohydrates']
            if not all(col in df.columns for col in required_columns):
                print("Error: Missing required columns. Found:", df.columns.tolist())
                df.columns = ['food', 'Caloric Value', 'Fat', 'Carbohydrates', 'Sugars', 'Protein', 'Water', 
                              'Vitamin A', 'Vitamin B1', 'Vitamin C', 'Vitamin D', 'Vitamin E', 'Vitamin K', 
                              'Calcium', 'Iron']
            
            meals = []
            for _, row in df.iterrows():
                food_name = row['food']
                if any(term in food_name.lower() for term in ['chicken', 'beef', 'pork', 'ham', 'egg']):
                    category = "Non-Vegetarian"
                elif any(term in food_name.lower() for term in ['cheese', 'pasta', 'ricotta', 'mozzarella', 'cheddar']):
                    category = "Vegetarian"
                elif any(term in food_name.lower() for term in ['jam', 'honey', 'peanut butter', 'apple butter', 'marmalade', 'tahini']):
                    category = "Vegan"
                else:
                    category = "Vegetarian"  
                try:
                    meal = Meal(
                        name=food_name,
                        calories=float(row['Caloric Value']),
                        protein=float(row['Protein']),
                        carbs=float(row['Carbohydrates']),
                        category=category
                    )
                    meals.append(meal)
                except ValueError as e:
                    print(f"Skipping row with food '{food_name}': Invalid data ({e})")
            return meals
        except FileNotFoundError:
            print("Error: CSV file 'DSA_DP.csv' not found. Please check the file path.")
            return []
        except Exception as e:
            print(f"Error loading CSV: {e}")
            return []

    meal_database = load_meal_database()

    @staticmethod
    def get_matching_meals(profile):
        return [meal for meal in MealPlanner.meal_database 
                if meal.calories <= profile.calorie_requirement and meal.category in profile.dietary_restrictions]

    @staticmethod
    def generate_meal_plan(profile):
        matched_meals = MealPlanner.get_matching_meals(profile)
        breakfast, lunch, dinner = [], [], []
        
        for meal in matched_meals:
            if not breakfast:
                breakfast.append(meal)
            elif not lunch:
                lunch.append(meal)
            elif not dinner:
                dinner.append(meal)
            if len(breakfast) == 1 and len(lunch) == 1 and len(dinner) == 1:
                break
        
        return MealPlan(breakfast, lunch, dinner)

def main():
    diet1 = ["Vegan"]
    diet2 = ["Vegetarian"]
    diet3 = ["Vegan", "Vegetarian"]
    
    user1 = UserProfile("Sathwik", 25, "Vegan", 1000, diet1)
    user2 = UserProfile("Dheeraj", 22, "Vegetarian", 1500, diet2)
    user3 = UserProfile("Deekshith", 28, "Vegan", 1800, diet3)
    
    bst = DietaryBST()
    bst.insert(user1)
    bst.insert(user2)
    bst.insert(user3)
    
    print("Inorder Traversal of Profiles:")
    bst.inorder_traversal()
    
    print("\nMeal Plan for Sathwik:")
    MealPlanner.generate_meal_plan(user1).display_meal_plan()
    
    print("\nMeal Plan for Dheeraj:")
    MealPlanner.generate_meal_plan(user2).display_meal_plan()
    
    print("\nMeal Plan for Deekshith:")
    MealPlanner.generate_meal_plan(user3).display_meal_plan()

if __name__ == "__main__":
    main()