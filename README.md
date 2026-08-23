# Student Marks Card System

A simple Python project that simulates a student marks card system using 
Object-Oriented Programming (OOP) concepts.

## Features
- Store multiple students with their name, age, ID, and marks
- Search for a student by name and view their full details
- Update a student's marks or age with validation (prevents invalid values)
- Displays a clear "not found" message if the searched name doesn't exist

## OOP Concepts Used
- **Class & Object** — `Person` and `School` classes, with multiple student objects created from `School`
- **Constructor (`__init__`)** — used to initialize each student's data
- **Inheritance** — `School` inherits from `Person`, reusing `name` and `age` 
  instead of repeating that logic
- **Encapsulation** — `age` and `marks` are protected using underscore-prefixed 
  attributes (`_age`, `_marks`) and can only be updated through validated 
  setter methods (`set_age`, `set_marks`)

## How It Works
1. Five student objects are created and stored in a list.
2. The user is prompted to enter a student's name.
3. The program searches the list and displays that student's full details, 
   or a "not found" message if there's no match.
4. Marks/age can be updated through `set_marks()` / `set_age()`, which 
   reject invalid values (marks must be 0–100, age must be 0–20).

## Example
