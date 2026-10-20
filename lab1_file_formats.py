import csv
import json

students = [
    {"id": 1, "name": "Nguyen Van A", "age": 20, "major": "Computer Science", "gpa": 3.4},
    {"id": 2, "name": "Tran Thi B", "age": 21, "major": "Data Science", "gpa": 3.8},
    {"id": 3, "name": "Le Van C", "age": 22, "major": "Information Technology", "gpa": 3.1},
    {"id": 4, "name": "Pham Minh D", "age": 20, "major": "Data Science", "gpa": 3.6},
    {"id": 5, "name": "Vu Hai Yen", "age": 21, "major": "Computer Science", "gpa": 3.9}
]

# 1. Tao file TXT
with open("students.txt", "w", encoding="utf-8") as f:
    f.write("DANH SACH SINH VIEN\n")
    for s in students:
        f.write(
            f"ID: {s['id']} | {s['name']} | Tuoi: {s['age']} "
            f"| Nganh: {s['major']} | GPA: {s['gpa']}\n"
        )

# 2. Tao file CSV
with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f, fieldnames=["id", "name", "age", "major", "gpa"]
    )
    writer.writeheader()
    writer.writerows(students)

# 3. Tao file JSON
with open("students.json", "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False, indent=2)

print("Da tao thanh cong 3 file: students.txt, students.csv, students.json!")