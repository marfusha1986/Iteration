num = 0
tot = 0.0
while True:
   pt = input('Enter a number:')
   if pt == 'done' :
       break
   try:
     kt = float(pt)
   except:
       print('Invalid input')
       continue
   print(kt)
   num = num + 1
   tot = tot +kt
print('All done')
print(tot, num, tot/num)