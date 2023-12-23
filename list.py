#creat a python list contains duplicate values 
my_list=[1,2,3,4,4,5,6,7,7,8,8]
#creat a empty list
unique_list=[]
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)
    