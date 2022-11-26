def sum_list(the_list):
    if len(the_list)==0:
        return None
    else:
        sum=0
        for item in the_list:
            sum=item+sum
        return sum

my_list=[1,2,3]
print (sum_list(my_list))