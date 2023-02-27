#inputs and other modifications
print('Watchout for the case of the names for the flames and for the birthday kindly follow this format "09/11/2002"')
name1 = list(input('name1:'))
a = ''.join(name1)
name2 = list(input('name2:'))
b = ''.join(name2)
bday1 = input('Birthday1:').split('/')            
bday2 = input('Birthday2:').split('/')
month1 = int(bday1[0])
day1 = int(bday1[1])
month2 = int(bday2[0])
day2 = int(bday2[1])


#For the name with Spaces
if  " " in name1:
    name1.remove(" ")
if  " " in name2:
    name2.remove(" ")
#remove the similar element within the two list
for i in name1:
    if i in name2:
        name1.remove(i)
        name2.remove(i)
res = len(name1) + len(name2)

#This will check the Result of two names in flames
flames = ['FRIENDS','LOVERS','AFFECTIONATE','MARRIAGE','ENEMIES','SOULMATE']
count = 0
while len(flames) > 1:
    for j in range(res):
        count += 1
        if len(flames) < count :
            count = 1
    flames.remove(flames[count-1])

#Check what's the first birthday's zodiac sign  
if month1 == 1:
    if day1 < 20:
        zodiac1 = 'Capricorn - Represses any emotion that gets in the way of success'
    else:
        zodiac1 = 'Aquarius - More in love with humanity as a whole than individuals'
if month1 == 2:
    if day1 < 20:
        zodiac1 = 'Aquarius - More in love with humanity as a whole than individuals'
    else:
        zodiac1 = 'Pisces - Can’t remember if they dreamt it or it actually happened'
if month1 == 3:
    if day1 < 21:
        zodiac1 = 'Pisces - Can’t remember if they dreamt it or it actually happened'
    else:
        zodiac1 = 'Aries - Gets angry, then forgets why they were angry' 
if month1 == 4:
    if day1 < 20:
        zodiac1 = 'Aries - Gets angry, then forgets why they were angry'
    else:
        zodiac1 = 'Taurus - All or nothing, no in between'
if month1 == 5:
    if day1 < 21:
        zodiac1 = 'Taurus - All or nothing, no in between'
    else:
        zodiac1 = 'Gemini - Knows a little about everything' 
if month1 == 6:
    if day1 < 21:
        zodiac1 = 'Gemini - Knows a little about everything'
    else:
        zodiac1 = 'Cancer - Forgives but never forgets'
if month1 == 7:
    if day1 < 23:
        zodiac1 = 'Cancer - Forgives but never forgets'
    else:
        zodiac1 = 'Leo - Really big personality'
if month1 == 8:
    if day1 < 23:
        zodiac1 = 'Leo - Really big personality'
    else:
        zodiac1 = 'Virgo - Judgmental, but with good intentions'
if month1 == 9:
    if day1 < 23:
        zodiac1 = 'Virgo - Judgmental, but with good intentions'
    else:
        zodiac1 = 'Libra - Conflict avoidant'
if month1 == 10:
    if day1 < 23:
        zodiac1 = 'Libra - Conflict avoidant'
    else:
        zodiac1 = 'Scorpio - OK with uncomfortable silence'
if month1 == 11:
    if day1 < 22:
        zodiac1 = 'Scorpio - OK with uncomfortable silence'
    else:
        zodiac1 = 'Sagittarius - Obsessed with self-improvement'
if month1 == 12:
    if day1 < 22:
        zodiac1 = 'Sagittarius - Obsessed with self-improvement'
    else: 
        zodiac1 = 'Capricorn - Represses any emotion that gets in the way of success'


#Check what's the second birthday's zodiac sign.
if month2 == 1:
    if day2 < 20:
        zodiac2 = 'Capricorn - Represses any emotion that gets in the way of success'
    else:
        zodiac2 = 'Aquarius - More in love with humanity as a whole than individuals'
if month2 == 2:
    if day2 < 20:
        zodiac2 = 'Aquarius - More in love with humanity as a whole than individuals'
    else:
        zodiac2 = 'Pisces - Can’t remember if they dreamt it or it actually happened'
if month2 == 3:
    if day2 < 21:
        zodiac2 = 'Pisces - Can’t remember if they dreamt it or it actually happened'
    else:
        zodiac2 = 'Aries - Gets angry, then forgets why they were angry' 
if month2 == 4:
    if day2 < 20:
        zodiac2 = 'Aries - Gets angry, then forgets why they were angry'
    else:
        zodiac2 = 'Taurus - All or nothing, no in between'
if month2 == 5:
    if day2 < 21:
        zodiac2 = 'Taurus - All or nothing, no in between'
    else:
        zodiac2 = 'Gemini - Knows a little about everything' 
if month2 == 6:
    if day2 < 21:
        zodiac2 = 'Gemini - Knows a little about everything'
    else:
        zodiac2 = 'Cancer - Forgives but never forgets'
if month2 == 7:
    if day2 < 23:
        zodiac2 = 'Cancer - Forgives but never forgets'
    else:
        zodiac2 = 'Leo - Really big personality'
if month2 == 8:
    if day2 < 23:
        zodiac2 = 'Leo - Really big personality'
    else:
        zodiac2 = 'Virgo - Judgmental, but with good intentions'
if month2 == 9:
    if day2 < 23:
        zodiac2 = 'Virgo - Judgmental, but with good intentions'
    else:
        zodiac2 = 'Libra - Conflict avoidant'
if month2 == 10:
    if day2 < 23:
        zodiac2 = 'Libra - Conflict avoidant'
    else:
        zodiac2 = 'Scorpio - OK with uncomfortable silence'
if month2 == 11:
    if day2 < 22:
        zodiac2 = 'Scorpio - OK with uncomfortable silence'
    else:
        zodiac2 = 'Sagittarius - Obsessed with self-improvement'
if month2 == 12:
    if day2 < 22:
        zodiac2 = 'Sagittarius - Obsessed with self-improvement'
    else: 
        zodiac2 = 'Capricorn - Represses any emotion that gets in the way of success'

#The compatibility of two zodiac sign
if 'Taurus' in zodiac1 and 'Aquarius' in zodiac2:
    comp = 'The Aquarius and Taurus have two distinctly different approaches to life and it is difficult for the duo to find middle ground amidst such stark dissimilarity. \nHowever, if Aquarius and Taurus really love each other and want to make their relationship work, there are a few things they can take care of to avoid \nunnecessary conflict and tension between them.'
elif 'Capricorn' in zodiac1 and 'Taurus' in zodiac2:
    comp = 'Capricorn and Taurusdeeply care about their work committments and they look for someone who can understand their goals and ambitions. Taurus is very similar to Capricorns; \nthey aim for comfort and are strikingly dedicated towards their professional and personal life as well.'
elif 'Aries' in zodiac1 and 'Sagittarius' in zodiac2:
    comp = 'Aries and Sagittarians are born for one another. While both these sunsigns cannot be contained or restricted \nto do what they like, they make sure that each has their private spaces.'
elif 'Scorpio' in zodiac1 and 'Leo' in zodiac2:
    comp = 'Scorpion and a Leo can accomplish everything they set their minds to. Their relentless passion and dominant personalities also help balance their arrogance and \nemotional ignorance, which can be very healthy in the long run.'
elif 'Libra' in zodiac1 and 'Gemini' in zodiac2:
    comp = 'Libra and Gemini enjoy each other’s company. Together they help each other grow and motivate one another to achieve wonderful things.'
elif 'Cancer' in zodiac1 and 'Pisces' in zodiac2:
    comp = 'Cancerians and Pisceans are one great combination of love-birds. With a Cancerian’s ability to feel love and passion, \na Piscean’s personality to give and endure makes for the best couple ever.'
elif 'Virgo' in zodiac1 and 'Taurus' in zodiac2:
    comp = 'A Taurean is all about his or her comfort zone. Besides loving the idea of loyalty, they are also about stability and security. \nThat being said, Virgos may be a little too critical in a relationship, but for a Taurean, they make for the perfect partner.'
elif 'Leo' in zodiac1 and 'Sagittarius' in zodiac2:
    comp = 'When it comes to a Leo and a Sagittarian, fun is what connects them together. Both are highly engaging and love to remain in the company of one another. \nWith Sagittarians charming demeanour and a Leos pleasing personality, both make for a wonderful yet fierce couple.'
elif 'Scorpio' in zodiac1 and 'Cancer' in zodiac2:
    comp = "corpio and Cancer feed off each other's passion, which allows them to work well when paired. They're also deeply devoted to one another and provide a terrific support system. \nBoth share very similar morals and are caring toward each other and those around them."
elif 'Pisces' in zodiac1 and 'Scorpio' in zodiac2:
    comp = "These two zodiac signs can get into each other's minds and know what they are thinking almost as well as if they were thinking it themselves. But they aren't just into intellect; \nthey both have a hunger to understand the other's body and soul and learn what makes the other person tick."
elif 'Cancer' in zodiac1 and 'Taurus' in zodiac2:
    comp = "The bonding that Taurus and Cancer share is very harmonious. No matter what their relation, both can be relied on for an abundance of emotional support. \nWhen Taurus digs in his heels or the Cancer is moody, matters might get a little patchy, but it is never long lasting."
elif 'Aries' in zodiac1 and 'Libra' in zodiac2:
    comp =  "Aries and Libra have surprisingly high love compatibility. They are both passionate signs, so they are going to be eager to please in the bedroom. \nThey both love sex and will be excited to touch one another. The attraction between these two signs will be undeniable."
else:
    comp = ('They are incompatible and unlucky')

#the result.
print(a, 'is a',zodiac1)
print(b, 'is a',zodiac2)
print(comp)
print()
print('FLAMES result: ', flames[0])
