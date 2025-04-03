# 학생 점수 관리 프로그램
students = [["학생1", [0, 0, 0]], ["학생2", [0, 0, 0]], ["학생3", [0, 0, 0]]]
subjects = ["국어", "영어", "수학"]

def show_students():
    print("\n전체 학생 성적:")
    for student in students:
        name, scores = student
        total = sum(scores)
        average = total / len(scores)
        print(f"{name}: {scores}, 총점: {total}, 평균: {average:.2f}")

def change_score():
    print("\n성적 변경:")
    for i, student in enumerate(students):
        print(f"{i+1}. {student[0]}")
    student_idx = int(input("학생 번호 선택: ")) - 1
    
    for i, subject in enumerate(subjects):
        print(f"{i+1}. {subject}")
    subject_idx = int(input("과목 번호 선택: ")) - 1
    
    new_score = int(input("새 점수 입력: "))
    students[student_idx][1][subject_idx] = new_score
    print(f"{students[student_idx][0]}의 {subjects[subject_idx]} 점수가 {new_score}로 변경되었습니다.")

def main():
    while True:
        print("\n1. 전체 학생 출력\n2. 성적 변경\n3. 종료")
        choice = input("메뉴 선택: ")
        if choice == "1":
            show_students()
        elif choice == "2":
            change_score()
        elif choice == "3":
            print("프로그램 종료")
            break
        else:
            print("잘못된 입력입니다.")

# 프로그램 실행
main()
