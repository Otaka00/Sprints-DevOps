import sprints

list = [2.3, 3.4, 5.6, 9, 10, 15, 45, 0, 7, 90, 4]
result = sprints.MyFunc(list)
list2=[]
result2 = sprints.MyFunc(list2)
list3 = [2.8, 7.4, 55.8, 0.9, -0.10, 22, 33, 44, 15, 7]
result3 = sprints.MyFunc(list3)

assert result == (26, 5.6)
assert result2 ==0
assert result3 == (33,55.8)
print("All tests are passed")
