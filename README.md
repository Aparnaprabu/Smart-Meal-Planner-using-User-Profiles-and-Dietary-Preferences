# Smart Meal Planner

## Project Overview
The **Smart Meal Planner** is a Java-based application designed to automate personalized meal planning by leveraging user profiles, dietary preferences, and nutritional data. The system generates tailored meal plans for breakfast, lunch, and dinner based on user inputs such as age, calorie requirements, dietary preferences (Vegan, Vegetarian, Non-Vegetarian), and restrictions. It integrates Object-Oriented Programming (OOP) concepts and Data Structures and Algorithms (DSA) to ensure efficient data management and retrieval.

This project was developed as part of the coursework for:
- **22AIE111 - OOP in Java**
- **22AIE112 - Data Structure and Algorithm**

## Team Members
- Aparna A (CB.SC.U4AIE24206)
- Gaddam Deepika Reddy (CB.SC.U4AIE24215)
- Pabbathi Gnana Vikas Sai (CB.SC.U4AIE24238)
- P. Praveen Reddy (CB.SC.U4AIE24243)

## Features
- **User Profile Management**: Stores user details such as name, age, dietary preferences, restrictions, and calorie needs.
- **Meal Data Processing**: Reads nutritional data from a CSV file and filters meals based on user preferences.
- **Meal Plan Generation**: Automatically generates daily meal plans (breakfast, lunch, dinner) tailored to user requirements.
- **Efficient Data Storage**: Utilizes a Binary Search Tree (BST) for storing and retrieving user profiles sorted by calorie requirements.
- **Web-based UI**: Provides a simple and intuitive interface for users to input data and view personalized meal plans.

## Objectives
- Create and manage user profiles with relevant dietary and nutritional information.
- Filter meals from a CSV dataset based on user preferences and restrictions.
- Generate personalized meal plans for breakfast, lunch, and dinner.
- Implement efficient storage and retrieval of user data using a Binary Search Tree (BST).

## Technologies Used
- **Programming Language**: Java
- **Data Structures**: Binary Search Tree (BST), ArrayList
- **File Handling**: CSV file processing for meal data
- **UI**: Web-based interface for user interaction
- **Concepts**:
  - OOP: Classes, Objects, Constructors, Encapsulation, Static Methods, Method Definition
  - DSA: BST Insertion, Inorder Traversal, Recursion, Filtering, Sorting
  - Others: Conditional Statements, Looping, File Handling

## Java Concepts Implemented
| Concept | Description | Example in Project |
|---------|-------------|--------------------|
| Class | Blueprint for objects | `UserProfile`, `Meal`, `MealPlanner` classes |
| Object | Instance of a class | `UserProfile user = new UserProfile(...);` |
| Constructor | Initializes objects | `public Meal(String name, int calories, ...)` |
| Static Methods | Methods called without instantiation | `MealPlanner.generatePlan()` |
| Encapsulation | Data hiding with private variables and accessors | `private int calories; getCalories()` |
| File Handling | Reading/writing data from files | `BufferedReader reader = new FileReader(...)` |
| ArrayList | Dynamic array for storing items | `ArrayList<Meal> meals = new ArrayList<>();` |
| Conditional Statements | Controls logic flow | `if (meal.getCalories() < user.getLimit())` |
| Looping | Iterates over collections | `for (Meal m : meals)` |
| Method Definition | Defines reusable code blocks | `public void displayMeal()` |

## DSA Concepts Implemented
| Concept | Description | Example in Project |
|---------|-------------|--------------------|
| Binary Search Tree (BST) | Organizes user profiles by calorie requirements | `DietaryBST.insert(userProfile)` |
| Inorder Traversal | Retrieves profiles in sorted order | `inorderTraversal(root)` |
| Filtering | Selects meals based on conditions | `if (meal.category.equals(user.category))` |
| Recursion | Function calling itself | `displayInorder(node.left)` |
| Time Complexity | Efficiency of operations | List filtering: O(n), BST insertion: O(log n) |
