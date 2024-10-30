# email = "ram@gmail.com"
# split_data = split ("@")
# print (split_data[1])


#  split
#  strip
#  Find 

# data = "hello how are you sita"
# print = "before replice (data)"
# changed_data = data.replace('sita','ram')
# print = "after  replice (changed_data)" 

# data = "i love veg food"
# changed_data =  data.replace('veg','non veg')
# print(changed_data) 

# data = "hello how are you sita"
# changed_data =  data.replace('sita','ram')
# print(changed_data)

# 1. find
# It appears you're trying to perform some basic string operations in Python. Here's a corrected and improved
#  version of your code:
      
#  split      

# user_email = "mohan@gmail.com"
# split_data =  user_email.split("@")
# print(split_data) 

user_email = "mohan@gmail.com"
split_data_first = user_email.split("@")
second_part = split_data_first[1]  # Output: mohan 
second_part =  second_part.split(".")
print(second_part)

# strip 

data = "hello world ASDF"
lower_data = data.lower()
print(lower_data)
