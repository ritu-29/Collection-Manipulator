print("Welcome to the student Data Oraganizer...!")

students = []
subjects = set()

while True:
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    ch = int(input("Enter your choice:"))

    if ch == 1:
        print("Enter student details:")
        
        stu_id = int(input("Student ID:"))
        name = input("Name:")
        age = int(input("Age:"))
        grade = input("Grade:")
        dob = input("Date of Birth (YYYY-MM-DD):")
        subject = input("Subjects (comma-separated): ").split(",")

        unique_info = (stu_id,dob)

        for i in students:
            for j in i["subject"]:
                subjects.add(j)

        student = {
            "unique" : unique_info,
            "name" : name,
            "age" : age,
            "grade" : grade,
            "subject" : subject,
        }
        students.append(student)
        
        print("Student Added Successfully..!!")

    elif ch == 2:
        print("--Display All Students--")
        if not students:
            print("Not found data")
        else:
            for s in students:
                print(f"Student Id : {s["unique"][0]}  |  Name : {s["name"]}  | Age: {s["age"]} | Date of Birth : {s["unique"][1]} | Grade : {s["grade"]} |  Subject: {s["subject"]}" )
    
    
    elif ch == 3:
        stu_id = int(input("Enter Student Id You want to Update: "))
        
        for s in students:
            if s["unique"][0]==stu_id:
                new_age = int(input("Enter New Age:"))
                s["age"]=new_age
                
                new_subs = input("New Subjects(comma separated):").split(",")
                s["subject"] = new_subs

                for i in new_subs:
                    subjects.add(i)
                s["subjects"] = subjects
                
                print("Updated..!")
                break

        else:
            print("Student Not Found")
        
    elif ch == 4:
        stu_id = int(input("Enter Student Id You want to Delete: "))

        for s in students:
            if s["unique"][0] == stu_id:
                students.remove(s)
                print("Deleted successfully")
                break
        else:
            print("Not Found student")
    
    elif ch == 5:
        if not students:
            print("Not found")
        else:
            subjects.clear()
            for i in students:
                for j in i["subject"]:
                    subjects.add(j)
            
            print("Subjects Offered:")
            for j in subjects:
                print(j)
                
    elif ch == 6:
        print("Exit")
        break

    else:
        print("Invalid Choice") 
        
        
        