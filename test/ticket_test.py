import unittest
from model.entity.ticket import ticket
class TestTicket(unittest.TestCase):
    def test_create(self):
        t = ticket("John" ,"5841" ,"Usa" , )