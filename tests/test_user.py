from lr8.user import User

def test_full_name():
    user = User("testuser001", "First", "Last", "test@example.com", 30)
    assert user.full_name == "First Last"

def test_have_birthday():
    user = User("testuser001", "First", "Last", "test@example.com", 30)
    user.have_birthday()
    assert user.age == 31