
#this is question 1
import datetime

def my_function():
	now = datetime.datetime.now()
	print("Current date and time: ")
	print(str(now))



# this is question 2
def second_function():
	color_list_1 = {"White", "Black", "Red"}
	color_list_2 = {"Red", "Green"}
	print(color_list_1 - color_list_2)
	

# this is question 3
def add_digits(num):
        return (num - 1) % 9 +1  if num > 0 else 0



