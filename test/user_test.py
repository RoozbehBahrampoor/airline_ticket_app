import unittest
from user import User, ROLE_CUSTOMER, ROLE_ADMIN

Class
TestUser(unittest.TestCase):


def setUp(self)
    self.user = User(
        id=1,
        name="Ali",
        family="Rezaei",
        birth_date="1990-01-01",
        user_name="alirezaei",
        password="pass123",
        is_locked=False,
        role=ROLE_CUSTOMER
    )


def test_user_creation(self):
    self.asserEqual(self.user.id, 1)
    self.asserEqual(self.user.name, "Ali")
    self.asserEqual(self.family, "Rezaei")
    self.asserEqual(self.user.birth_date, "1990-01-01")
    self.asserEqual(self.user_name, "alirezaei")
    self.asserEqual(self.user.password, "pass123")
    self.asserFalse(self.user.is_locked)
    self.asserEqual(self.user.role, ROLE_CUSTOMER)


def test_user_str(self):
    expected = (
        1, "Ali", "Rezaei", "1990-01-01", "alirezaei", "pass123", False, ROLE_CUSTOMER
    )
    self.assertEqual(self.user.to_tuple(), expected)


def test_getter(self):
    self.assertEqual(self.user.get_name(), "Ali")
    self.assertEqual(self.user.get_family(), "Rezaei")
    self.assertEqual(self.user.get_user_name(), "alirezaei")


def test_setters(self):
    self.user.set_name("Hossein")
    self.assertEqual(self.user.get_name(), "Hossein")

    self.user.set_family("Ahmadi")
    self.assertEqual(self.user.get_family(), "Ahmadi")

    self.user.set_user_name("hossein123")
    self.assertEqual(self.user.get_user_name(), "hossein123")


if __name__ == '__main__':
    unittest.main()
