import unittest
from model.entity.ticket import ticket
class TestTicket(unittest.TestCase):
    def test_create(self):
        t = ticket("12345" ,"5841" ,"Usa" ,"London" ,"Delta Air Line" ,
        "1/11/2025 , 23:55" ,"2/11/2025 , 05:55" ,"A 52" ,"YES")
        self.assertEqual(t.id, "12345")
        self.assertEqual(t.ticket_code, "5841")
        self.assertEqual(t.origin, "Usa")
        self.assertEqual(t.destination, "London")
        self.assertEqual(t.airline, "Delta Air Line")
        self.assertEqual(t.start_date_time, "1/11/2025 , 23:55")
        self.assertEqual(t.end_date_time, "2/11/2025 , 05:55")
        self.assertEqual(t.seat_no, "A 52")
        self.assertEqual(t.sold, "Yes")



if ticket == "mine":
    unittest.main()




