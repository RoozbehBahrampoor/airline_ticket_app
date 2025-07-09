import unittest
from model.entity.ticket import ticket
class TestTicket(unittest.TestCase):
    def test_create(self):
        t = ticket("John" ,"5841" ,"Usa" ,"London" ,"Delta Air Line" ,
        "1/11/2025 , 23:55" ,"2/11/2025 , 05:55" ,"A 52" ,"YES")

