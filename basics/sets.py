# set = the same in math's set

# no dup item
# unordered
# unindexed

odd_no = { 1, 3, 5, 7, 9 }

odd_no.add(13)

odd_no.remove(13)

odd_no.update([9, 11, 13])

even_no = { 2, 4, 6, 8 }

my_num = even_no.union(odd_no)

# for num in odd_no:
#     print(num)

# for num in my_num:
#     print(num)

print(odd_no.difference(my_num))