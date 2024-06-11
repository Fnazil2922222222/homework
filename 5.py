#immutable_var = ('1', '2', 'a', 'b') #кортежи - это объекты неизменяемого типа в python
#print(immutable_var)
#immutable_var[0] = 3
#print(immutable_var)
muttable_list = ['1', '2', 'a', 'b']
muttable_list[0] = 3
print(muttable_list)
muttable_list.append('Modified')
print(muttable_list)