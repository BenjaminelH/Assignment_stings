# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player1 = 'Gullit'
player2 = 'Van Basten'

goal_1 = 32
goal_2 = 54

scorers = player1 +' ' +str(goal_1) +',' +' ' + player2 +' ' + str(goal_2)
print (scorers)

report = (
player1
+' '
+'scored in the'
+' '
+str(goal_1)
+'nd minute'
+'\n'
+player2
+' '
+'scored in the'
+' '
+str(goal_2)
+'th minute'
)
print (report)

name = 'Ronald Koeman'
first_name = name[name.find('Ronald'):6]
print (first_name)

last_name_len = len(name[name.find('K'):13])
print(last_name_len)


name_short = name[name.find('R')] +'.' +' ' + name[7:13]
print(name_short)

crowd = 'Go'
chant = (crowd+ ' ' +name[name.find('Ronald'):6]+'!'+' ')*6
print (chant.rstrip())

good_chant = chant[-1] != ' '
print (good_chant)
