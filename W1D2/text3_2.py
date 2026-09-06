class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")


# ---------- Admin 类继承 User ----------
class Admin(User):
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f" - {privilege}")


# ---------- 主程序执行演示 ----------
if __name__ == '__main__':
    # 演示 User 和 Admin
    print("\n--- User demo ---")
    user = User("John", "Doe")
    user.describe_user()
    user.greet_user()

    print("\n--- Admin demo ---")
    admin = Admin("Jane", "Smith", ["can add post", "can delete post", "can ban user"])
    admin.describe_user()
    admin.greet_user()
    admin.show_privileges()