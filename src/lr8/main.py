from lr8.user import User

def main():
    user = User("iva123", "Iva", "Test", "iva@example.com", 20)
    print(user.username)
    print(user.full_name)
    print(user.age)
    print(user.is_active)

    user.username = "iva2025"
    user.have_birthday()
    user.is_active = False
    print(user.username)
    print(user.age)
    print(user.is_active)

if __name__ == "__main__":
    main()