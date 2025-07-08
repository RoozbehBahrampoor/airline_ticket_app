


ticket_list = []

class ticketController:
    def save(self,id ,ticket_code ,origin ,destination ,airline ,start_date_time ,end_date_time ,price ,seat_no ,sold  ):
        try:
            ticket = ticket(id ,ticket_code ,origin ,destination ,airline ,start_date_time ,end_date_time ,price,seat_no,sold )
            ticket_list.append(ticket)
            return True, f"ticket Saved Successfully {ticket}"
        except Exception as e:
            return False, f"ticket Saved Failed\n{e}"


    def edit(self,id ,ticket_code ,origin ,destination ,airline ,start_date_time ,end_date_time ,price,seat_no,sold ):
        try:
            ticket1 = ticket(id ,ticket_code ,origin ,destination ,airline,start_date_time ,end_date_time ,price ,seat_no ,sold )
        #     edit to database
            return True, f"ticket Edited Successfully {ticket}"
        except Exception as e:
            return False, f"ticket Edited Failed\n{e}"

    def delete(self, id):
        try:
        #     remove from database
            return True, f"ticket Removed Successfully - {id}"
        except Exception as e:
            return False, f"ticket Removed Failed\n{e}"


    def find_all(self):
        try:
            return True, ticket_list
        except Exception as e:
            return False, f"Can't Load ticket"


