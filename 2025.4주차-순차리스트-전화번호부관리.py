class PhoneBookManager:
    def __init__(self):
        self.phone_book = []

    def add_user(self):
        name = input("이름: ")
        if any(user["name"] == name for user in self.phone_book):
            print("이미 저장된 이름입니다.")
            return
        phone = input("전화번호: ")
        self.phone_book.append({"name": name, "phone": phone})

    def edit_user(self):
        name = input("수정할 이름: ")
        for user in self.phone_book:
            if user["name"] == name:
                user["phone"] = input("새 전화번호: ")
                print(f"{name}님의 정보가 수정되었습니다.")
                return
        print("해당 사용자가 없습니다.")

    def delete_user(self):
        name = input("삭제할 이름: ")
        for user in self.phone_book:
            if user["name"] == name:
                self.phone_book.remove(user)
                print(f"{name}님의 정보가 삭제되었습니다.")
                return
        print("해당 사용자가 없습니다.")

    def print_all(self):
        print("\n전화번호부")
        for user in self.phone_book:
            print(f"이름: {user['name']}, 전화번호: {user['phone']}")
        print()

    def run(self):
        while True:
            choice = input("추가(n), 수정(e), 삭제(d), 출력(p), 종료(q): ").lower()
            if choice == 'n':
                self.add_user()
            elif choice == 'e':
                self.edit_user()
            elif choice == 'd':
                self.delete_user()
            elif choice == 'p':
                self.print_all()
            elif choice == 'q':
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다.")


if __name__ == '__main__':
    PhoneBookManager().run()

