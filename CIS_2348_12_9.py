# Joshua Chan
# 1588459
list_for_input = []
name_number = ""
while(name_number != "-1"):
    name_number = input()
    if(name_number != "-1"):
        list_for_input.append(name_number)
# A list is created and the user input will be taken until '-1' where the loop will end
for i in list_for_input:
    final = []
    end = i.split(" ")
    for i in end:
        if(len(i)>0):
            final.append(i)
    try:
        print(final[0],end = " ")
        list_for_input = int(final[1])+1
        print(list_for_input,end = "\n")
# The number will increment by 1 and print
    except ValueError as vError:
        print(0,end = "\n")
# When the input contains string where it expects an integer, the output will be 0