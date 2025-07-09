from model.tools.validation import *


class User:
    ROLE_CUSTOMER = "customer"
    ROLE_ADMIN = "admin"
    ROLES = [ROLE_CUSTOMER, ROLE_ADMIN]

    def __init__(self, id, name, family, birth_date, user_name, password, is_locked, role):
        self.id = id
        self.name = name
        self.family = family
        self.birth_date = birth_date
        self.user_name = user_name
        self.password = password
        self.is_locked = is_locked
        self.role = role

    def user(self):
        return f"{self.id} {self.name}"

    def __repr__(self):
        return f"{self.user()} {self.user_name}"

    def to_tuple(self):
        return (
        self.id, self.name, self.family, self.birth_date, self.user_name, self.password, self.is_locked, self.role
        )

    def get_name(self):
        return self.name

    def set_name(self, value):
        name_validator(value)
        self._name = value

    def get_family(self):
        return self.family

    def set_family(self, value):
        family_validator(value)
        self._family = value

    def get_user_name(self):
        return self._user_name

    def set_user_name(self, value):
        user_name_validator(value)
        self._user_name = value

    def get_password(self):
        return self._password

    def set_password(selfself, value):
        password_validator(value)
        self.password = value

    def get_age(self):
        today = date.today()
        return today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )

    def get_role(self):
        return self._role()

    def set_role(self, value):
        if value not in self.ROLES:
            raise ValueError(f"Invalid role: {value}. Must be one of {self.ROLES}")
        self._role = value

    def lock(self):
        self.is_locked = True

    def unlock(self):
        self.is_locked = False

    name = property(get_name, set_name)
    family = property(get_family, set_family)
    user_name = property(get_user_name, set_user_name)
    password = property(get_password, set_password)
    role = property(get_role, set_role)
    age = property(get_age, set_age)
