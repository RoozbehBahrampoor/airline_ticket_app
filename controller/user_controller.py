from model.entity.user import  User

user_list = []

class UserController:
    def save(self,id,name,family,birth_date,user_name,password,is_locked,role ):
        try:
            user = User(id,name,family,birth_date,user_name,password,is_locked,role)
            user_list.append(user)
            return True, f"User Saved Successfully {user}"
        except Exception as e:
            return False, f"User Saved Failed\n{e}"


    def edit(self,id,name,family,birth_date,user_name,password,is_locked,role ):
        try:
            user1 = User(id,name,family,birth_date,user_name,password,is_locked,role)
        #     edit to database
            return True, f"User Edited Successfully {user1}"
        except Exception as e:
            return False, f"User Edited Failed\n{e}"

    def delete(self, id):
        try:
        #     remove from database
            return True, f"Uerson Removed Successfully - {id}"
        except Exception as e:
            return False, f"User Removed Failed\n{e}"


    def find_all(self):
        try:
            return True, user_list
        except Exception as e:
            return False, f"Can't Load  Users"


    # def find_by_name_and_family(self,name, family):