class User:
    def __init__(self, username: str, first_name: str, last_name: str, email: str, age: int, is_active: bool = True):
        self._username = username
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._age = age
        self._is_active = is_active

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value: str):
        if not value:
            raise ValueError("Поле username не может быть пустым")
        self._username = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        if not value:
            raise ValueError("Поле имя не может быть пустым")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value: str):
        if not value:
            raise ValueError("Поле фамилия не может быть пустым")
        self._last_name = value

    @property
    def email(self):
        return self._email

    @property
    def age(self):
        return self._age

    def have_birthday(self):
        self._age += 1

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, value: bool):
        self._is_active = bool(value)

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"
