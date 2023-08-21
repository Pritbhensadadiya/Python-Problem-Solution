import random 

print ("----------------------------------------------------------------------------------------")
print ("----------------------------------------------------------------------------------------")
when = ["A few years ago ", " Last night ", "On 11th December ","Yesterday "]
who = [ "a elephant " , "a man " ,  "a mouse ", "a lion " , "a cat "]
name = [" named dev " ," named yash " ,"named kunj " ,"named jash " ,"named sanjay " ]
country = ["from india ", "from USA ", "from pakistan ", "from canada ", "from france "]
went = ["went to the ground ", "went to the  cinema ","went to the collage ", "went to the garden ","went to the bus station "]
do = [  "and made lot of friends. ", "and eat pizza. ","and found something." , " and write a  book."]


print (random.choice(when)   + random.choice(who)   + random.choice(name)  + random.choice(country)+ random.choice(went) + random.choice(do))

print ("----------------------------------------------------------------------------------------")
print ("----------------------------------------------------------------------------------------")

