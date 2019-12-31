# Sample code to read input and write output:

'''
name = input()                # Read input from STDIN
print("Hello " + name)        # Write output to STDOUT
'''

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail

# Write your code here


inp1 = input()

row,col,no_friend = inp1.split(" ")

row = int(row)
col = int(col)
no_friend = int(no_friend)

nest_lst = []
# for i in range(no_friend):
#     x = input()
#     temp = list(map(int, x.split()))
#     nest_lst.append(temp[1:])
#     # print(dic)

# print(nest_lst)

temp1 = []

for i in range(no_friend):
    x = input()
    temp = list(map(int, x.split()))
    for i in temp[1:]:
        temp1.append(i)

unique = []

for i in temp1:
    if i not in unique:
        unique.append(i)

print(len(unique))





