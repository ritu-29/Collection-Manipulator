# Student Collection Manipulator

## 📌 Overview
This is a **menu-driven Python program** used to manage student records.  
It allows the user to **add, display, update, delete students**, and **view unique subjects offered**.

The program is written **without using functions**, to clearly demonstrate **loops, logic, and collection data types**.

---

## 🎯 Objective
- Store student data efficiently
- Use Python collections properly
- Understand loops and conditional logic
- Practice real-world style menu program

---

## 🧱 Data Structures Used

### 🔹 List (`students`)
```python
students = []
```
- Stores multiple student records
- Each record is a dictionary
- List is **mutable**, so data can be added or removed

---

### 🔹 Tuple (`unique_info`)
```python
unique_info = (stu_id, dob)
```
- Stores **Student ID** and **Date of Birth**
- Tuple is **immutable**, so unique identity cannot be changed

---

### 🔹 Dictionary (`student`)
```python
student = {
    "unique": unique_info,
    "name": name,
    "age": age,
    "grade": grade,
    "subject": subject
}
```
- Stores complete student information
- Access values using keys like `student["name"]`

---

### 🔹 Set (`subjects`)
```python
subjects = set()
```
- Stores only **unique subjects**
- Duplicate subjects are automatically removed

---

## 🔁 Loops Used (Detailed Explanation)

### 1️⃣ Infinite `while` Loop
```python
while True:
```
✅ **Why used?**
- Keeps showing the menu again and again
- Program stops only when user selects **Exit (6)**

---

### 2️⃣ `for` Loop – Add Subjects to Set
```python
for i in students:
    for j in i["subject"]:
        subjects.add(j)
```
✅ **Explanation:**
- Outer loop goes through each student
- Inner loop goes through each subject of that student
- `set.add()` ensures subjects stay unique

📌 **Why nested loop?**
Because one student can have multiple subjects.

---

### 3️⃣ `for` Loop – Display Students
```python
for s in students:
    print(s)
```
✅ **Explanation:**
- Loops through each student dictionary
- Prints student details one by one

---

### 4️⃣ `for-else` Loop – Update Student
```python
for s in students:
    if s["unique"][0] == stu_id:
        s["age"] = new_age
        break
else:
    print("Student Not Found")
```
✅ **Explanation:**
- Searches student by ID
- `break` stops loop when found
- `else` runs only if student is NOT found

---

### 5️⃣ `for` Loop – Display Subjects Offered
```python
subjects.clear()
for i in students:
    for j in i["subject"]:
        subjects.add(j)
```
✅ **Why `clear()`?**
- Removes old subjects
- Prevents duplicate or outdated data

---

## 🧠 Menu Logic (Conditionals)

```python
if ch == 1:
elif ch == 2:
elif ch == 3:
...
```
- Executes different code blocks based on user choice
- Makes program **interactive and user-friendly**

---

## 🔧 Methods Used

| Method | Purpose |
|------|--------|
| `append()` | Add student to list |
| `remove()` | Delete student |
| `add()` | Add subject to set |
| `clear()` | Clear set data |
| `split()` | Convert string to list |
| `input()` | Take input |
| `print()` | Display output |

---

## 📌 Key Concepts Learned
- List mutability
- Tuple immutability
- Set uniqueness
- Dictionary data handling
- Nested loops
- Menu-driven logic

---

## ✅ Conclusion
This project is ideal for **Python beginners** to understand how loops and collections work together in a real program.

---

✍️ Author: Rituu Poonjani
