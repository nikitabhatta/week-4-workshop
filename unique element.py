#new list containing unique elements

l=[1,1,2,3,3,4,4,5,6,5,6]


unique_list=list(set(l))

desc_list=[]

for i in range(len(unique_list)-1,-1,-1):
    desc_list.append(unique_list[i])

print(desc_list)
