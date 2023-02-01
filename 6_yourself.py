largest_value = None
#print('Before',largest_value)
for value in [5, 9, 56, 86, 65, 97, 12]:
   if largest_value is None or largest_value < value:
        largest_value = value
        print('Max:', largest_value)