#
#  Python: 3.11.3
#
#  Author: Catherine Machado
#
#  Purpose:  
#
#

def start():
    f_name = "Catherine"
    l_name = "Machado"
    age = 19
    gender = "Female"
    get_info(f_name,l_name,age,gender)

def get_info(f_name,l_name,age,gender):
    print("My name is {} {}. I am {} year old {}.".format(f_name,l_name,age,gender))








if __name__ == "__main__":
    start()
