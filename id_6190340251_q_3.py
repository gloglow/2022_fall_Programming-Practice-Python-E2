l=[1,2]
list_of_attributes_for_a_list=dir(l)
for _ in range(len(list_of_attributes_for_a_list)):
    list_of_attributes_for_a_list[_]=list_of_attributes_for_a_list[_].strip("_")
list_of_attributes_for_a_list=set(list_of_attributes_for_a_list)
for _ in list_of_attributes_for_a_list:
    print("tuples do not have"+" \'"+_+"\'")