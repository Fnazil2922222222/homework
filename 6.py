my_dict = {'Nazil': 1999, 'Alex': 2002}
print(my_dict)
print(my_dict.get('Nazil'))
print(my_dict.get('Anna'))
my_dict['Nastya'] = 1993
my_dict['Artur'] = 1986
print(my_dict.pop('Alex'))
print(my_dict)

my_set = {1, 1 , 1, 'Яблоко', '42.314'}
print(my_set)
my_set.add(13)
my_set.add((5, 6, 1.6))
my_set.remove(1)
print(my_set)