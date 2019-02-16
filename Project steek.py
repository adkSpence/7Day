from sys import exit
import turtle as t 
import time
name = raw_input("Please enter your name: \a\n> ")

print "Welcome", name, "Ready to learn and have some fun?"
print "Hit RETURN to continue or CTRL -C to quit..."
raw_input()

print """On a beautiful Saturday afternoon, you decide to go for a walk.
The walk is a pleasant one but nothing far fetched from the normal
walks you have been having but this time you feel an aura, a
strange one for the matter. The only problem is you really can't tell if
it is good or bad. Anyways "In Omnia Paratus!", Ready for Anything.
"""

print "After hours of walking and reflecting, you come to a crossroad."
print """\nTo your left is Ave Marie Avenue and to your right is Euclid Avenue.
You have heard of so many things concerning these streets.Do you continue on thepath that leads home or out of curiousity take one of these paths to see what lies beyond. What do you do?
"""

def Crossroads():
	choice = raw_input("\a> ")
	
	if "ave marie" in choice:
		FirstSet()
	elif "euclid avenue" in choice:
		SecondSet()
	else:
		End("You have no sense of adventure")

def FirstSet():
	print """\nYou choose to follow the Ave Marie road.
As you go deeper you hear screams coming from an abandoned house.
It catches your attention so you move towards the building. 
The screams are of a feminine tone. 
Should you run away or go inside to help her?  
"""
	choice = raw_input("What do you do? \a\n> ")

	if "go inside" in choice:
		FirstRid()
	elif "run away" in choice:
		End("for you cowardly act, the girl dies within the building. Turns out, she was Candace, your beloved sister")

def End(statement):
	print name, statement
	exit(0)

def FirstRid():
	print """'They say the few who do are the envy of the many who watch.'
Acting all courageous, you step up and open the door.
Now you can hear the screams louder than ever. You see a door.
The screams are probably coming from there. You get to the door and try to open it.
It's locked. By accident, it looks like you triggered some sort of time bomb. Its all a trap.
On the door is an electronic screen which displays.....
"""
	print """\nYou only get one try to answer this riddle.
If you solve it correctly, the door will be unlocked.
In contrast, a wrong answer will trigger the bomb tied to the girl inside the room to explode.
You have 20 seconds to prepare for the riddle.
"""
	
	time.sleep(20)
#	print """I look at you, 
#you look at me, 
#I raise my right, 
#you raise your left.
#What object am I?
#"""
	print "How many squares do you see below?"

	t.shape("turtle")
	def squares(length):
	    for i in range(4):
	        t.fd(length)
	        t.left(90)

	t.color("red","green")
	squares(50)
	t.color("#66CCCC")
	squares(100)
	t.color("yellow")
	squares(150)
	t.color("black")
	squares(200)

	t.penup()
	t.setpos(70, 58)
	t.setpos(100, 100)
	t.pendown()
	t.color("orange")
	t.circle(-50)
	t.color("brown")
	t.circle(50)

	answer = 8
	print "%s, What's your answer?" % name
	choice = raw_input("\a> ")

	if choice in answer:
		print "\nAwesome. You unlock the door."
		FinalPhase()
	else:
		End("You tried but couldn't save her. Unfortunately, the girl was Candace, your beloved sister")

def FinalPhase():
	print """\nOh goodness gracious! It's Candace, your sister.
How did she get here. But this is not the time for questions.
You quickly untie her hands and legs and you help her up. She thanks you in a weak voice.
You move quickly out of that room and head for the exit. Upon reaching there it looks like
your opening of the door that had Candace in it, caused a lockdown of the main door. Again,
you see another prompt. This one unlike the previous one, will trigger a bomb that will 
cause the whole building to explode. You have 20 seconds to prepare again.
"""

	time.sleep(20)
	print """Jack and Jill are lying on the floor inside the house, dead. 
They died from lack of water.
There is shattered glass next to them.
How did they die?
"""
	answer = "goldfishes"
	print "%s, You can not afford to get this wrong. Candace tells you."
	choice = raw_input("One last riddle to freedom. What's your answer? \a\n> ")

	if choice in answer:
		print "Yay!!! Congratulations, you unlocked the main gate. You saved your sister and you guys are free."
		exit(0)
	else:
		End("You tried. Anyways, you died a hero")
		exit(0)

def SecondSet():
	print """\nSweet choice. Goodness gracious!!! 
Going up this street, you feel an aura of mixed feelings. 
As you continue organizing your emotions, you come across a treehouse.
This treehouse triggers nostalgic memories, you are drawn to it. 
After you climb into the treehouse you recognize the door left ajar. 
Piques your interest so you go inside. Place looks very whimsical.
Now there are 2 giant doors. One contains a very beautiful girl screaming for you to rescue her.
On the other side is a treasury chest of gold. Pheeeeeewww!!! Is this supposed to even be a conundrum?
The girl is very pretty but who knows she could be bait. You also need the money, your family does.
You have only one chance. Save girl or Get money?
What do you do?
"""
	choice = raw_input("\n\a> ")

	if "save girl" in choice:
		BeautifulGirl()
	elif "get money" in choice:
		Riches()

def BeautifulGirl():
	print """\nYou really can't bring yourself to the thought of choosing money over the girl.
Whether it is bait or not, you are still going to help her out. As you approach the door and try to unlock it,
you realize it is locked. All of a sudden, you receive a message from the screen infront of the giant door.
It reads, "you have only one chance to answer this riddle correctly. Right answer unlocks the door and wrong breaks
poisonous gas. You have 20 seconds to prepare for it"
"""

	time.sleep(20)
	print """\n\aIf a rooster laid a brown egg and a white
egg, what kind of chicks would hatch?
"""
	answer = "roosters don't lay eggs"

	choice = raw_input("Your answer? \n> ")

	if choice in answer or "roosters can't lay eggs" in choice:
		print "Look at that. You answered correctly"
		FinalEscape()
	else:
		End("wrong answer. The gas is released, the girl dies, the room with the gold locks down permanently. You lose")

def Riches():
	print """\nFor all you know, the girl could be used as bait to trap you too.
You decide to play it safe so you go in for the money. That is very greedy of you
but hey, you need the money for the kidney transplant your parents can't afford to get for Leo, your kid brother.
\nNow as you try to unlock the door into the room with the gold, you find its locked
And unto the screen appears this strange message and it reads, 
"you have only one chance to answer this riddle correctly. Right answer unlocks the door and wrong permanently
locks the door. You have 20 seconds to prepare for the riddle"
"""

	time.sleep(20)
	print"""You answer me
Though I never ask you any questions
Who am I?
"""
	answer = "telephone"
	choice = raw_input("\n\a> ")

	if "a telephone" in answer or choice in answer:
		print "Great! Correct answer. You hear a click, the door is unlocked now."
		FinalEscape2()
	else:
		print End("Wrong answer. All your hopes shattered. You go back home but never again do you feel like yourself. Game over")

def FinalEscape():
	print """\nNice you get into the room and you quickly untie the girl.
Whoaa such a beautiful girl. Well if love at first sight is a real thing, it just caught you.
She tells you her name is Rebecca is a very glad you decided to choose her over the money.
You tell her not to mention it and hastily ask her out on a date. She laughs and says well we can't have a date in here.
You laugh and say yeah well let's get out of this hell hole. Surprisingly, the door leading to the outside locked down
as you opened the door that Rebecca was contained in. As you attempt to open it, you see a similar prompt.
Whoosh!!! Again you have 20 seconds. Correct answer you are free. Wrong answer, you are both trapped till the captor arrives.
"""

	time.sleep(20)
	print """He has married many women but has never married.
Who is he?
"""
	
	answer = "priest"
	choice = raw_input("\n\a> ")
	
	if choice in answer:
		End("Wow. Smart guy. The door unlocks and into the free world you step with a girl soon to become your Queen")
	else:
		End("Sorry but you get trapped and soon the captor will arrive. yeah well if only you opted for the gold rather? but who knows. GAME OVER")

def FinalEscape2():
	print """\nSo you successfully get into the room and you quickly gather as much gold as you can.
Fortunately there is a bag in which you can put all in it. After you feel content with how much you have collected,
you head for the door only to realize that it locked the very moment you opened the door leading to the gold.
A similar prompt appears on the door leading to the outside world. Again, you have only 20 seconds to prepare."""

	time.sleep(20)
	print "What can fill a room but takes up no space?"

	answer = "light"
	choice = raw_input("\n\a> ")

	if choice == answer:
		End("beautiful. You successfully escape with the money but leaving the girl behind torments you forever.")
	else:
		End("your failure to open the door leads you to being trapped permanently till the captor comes. Sorry")

Crossroads()
input()