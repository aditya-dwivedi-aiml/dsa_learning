# K sum problems
# find the numbers which combine to give the target number
#O(N^2)

# Approach 1
input_var=[6,8,2,7,11,2]
target=9
for a in range(len(input_var)):
    tar=target-input_var[a]
    for b in range(len(input_var)):
        if b>a:
            if input_var[b]==tar:
                    print(a,b)
        else:
            pass


##Better Approch 2
# N(log(n))
input_var=[3,4,9,2]
temp_dict={}
target=6
for i in input_var:
    tar=target-i
    if tar in temp_dict.keys():
        print(input_var.index(i),temp_dict[tar])
    else:
        temp_dict[i]=input_var.index(i)
