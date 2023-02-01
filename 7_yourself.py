smallest_value = None
#print('Before',smallest_value)
for value in [5, 9, 56, 86, 65, 97, 12]:
   if smallest_value is None or smallest_value > value:
        smallest_value = value
        print('Min:', smallest_value)