students = [
    {
        "id": "SV001",
        "name": "Nguyen Van An",
        "math": 8.5,
        "physics": 7.5,
        "chemistry": 9.0,
        "average": 8.33,
        "rank": "Giỏi"
    },
    {
        "id": "SV002",
        "name": "Tran Thi Binh",
        "math": 7.0,
        "physics": 6.5,
        "chemistry": 7.5,
        "average": 7.0,
        "rank": "Khá"
    },
    {
        "id": "SV003",
        "name": "Le Van Cuong",
        "math": 5.0,
        "physics": 5.5,
        "chemistry": 6.0,
        "average": 5.5,
        "rank": "Trung Bình"
    },
    {
        "id": "SV004",
        "name": "Pham Thi Dung",
        "math": 4.0,
        "physics": 4.5,
        "chemistry": 3.5,
        "average": 4.0,
        "rank": "Yếu"
    },
    {
        "id": "SV005",
        "name": "Hoang Minh Duc",
        "math": 9.5,
        "physics": 9.0,
        "chemistry": 10.0,
        "average": 9.5,
        "rank": "Giỏi"
    }
]

while True:

    print("""
========== QUẢN LÝ SINH VIÊN ==========
1. Hiển thị danh sách sinh viên
2. Thêm mới sinh viên
3. Cập nhật thông tin sinh viên
4. Xóa sinh viên
5. Tìm kiếm sinh viên
6. Sắp xếp danh sách sinh viên
7. Thống kê điểm TB
8. Liệt kê sinh viên điểm cao nhất/thấp nhất
9. Phân loại học lực
0. Thoát
======================================
""")

    choice = input("Nhập lựa chọn: ").strip()

    match choice:

        case "1":

            if not students:
                print("Danh sách sinh viên trống")
                continue

            print(f"{'MÃ SV':<10}{'HỌ TÊN':<25}{'TOÁN':<10}{'LÝ':<10}{'HÓA':<10}{'TB':<10}{'XẾP LOẠI'}")

            for student in students:
                print(f"{student['id']:<10}{student['name']:<25}{student['math']:<10}{student['physics']:<10}{student['chemistry']:<10}{student['average']:<10}{student['rank']}")

        case "2":

            student_id = input("Nhập mã sinh viên: ").strip().upper()

            is_exist = False

            for student in students:
                if student["id"] == student_id:
                    is_exist = True
                    break

            if is_exist:
                print("Mã sinh viên đã tồn tại")
                continue

            name = input("Nhập họ tên: ").strip()

            try:
                math = float(input("Nhập điểm Toán: "))
                physics = float(input("Nhập điểm Lý: "))
                chemistry = float(input("Nhập điểm Hóa: "))
            except:
                print("Điểm không hợp lệ")
                continue

            if not (0 <= math <= 10 and 0 <= physics <= 10 and 0 <= chemistry <= 10):
                print("Điểm phải từ 0 đến 10")
                continue

            average = round((math + physics + chemistry) / 3, 2)

            if average < 5: rank = "Yếu"
            elif average < 7: rank = "Trung Bình"
            elif average < 8: rank = "Khá"
            else: rank = "Giỏi"

            students.append({"id": student_id, "name": name, "math": math, "physics": physics, "chemistry": chemistry, "average": average, "rank": rank})

            print("Thêm sinh viên thành công")

        case "3":

            student_id = input("Nhập mã sinh viên cần sửa: ").strip().upper()

            is_found = False

            for student in students:

                if student["id"] == student_id:

                    is_found = True

                    try:
                        student["math"] = float(input("Điểm Toán mới: "))
                        student["physics"] = float(input("Điểm Lý mới: "))
                        student["chemistry"] = float(input("Điểm Hóa mới: "))
                    except:
                        print("Điểm không hợp lệ")
                        break

                    student["average"] = round((student["math"] + student["physics"] + student["chemistry"]) / 3, 2)

                if student["average"] < 5: student["rank"] = "Yếu"
                elif student["average"] < 7: student["rank"] = "Trung Bình"
                elif student["average"] < 8: student["rank"] = "Khá"
                else: student["rank"] = "Giỏi"

                print("Cập nhật thành công")
                break

            if not is_found:
                print("Không tìm thấy sinh viên")

        case "4":

            student_id = input("Nhập mã sinh viên cần xóa: ").strip().upper()

            is_found = False

            for student in students:

                if student["id"] == student_id:

                    is_found = True

                    confirm = input("Bạn có chắc muốn xóa? (Y/N): ").strip().upper()

                    if confirm == "Y":
                        students.remove(student)
                        print("Xóa thành công")
                    else:
                        print("Đã hủy")

                    break

            if not is_found:
                print("Không tìm thấy sinh viên")

        case "5":

            keyword = input("Nhập mã hoặc tên sinh viên: ").strip().lower()

            is_found = False

            print(f"{'MÃ SV':<10}{'HỌ TÊN':<25}{'TB':<10}{'XẾP LOẠI'}")

            for student in students:

                if keyword == student["id"].lower() or keyword in student["name"].lower():

                    is_found = True

                    print(f"{student['id']:<10}{student['name']:<25}{student['average']:<10}{student['rank']}")

            if not is_found:
                print("Không tìm thấy sinh viên")

        case "6":

            print("""
1. Sắp xếp theo điểm TB giảm dần
2. Sắp xếp theo tên A-Z
""")

            sort_choice = input("Chọn: ")

            if sort_choice == "1":
                students.sort(key=lambda student: student["average"], reverse=True)
                print("Đã sắp xếp theo điểm TB")

            elif sort_choice == "2":
                students.sort(key=lambda student: student["name"].lower())
                print("Đã sắp xếp theo tên")

            else:
                print("Lựa chọn không hợp lệ")

        case "7":

            gioi = 0
            kha = 0
            trung_binh = 0
            yeu = 0

            for student in students:

                if student["rank"] == "Giỏi":
                    gioi += 1

                elif student["rank"] == "Khá":
                    kha += 1

                elif student["rank"] == "Trung Bình":
                    trung_binh += 1

                else:
                    yeu += 1

            print(f"Giỏi: {gioi}")
            print(f"Khá: {kha}")
            print(f"Trung Bình: {trung_binh}")
            print(f"Yếu: {yeu}")

        case "8":

            if not students:
                print("Danh sách sinh viên trống")
                continue

            highest = max(students, key=lambda student: student["average"])
            lowest = min(students, key=lambda student: student["average"])

            print("\nSinh viên có điểm TB cao nhất:")
            print(highest)

            print("\nSinh viên có điểm TB thấp nhất:")
            print(lowest)

        case "9":

            for student in students:

                if student["average"] < 5: student["rank"] = "Yếu"
                elif student["average"] < 7: student["rank"] = "Trung Bình"
                elif student["average"] < 8: student["rank"] = "Khá"
                else: student["rank"] = "Giỏi"

            print("Đã phân loại học lực")

        case "0":
            print("Thoát chương trình")
            break

        case _:
            print("Lựa chọn không hợp lệ")