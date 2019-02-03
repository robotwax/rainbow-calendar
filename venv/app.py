# -*- coding: UTF-8 -*-

import json
import itertools

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import datetime
from datetime import timedelta
import numpy as np
import numpy.ma as ma
import plotly.plotly as py


d = datetime.datetime.now()
d1 = d.date()
from datetime import date
d0 = date(2010, 10, 25)
d4 = d-timedelta(days=19)
d5 = d+timedelta(days=19)
d10 = str(d1)
delta = d1 - d0
d2 = delta.days
delta2 = d5 - d4
ba = []
for i in range(delta2.days +1):
    ba.append(d4 + timedelta(i))

#text
import numpy as nd
a = nd.array(['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'] * 38)
b = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 6, 4, 7, 3, 8, 2, 9, 1,
     10, 9, 1, 8, 2, 7, 3, 6, 4, 5, 5, 4, 6, 3, 7, 2, 8, 1, 9]
e = int(d2/200)
y1 = (-3 * e)
a = nd.roll(a, y1, axis=0)
a = a.tolist()
c = []
for x, y in zip(a, b):
    c.extend([x] * y)
g = d2 % 200
gb = d2 % 200
gx = g - 1
def func(gb):
    if gb == 0:
        return('Today is ', c[-1])
    else:
        return('Today is ', c[gx])
gc = func(gb)
def func(g):
    if g == 0:
        return(200)
    else:
        return(g)
f = (func(g))
x0 = f - 1
xx0 = x0

#x/y axis

b0 = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 6, 4, 7, 3, 8, 2, 9, 1,
      10, 9, 1, 8, 2, 7, 3, 6, 4, 5, 5, 4, 6, 3, 7, 2, 8, 1, 9]
cb = []
for x, y in zip(a, b0):
    cb.extend([x] * y)
b2 = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 6, 4, 7, 3, 8, 2, 9, 1,
      10, 9, 1, 8, 2, 7, 3, 6, 4, 5, 5, 4, 6, 3, 7, 2, 8, 1, 9]
axb = nd.array(a)
def func(xx0):
    if 0 <= xx0 <= 18:
        k = e - 1
        y1 = (-3 * k)
        axa = nd.roll(axb, y1, axis=0)
        akk = axa.tolist()
        n1 = []
        for x, y in zip(akk, b2):
            n1.extend([x] * y)
        cc=(n1 + cb)
        o1 = xx0 + 200
        o2 = o1 - 19
        p1 = cc[o2:]
        kk1= o1 + 20
        q1 = cc[o2:kk1]
        return(q1)
    elif 180 <= xx0 <= 199:
        m = e + 1
        y1 = (-3 * m)
        axa = nd.roll(axb, y1, axis=0)
        akk = axa.tolist()
        n1 = []
        for x, y in zip(akk, b2):
            n1.extend([x] * y)
        t2 = cb + n1
        r1 = xx0 + 19
        r33 = xx0 - 19
        t1 = t2[r33:r1+1]
        return(t1)
    else:
        u1 = xx0 - 19
        v1 = xx0 + 19
        w1 = cb[u1:v1+1]
        return(w1)
dc = (func(xx0))
import numpy as np
aa = [1, 2, 3, 4, 5, 6, 7] * 38
b3 = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 6, 4, 7, 3, 8, 2, 9, 1,
      10, 9, 1, 8, 2, 7, 3, 6, 4, 5, 5, 4, 6, 3, 7, 2, 8, 1, 9]
y1 = (-3 * e)
a44 = np.array(aa)
a55 = np.roll(a44, y1, axis=0)
a5 = a55.tolist()
ca = []
for x, y in zip(a5, b3):
    ca.extend([x] * y)
x1 = f - 1
axc = nd.array(aa)
def func(x0):
    if 1 <= x0 <= 18:
        k = e - 1
        y2 = (-3 * k)
        axa = np.roll(axc, y2, axis=0)
        asa = axa.tolist()
        n = []
        for x, y in zip(asa, b3):
            n.extend([x] * y)
        t4 = n + ca
        o1 = x0 + 200
        r19 = o1 - 19
        r35 = o1 + 20
        p35 = t4[r19:r35]
        return(p35)
    elif 180 <= x0 <= 199:
        m = e + 1
        y2 = (-3 * m)
        axa = np.roll(axc, y2, axis=0)
        aga = axa.tolist()
        n = []
        for x, y in zip(aga, b3):
            n.extend([x] * y)
        t2 = ca + n
        r11 = x0 + 19
        r34 = x0 - 19
        t1 = t2[r34:r11+1]
        return(t1)
    else:
        u = x1 - 19
        v = x0 + 19
        w = ca[u:v]
        return(w)
ab = (func(x0))
bc = e * 200
bd = d2 - bc
be = 200 - bd
bf = ('Date today; %s' %(d10))
def func(bd):
    if bd != 1 and bd !=0:
        return((bd),'-days have elapsed since the beginning of the current cycle')
    elif bd == 1:
        return('This is the first day of a new cycle')
    else:
        return('This is the last day of this cycle')
bg = (func(bd))
def func(be):
    if be > 1:
        return('There are ', (be), '-days left in this cycle')
    else:
        return()
bh = (func(be))

#info

One=['''One:

The number 1 is all about ‘beginnings’. You like to take the initiative. Those born with this value are generally positive and active. This number covers all “firsts”: first impressions, the self and appearance, leadership, new initiatives, fresh starts and beginnings.

''']

Red= ['''Red

Ruling Chakra: Muladhara

Root Chakra — Represents our foundation and feeling of being grounded.
Location: Base of spine in tailbone area.
Emotional issues: Survival issues such as financial independence, money and food.
''']

xix = itertools.chain(One, Red)
xox=list(xix)

        
Two = ['''Two:

 This number rules all matters related to your immediate material and physical environment—taste, smells, sound, touch, sights, making you a very sensual person. Two also rules matters to do with income, money, and self-esteem. You like to be secure in these areas. Positive attributes; balance. Negative attributes; delays, waiting.

''']

Orange = ['''Orange

Ruling Chakra: Swadhisthana

Sacral Chakra — Our connection and ability to accept others and new experiences.
Location: Lower abdomen, about two inches below the navel and two inches in.
Emotional issues: Sense of abundance, well-being, pleasure and sexuality.
''']



Three = ['''Three:

Three rules all forms of communication—talking, thinking, gadgets and devices (cell phones, pagers, Instant Messenger, etc.). The number three also covers siblings, neighbourhoods, local travel, libraries, schools, teachers and community affairs. Connection (or division, mixed-up communication, plans gone awry. 

''']

Yellow = ['''Yellow

Ruling Chakra: Manipura
    
Solar Plexus Chakra — Our ability to be confident and in control of our lives.
Location: Upper abdomen in the stomach area.
Emotional issues: Self-worth, self-confidence and self-esteem.
''']

Four=['''Four:

Four refers to foundation; your home, privacy, your basic security, your parents, children, nurturing. These are things that are important to you. Positive attributes; stability. Negative attribute; feeling stuck. 

''']

Five= ['''Five:

Five governs creativity, dynamism, and a war-like spirit. The number five is all about challenges and these challenges that can lead to expansion.

''']

Green = ['''Green

Ruling Chakra: Anahata

Heart Chakra — Our ability to love.
Location: Center of chest just above the heart.
Emotional issues: Love, joy and inner peace.''']

Six = ['''Six:

Harmony (or the lack of or yearning for it, but sixes are rarely negative). Six is the domain of health and service. It rules schedules, organisation, routines, fitness, diet and exercise, natural and healthy living, helpfulness and being of service to others.

''']

Blue = ['''Blue

Ruling Chakra: Vishudda

Throat Chakra — Our ability to communicate.
Location: Throat.
Emotional issues: Communication, self-expression of feelings and the truth.
''']


Seven = ['''Seven:

Seven is the sector of relationships and other people. It governs all partnerships, both business and personal, and relationship-associated matters, like contracts, marriage, and business deals. Postive attrubtes; Mystery. Negative attribute; Being overly concerned with superficialities. 

''']

Indigo = ['''Indigo

Ruling Chakra: Ajna

Third Eye Chakra — Our ability to focus on and see the big picture.
Location: Forehead between the eyes (also called the Brow Chakra).
Emotional issues: Intuition, imagination, wisdom and the ability to think and make decisions.
''']


Eight = ['''Eight:

Eight is a mysterious number that rules birth, death, sex, transformation, mysteries, merged energies, and bonding at the deepest level. Eight also rules other people’s property and money (real estate, inheritances, investments, et. al.) Positive attributes; Movement. Negative attributes; Lack of movement, Stagnation.

''']

Violet = ['''Violet

Ruling Chakra: Sahasrara

Crown Chakra — The highest chakra represents our ability to be fully connected spiritually.
Location: The very top of the head.
Emotional issues: Inner and outer beauty, our connection to spirituality and pure bliss.
''']

Nine = ['''Nine:

Nine covers the higher mind, expansion, international and long-distance travel, foreign languages, inspiration, optimism, publishing, broadcasting, universities and higher education, luck, risk, adventure, gambling, religion, philosophy, morals and ethics. Positive attributes; Growth. Negative attributes;  Satiety.

''']
Ten = ['''Ten:

Ten governs structures, corporations, tradition, public image, fame, honours, achievements, awards, boundaries, rules, discipline, authority, fathers and fatherhood. Positve attributes; Completion (new beginnings). Completion. Negative attributes: Destructive. 

''']

#Historic dates

colour_dates = nd.array(['0', 'Yellow', 'Green', 'Orange', 'Green', 'Yellow', 'Violet', 'Indigo', 'Indigo', 'Green', 'Blue', 'Indigo', 'Orange', 'Blue', 'Red', 'Blue', 'Blue', 'Blue', 'Indigo', 'Red', 'Violet', 'Red', 'Violet', 'Yellow', 'Orange', 'Yellow', 'Indigo', 'Yellow', 'Blue', 'Indigo', 'Green', 'Red', 'Green', 'Yellow', 'Green', 'Red', 'Blue', 'Indigo', 'Green', 'Yellow', 'Blue', 'Yellow', 'Yellow', 'Orange', 'Blue', 'Yellow', 'Red', 'Yellow', 'Indigo', 'Violet', 'Red', 'Red', 'Red', 'Green', 'Indigo', 'Red', 'Indigo', 'Green', 'Green', 'Violet', 'Green', 'Violet', 'Green', 'Indigo', 'Indigo', 'Green', 'Indigo', 'Yellow', 'Green', 'Blue', 'Yellow', 'Blue', 'Violet'])

dates= nd.array(['0', '18 April 1980 Zimbabwe; Rhodesia gains independence', '24 April 1980 Commando raid to rescue hostages in Teheran fails', '18 May 1980 Mount St. Helens erupts', '22 September 1980 Iraq invades Iran', '12 August 1981 Personal computer launched by IBM', '6 October 1981 President Anwar Sadat assassinated in Cairo', '1 March 1982 Venera 13 sends first colour photos from Venus', '2 April 1982  Argentine forces mounted amphibious landings on the Falkland Islands', '6 June 1982 Israel invades Lebanon', '4 April 1983 Maiden voyage of US Space Shuttle Challenger', '13 May 1984 Explosion destroys a third of the Soviet Northern Fleet’s surface-to-air missiles', '3 December 1984 The Bhopal disaster also referred to as the Bhopal gas tragedy', '23 June 1985  Air India Flight 182 disaster passenger jet explosion off the coast of Ireland', '19 September 1985 Mexico City earthquake', '15 November 1985 the UK and Ireland sign the Anglo-Irish Treaty', '28 January 1986 Challenger disaster', '28 February 1986 Prime Minister of Sweden Olof Palme was shot dead', '13 March 1986 Europes Giotto space probe passed closest to the nucleus Halley\’s Comet', '26 April 1986 Chernobyl disaster', '19 October 1987 Black Monday', '2 November 1988 Internet virus jams over 6000 military computers', '7 December 1988 Armenian earthquake', '21 December 1988 Lockerbie bombing', '25 December 1991 Gorbachev resigns as president', '1 January 1993  The European Single Market begins', '26 February 1993 WTC bombing', '19 April 1993 Waco siege ends', '17 January 1994 Northridge earthquake; Los Angeles', '22  July 1994 The last fragments of Comet P/Shoemaker-Levy 9 collided with Jupiter', '17 January 1995 Kobe earthquake', '19 April 1995 Oklahoma bombing', '4 November 1995 Israeli Prime Minister Rabin assassinated', '22 February 1997 Dolly the sheep announced to public', '10 April 1998 The Good Friday Agreement', '31 October 1999 EgyptAir flight MS804 crashes over Atlantic', '1 January 2000 Y2K bug fails to happen', '12 February 2001 the NASA NEAR Shoemaker spacecraft lands on asteroid 433 Eros', '11 September 2001 9/11 Attacks', '1 February 2003 US Space Shuttle Columbia breaks up on reentry', '20 March 2003  Iraq War The invasion phase', '3 January 2004 Mars Rover Spirit lands on Mars', '11 March 2004 The Madrid Train Bombings', '26 December 2004 Boxing day Tsunami', '14 January 2005 the Huygens probe lands on Titan', '7 July 2005 7/7 Attacks London', '15 September 2008 Lehman Brothers goes bust', '4 November 2008 Obama elected POTUS', '11 March 2010 Japan tsunami', '20 April 2010  The Deepwater Horizon oil spill', '26 October 2010 Rainbow Calendar C-14 begins', '2 May 2011 Osama bin Laden was officially declared dead', '7 May 2012  The first licenses for cars without drivers is granted in the state of Nevada to Google', '11 September 2012  Terrorist attack on a consulate in the Libyan city of Benghazi kills four Americans', '29 October 2012  Hurricane Sandy', '6 November 2012  President Barack Obama wins a significant victory; 332 electoral votes to 206 for his second term in office', '12 February 2013  Using a 3D printer and cell cultures American scientists at Cornell University grow a living ear', '15 April 2013  Two bombs explode near the finish line of the Boston Marathon killing three and injuring hundreds in a terrorism attack', '1 January 2014  Obamacare; the Affordable Care Act goes into affect', '26 February 2014 Russian Federation annexes the Ukrainian territory of Crimea', '5 June 2014  Rise of ISIS', '30 September 2014  First case of Ebola is certified in the United States', '25 April 2015  Baltimore Riots', '20 July 2015  Full diplomatic relations are reestablished between the United States and Cuba for the first time in fifty-four years', '22 September 2015  Pope Francis makes his first visit to the United States holding services in Washington New York City and Philadelphia. This was the first papal visit to the U.S.A. since Pope Benedict XVI in 2008 and only the fourth pope to ever visit the United States', '2 December 2015  Islamic Terrorist inspired act in San Bernadino; California kills fourteen and follows a brutal attack against citizens in Paris in November', '12 June 2016  Terrorist attack in Orlando; Florida', '28 November 2016  Donald Trump wins presidential election', '11 February 2017  North Korea fires ballistic missile over the Sea of Japan', '30 March 2017  SpaceX; the private aeronautic firm engages in first reflight of an orbital class rocket', '1 June 2017  United States withdraws from the Paris Climate Agreement', '25 August 2017  Disastrous hurricane season in the Gulf of Mexico; Caribbean; and Atlantic seaboard begins with Hurricane Harvey', '22 December 2017  President Trump signs the largest tax cut since 1986'])

category=nd.array(['0', 'Political Unrest', 'Terrorism', 'Natural disaster', 'War', 'Technological Innovation', 'Political Unrest', 'Space Exploration', 'War', 'War', 'Space Exploration', 'Manmade disaster', 'Manmade disaster', 'Transportation disaster', 'Natural disaster', 'Political agreement', 'Transportation disaster', 'Political Unrest', 'Space Exploration', 'Manmade disaster', 'Financial crash', 'Manmade disaster', 'Natural disaster', 'Terrorism', 'Political change', 'Political change', 'Terrorism', 'Political Unrest', 'Natural disaster', 'Space Exploration', 'Natural disaster', 'Terrorism', 'Political Unrest', 'Technological Innovation', 'Political agreement', 'Transportation disaster', 'Manmade disaster', 'Space Exploration', 'Terrorism', 'Manmade disaster', 'War', 'Space Exploration', 'Terrorism', 'Natural disaster', 'Space Exploration', 'Terrorism', 'Financial crash', 'Political change', 'Natural disaster', 'Manmade disaster', 'Technological innovation', 'Political Unrest', 'Technological innovation', 'Terrorism', 'Natural disaster', 'Political change', 'Technological innovation', 'Terrorism', 'Political change', 'War', 'War', 'Natural disaster', 'Political Unrest', 'Political agreement', 'Political agreement', 'Terrorism', 'Terrorism', 'Political change', 'Political Unrest', 'Technological Innovation', 'Political change', 'Natural disaster', 'Political change'])

from datetime import date
d13 = date(1980, 2, 26)
d14 = date(1983, 12, 26)
delta15 = d14 - d13
d16 = delta15.days

d17 = []
for i in range(d16 + 1):
    d17.append(d13 + timedelta(i))

d18 = date(1983, 12, 27)
d19 = date(1987, 10, 27)
delta20 = d19 - d18
d21 = delta20.days

d22 = []
for i in range(d21 + 1):
    d22.append(d18 + timedelta(i))
    
d23 = date(1987, 10, 28)
d24 = date(1991, 8, 27)
delta25 = d24 - d23
d26 = delta25.days

d27 = []
for i in range(d26 + 1):
    d27.append(d23 + timedelta(i))
    
d28 = date(1991, 8, 28)
d29 = date(1995, 6, 27)
delta30 = d29 - d28
d31 = delta30.days

d32 = []
for i in range(d31 + 1):
    d32.append(d28 + timedelta(i))

d33 = date(1995, 6, 28)
d34 = date(1999, 4, 27)
delta35 = d34 - d33
d36 = delta35.days

d37 = []
for i in range(d36 + 1):
    d37.append(d33 + timedelta(i))

d38 = date(1999, 4, 28)
d39 = date(2003, 2, 25)
delta40 = d39 - d38
d41 = delta40.days

d42 = []
for i in range(d41 + 1):
    d42.append(d38 + timedelta(i))

d43 = date(2003, 2, 26)
d44 = date(2006, 12, 26)
delta45 = d44 - d43
d46 = delta45.days

d47 = []
for i in range(d46 + 1):
    d47.append(d43 + timedelta(i))

d48 = date(2006, 12, 27)
d49 = date(2010, 10, 26)
delta50 = d49 - d48
d51 = delta50.days

d52 = []
for i in range(d51 + 1):
    d52.append(d48 + timedelta(i))

z1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 7, 7, 7, 7, 7, 7, 7, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 7, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 7, 7, 7, 7, 7, 7, 7, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7]

b = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 6, 4, 7, 3, 8, 2, 9, 1,
 10, 9, 1, 8, 2, 7, 3, 6, 4, 5, 5, 4, 6, 3, 7, 2, 8, 1, 9]

a8 = nd.array(['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'] * 38)
a8 = a8.tolist()
r = []
for x, y in zip(a8, b):
    r.extend([x] * y)
a9 = nd.array(['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'] * 38)
a9 = np.roll(a9, -3, axis=0)
a9 = a9.tolist()
r1 = []
for x, y in zip(a9, b):
    r1.extend([x] * y)
k1 = r + r1
a10 = nd.array(['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'] * 38)
a10 = np.roll(a10, -6, axis=0)
a10 = a10.tolist()
r2 = []
for x, y in zip(a10, b):
    r2.extend([x] * y)
k2 = k1 + r2
a11 = nd.array(['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'] * 38)
a11 = np.roll(a11, -9, axis=0)
a11 = a11.tolist()
r3 = []
for x, y in zip(a11, b):
    r3.extend([x] * y)
k3 = k2 + r3
a12 = nd.array(['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'] * 38)
a12 = np.roll(a12, -12, axis=0)
a12 = a12.tolist()
r4 = []
for x, y in zip(a12, b):
    r4.extend([x] * y)
k4 = k3 + r4
a13 = nd.array(['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'] * 38)
a13 = np.roll(a13, -15, axis=0)
a13 = a13.tolist()
r5 = []
for x, y in zip(a13, b):
    r5.extend([x] * y)
k5 = k4 + r5
a14 = nd.array(['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'] * 38)
a14 = np.roll(a14, -18, axis=0)
a14 = a14.tolist()
r6 = []
for x, y in zip(a14, b):
    r6.extend([x] * y)
m = k5 + r6

import plotly.plotly as py
import plotly.graph_objs as go

from plotly.graph_objs import *

app = dash.Dash(__name__)

app.config['suppress_callback_exceptions'] = True
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

server = app.server

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
    <head>
	<meta charset="utf-8">
	
	<title>Rainbow Calendar C-14</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
    <footer>
        {%config%}
        {%scripts%}
        
    </footer>
    </body>
</html>
'''


styles = {
    'hr': { 
    'display': 'block',
    'margin-top': '0.1rem',
    'margin-bottom': '0.1rem',
    'margin-left': 'auto',
    'margin-right': 'auto',
    'border-style': 'inset',
    'border-width': '0.1rem'}
}


app.layout = html.Div(children=
      html.Div([
            html.Div([
                  html.H1('Rainbow Calendar C-14',
                  className = "six columns"),
                  html.Img(
                        src="/assets/rainbow_dash4.png",
                        className = 'six columns', style={'height': '30%', 'width': '25%', 'float': 'right', 'margin-right': 5},
                  ),
                  html.H4(gc,
                  className = "six columns", style={'float': 'left', 'margin-left': 0},
                  ),
            ], className = "row"),          
            html.Hr(id='graph1', style=styles['hr']),
            html.Div([
                      dcc.Graph(
                                id='Rain-Cal-C14',
                                figure={
                                'data': [
                                         go.Scatter(
                                                    x=ba,
                                                    y=ab[:],
                                                    text= dc[:],
                                                    mode='markers+lines',
                                                    opacity=0.7,
                                                    marker={
                                                    'size': 13,
                                                    'line': {'width': 1},
                                                    'symbol': 'octagon',
                                                    'autocolorscale': False,
                                                    'cauto': True,
                                                    'cmax': 7,
                                                    'cmin': 1,
                                                    'color': ab[:],
                                                    'colorscale': [[0, "#ff0000"], [0.142857142857143, "#ffae01"], [0.3333333333333, "#fff600"], [0.5555555555555, "#0aff04"], [0.6666666666666, "#0569ff"], [0.777777777777, "#a201ff"], [0.8888888888888, "#ff03ea"], [1.0000000, "#ff03ea"]],
                                                    'colorsrc': "robotwax:157:00284a",
                                                    'reversescale': False,
                                                    'showscale': True,
                                                    },
                                                    ),
                                         ],
                                'layout': go.Layout(
                                                    {'title': 'Rainbow Calendar C-14'},
                                                    images= [
                                                             {
                                                             "x": 0.5,
                                                             "y": 0.5,
                                                             "layer": "below",
                                                             "sizex": 1,
                                                             "sizey": 1,
                                                             "sizing": "stretch",
                                                             "source": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABLkAAAMZCAYAAADsgOatAAAACXBIWXMAAAsTAAALEwEAmpwYAAA53GlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4KPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS41LWMwMjEgNzkuMTU1NzcyLCAyMDE0LzAxLzEzLTE5OjQ0OjAwICAgICAgICAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iCiAgICAgICAgICAgIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIKICAgICAgICAgICAgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIgogICAgICAgICAgICB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIKICAgICAgICAgICAgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIKICAgICAgICAgICAgeG1sbnM6dGlmZj0iaHR0cDovL25zLmFkb2JlLmNvbS90aWZmLzEuMC8iCiAgICAgICAgICAgIHhtbG5zOmV4aWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vZXhpZi8xLjAvIj4KICAgICAgICAgPHhtcDpDcmVhdG9yVG9vbD5BZG9iZSBQaG90b3Nob3AgQ0MgMjAxNCAoTWFjaW50b3NoKTwveG1wOkNyZWF0b3JUb29sPgogICAgICAgICA8eG1wOkNyZWF0ZURhdGU+MjAxOC0xMS0wM1QxNTowOTo1OVo8L3htcDpDcmVhdGVEYXRlPgogICAgICAgICA8eG1wOk1vZGlmeURhdGU+MjAxOC0xMS0wM1QxNToxODoyMlo8L3htcDpNb2RpZnlEYXRlPgogICAgICAgICA8eG1wOk1ldGFkYXRhRGF0ZT4yMDE4LTExLTAzVDE1OjE4OjIyWjwveG1wOk1ldGFkYXRhRGF0ZT4KICAgICAgICAgPGRjOmZvcm1hdD5pbWFnZS9wbmc8L2RjOmZvcm1hdD4KICAgICAgICAgPHBob3Rvc2hvcDpDb2xvck1vZGU+MzwvcGhvdG9zaG9wOkNvbG9yTW9kZT4KICAgICAgICAgPHhtcE1NOkluc3RhbmNlSUQ+eG1wLmlpZDo3Y2IzYzk4NS1iMTVlLTQ0OTctODNkYi05NmVjZTk0NThlMGM8L3htcE1NOkluc3RhbmNlSUQ+CiAgICAgICAgIDx4bXBNTTpEb2N1bWVudElEPmFkb2JlOmRvY2lkOnBob3Rvc2hvcDoxYTNjOTIzNS0yMDBhLTExN2MtOGFjYi1iMzc1ZDdmNWM1ZTM8L3htcE1NOkRvY3VtZW50SUQ+CiAgICAgICAgIDx4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ+eG1wLmRpZDoxNDQ1YzZiNS1mN2I4LTRmNTUtYThiYi1mZDU2ZTQ2YzgzODk8L3htcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD4KICAgICAgICAgPHhtcE1NOkhpc3Rvcnk+CiAgICAgICAgICAgIDxyZGY6U2VxPgogICAgICAgICAgICAgICA8cmRmOmxpIHJkZjpwYXJzZVR5cGU9IlJlc291cmNlIj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OmFjdGlvbj5jcmVhdGVkPC9zdEV2dDphY3Rpb24+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDppbnN0YW5jZUlEPnhtcC5paWQ6MTQ0NWM2YjUtZjdiOC00ZjU1LWE4YmItZmQ1NmU0NmM4Mzg5PC9zdEV2dDppbnN0YW5jZUlEPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6d2hlbj4yMDE4LTExLTAzVDE1OjA5OjU5Wjwvc3RFdnQ6d2hlbj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OnNvZnR3YXJlQWdlbnQ+QWRvYmUgUGhvdG9zaG9wIENDIDIwMTQgKE1hY2ludG9zaCk8L3N0RXZ0OnNvZnR3YXJlQWdlbnQ+CiAgICAgICAgICAgICAgIDwvcmRmOmxpPgogICAgICAgICAgICAgICA8cmRmOmxpIHJkZjpwYXJzZVR5cGU9IlJlc291cmNlIj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OmFjdGlvbj5zYXZlZDwvc3RFdnQ6YWN0aW9uPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6aW5zdGFuY2VJRD54bXAuaWlkOjdjYjNjOTg1LWIxNWUtNDQ5Ny04M2RiLTk2ZWNlOTQ1OGUwYzwvc3RFdnQ6aW5zdGFuY2VJRD4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OndoZW4+MjAxOC0xMS0wM1QxNToxODoyMlo8L3N0RXZ0OndoZW4+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDpzb2Z0d2FyZUFnZW50PkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE0IChNYWNpbnRvc2gpPC9zdEV2dDpzb2Z0d2FyZUFnZW50PgogICAgICAgICAgICAgICAgICA8c3RFdnQ6Y2hhbmdlZD4vPC9zdEV2dDpjaGFuZ2VkPgogICAgICAgICAgICAgICA8L3JkZjpsaT4KICAgICAgICAgICAgPC9yZGY6U2VxPgogICAgICAgICA8L3htcE1NOkhpc3Rvcnk+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgICAgIDx0aWZmOlhSZXNvbHV0aW9uPjcyMDAwMC8xMDAwMDwvdGlmZjpYUmVzb2x1dGlvbj4KICAgICAgICAgPHRpZmY6WVJlc29sdXRpb24+NzIwMDAwLzEwMDAwPC90aWZmOllSZXNvbHV0aW9uPgogICAgICAgICA8dGlmZjpSZXNvbHV0aW9uVW5pdD4yPC90aWZmOlJlc29sdXRpb25Vbml0PgogICAgICAgICA8ZXhpZjpDb2xvclNwYWNlPjY1NTM1PC9leGlmOkNvbG9yU3BhY2U+CiAgICAgICAgIDxleGlmOlBpeGVsWERpbWVuc2lvbj4xMjA5PC9leGlmOlBpeGVsWERpbWVuc2lvbj4KICAgICAgICAgPGV4aWY6UGl4ZWxZRGltZW5zaW9uPjc5MzwvZXhpZjpQaXhlbFlEaW1lbnNpb24+CiAgICAgIDwvcmRmOkRlc2NyaXB0aW9uPgogICA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgIAo8P3hwYWNrZXQgZW5kPSJ3Ij8+9ZvwMQAAACBjSFJNAAB6JQAAgIMAAPn/AACA6QAAdTAAAOpgAAA6mAAAF2+SX8VGAABJGElEQVR42uzdz4vld7Xu8fxx0iDiLOBcEIQIzsSBUweaKOEgjkQOmDM6IRAICF7EgAhBkmAuaTyiaPAgUUxq165Utf3DzvfOGrzQ4KpePmsJrxc8g0z2YEGTXW/q0/3cAQAAAAD/5p5zgtu7uLhwBAj75JNPjocPHzoEBN2/f/+4ublxCAh6/PjxcTqdHALCzufz8fe//90hIOjevXvH3/72t5bPErmegcgFeSIX5IlckCdywQyRC/JEriVELsgTuSBP5Orxm998cPzHf/zXk/34xz93FJ5K5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5LVGrs985jPHu+++66q3IHJBnsgFeSJXD5GLCpELZohckNceud577z1XvQWRC/JELsgTuXqIXFSIXDBD5IK81sj1pS996Xj8+LGr3oLIBXkiF+SJXD1ELipELpghckFea+T69a9/7aK3JHJBnsgFeSJXD5GLCpELZohckNcauT799NMn/3F1dWWFXVxcuINZeKfT6Tifz25hFtzl5eVxOp3c4hn37rt3jxdf/OGTvfbaT9zFnrrz+ey7ptnQz3i+a5rlv2teXl62fNY//OuKjx49ssJOp5M7mIV3dXV13L9/3y3Mgrt3795xfX3tFs+4u3d/d7z88o+e7I033nQXe+oePnzou6bZwM7n8/HgwQO3MAvu5ubmuLm5afms5/xi3O15rgh5nitCnueKPTxXpMJzRZjhuSLktT5XdM7bE7kgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyBO5lhC5IE/kgjyRq4fIRYXIBTNELsgTuZYQuSBP5II8kauHyEWFyAUzRC7IE7mWELkgT+SCPJGrh8hFhcgFM0QuyGuNXH5YvD2RC/JELsgTuXqIXFSIXDBD5IK81sj17W9/20VvSeSCPJEL8kSuHiIXFSIXzBC5IK81cn3wwQcueksiF+SJXJAncvUQuagQuWCGyAV5/k6uJUQuyBO5IE/k6iFyUSFywQyRC/JaI9eHH37oorckckGeyAV5IlcPkYsKkQtmiFyQ1xq5PvvZzx7n8/nJB9s/v48//tgdzMK7vLw8PvnkE7cwC+7q6uo4n89u8Yx7773/Ob7znf98stdf/6m72FN3c3NzXFxcuIVZeKfT6bi+vnYLs+DO5/NxdXXV8lnP3blz53jrrbdELpHLTOQyM5FL5DKRy0zkErnM/r0j1zvvvOP3427Bc0XI81wR8jxX7OG5IhWeK8IMzxUhr/W54p07d548V6RG5II8kQvyRK4eIhcVIhfMELkgrzVyvf322y56SyIX5IlckCdy9RC5qBC5YIbIBXmtkcs5b0/kgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IK81ct25c+f46KOPXPUWRC7IE7kgT+TqIXJRIXLBDJEL8loj19tvv308ePDAVW9B5II8kQvyRK4eIhcVIhfMELkgz3PFJUQuyBO5IE/k6iFyUSFywQyRC/JaI9fjx49d9JZELsgTuSBP5OohclEhcsEMkQvyWiPXCy+88OQP8aNHj6yw0+nkDmbhXV1dHffv33cLs+Du3bt3XF9fu8Uz7u7d3x0vv/yjJ3vjjTfdxZ66hw8f+q5pNrDz+Xw8ePDALcyCu7m5OW5ublo+6x/+4vmrqysr7OLiwh3MwjudTsf5fHYLs+AuLy+P0+nkFs+4d9+9e7z44g+f7LXXfuIu9tSdz2ffNc2GfsbzXdMs/13z8vKy5bP864rPwHNFyPNcEfI8V+zhuSIVnivCDM8VIa/1ueLzzz9/PHr0yFVvQeSCPJEL8kSuHiIXFSIXzBC5IK81cn344YcueksiF+SJXJAncvUQuagQuWCGyAV5rZHLOW9P5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgT+RaQuSCPJEL8kSuHiIXFSIXzBC5IE/kWkLkgjyRC/JErh4iFxUiF8wQuSBP5FpC5II8kQvyRK4eIhcVIhfMELkgrzVyffzxxy56SyIX5IlckCdy9RC5qBC5YIbIBXki1xIiF+SJXJAncvUQuagQuWCGyAV5ItcSIhfkiVyQJ3L1ELmoELlghsgFeSLXEiIX5IlckCdy9RC5qBC5YIbIBXmtkev6+vrJf1xcXJiZmZnZv2C//OV7x7e+9YMn++///rG7mJmZmTXuua985SvH+++/Lx3egt/kgjy/yQV5fpOrh9/kosJvcsEMv8kFea2/yfXd7373+MMf/uCqtyByQZ7IBXkiVw+RiwqRC2aIXJD3L3uuSI3IBXkiF+SJXD1ELipELpghckGev3h+CZEL8kQuyBO5eohcVIhcMEPkgrzWyOWctydyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckNcaud5//30XvSWRC/JELsgTuXqIXFSIXDBD5IK81sj1/PPPH48fP3bVWxC5IE/kgjyRq4fIRYXIBTNELshrjVyf//zn/SG+JZEL8kQuyBO5eohcVIhcMEPkgrzWyPXmm2+66C2JXJAnckGeyNVD5KJC5IIZIhfktUauX/7yl0/+4+rqygq7uLhwB7PwTqfTcT6f3cIsuMvLy+N0OrnFM+7dd+8eL774wyd77bWfuIs9defz2XdNs6Gf8XzXNMt/17y8vGz5rOfu3LlzXF5eHsdxHI8ePbLCTqeTO5iFd3V1ddy/f98tzIK7d+/ecX197RbPuLt3f3e8/PKPnuyNN950F3vqHj586Lum2cDO5/Px4MEDtzAL7ubm5ri5uWn5rOfu3LlzfPTRR34/7hY8V4Q8zxUhz3PFHp4rUuG5IszwXBHy2v91xUePHrnqLYhckCdyQZ7I1UPkokLkghkiF+S1Rq4PP/zQRW9J5II8kQvyRK4eIhcVIhfMELkgrzVyOeftiVyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjVQ+SiQuSCGSIX5IlcS4hckCdyQZ7I1UPkokLkghkiF+SJXEuIXJAnckGeyNVD5KJC5IIZIhfktUauv/zlLy56SyIX5IlckCdy9RC5qBC5YIbIBXmtkeuFF144Hj9+7Kq3IHJBnsgFeSJXD5GLCpELZohckNcauZ5//nl/iG9J5II8kQvyRK4eIhcVIhfMELkgrzVyff3rXz8+/fRTV70FkQvyRC7IE7l6iFxUiFwwQ+SCvNbI9cEHH/zDB9s/v48//tgdzMK7vLw8PvnkE7cwC+7q6uo4n89u8Yx7773/Ob7znf98stdf/6m72FN3c3NzXFxcuIVZeKfT6bi+vnYLs+DO5/NxdXXV8lnP/f/1zEQuM5HLzEQukctELjORy8z+rSMXNZ4rQp7nipDnuWIPzxWp8FwRZniuCHmtzxXv3r3rB8ZbErkgT+SCPJGrh8hFhcgFM0QuyGuNXHfu3Dk++ugjV70FkQvyRC7IE7l6iFxUiFwwQ+SCvNbI5Zy3J3JBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckCdyLSFyQZ7IBXkiVw+RiwqRC2aIXJAnci0hckGeyAV5IlcPkYsKkQtmiFyQJ3ItIXJBnsgFeSJXD5GLCpELZohckPcvi1yPHj2ywk6nkzuYhXd1dXXcv3/fLcyCu3fv3nF9fe0Wz7i7d393vPzyj57sjTfedBd76h4+fOi7ptnAzufz8eDBA7cwC+7m5ua4ublp+ax/iFxXV1dW2MXFhTuYhXc6nY7z+ewWZsFdXl4ep9PJLZ5x775793jxxR8+2Wuv/cRd7Kk7n8++a5oN/Yznu6ZZ/rvm5eVly2d5rvgMPFeEPM8VIc9zxR6eK1LhuSLM8FwR8lqfK/qf5+2JXJAnckGeyNVD5KJC5IIZIhfktUaul156yUVvSeSCPJEL8kSuHiIXFSIXzBC5IM+/rriEyAV5IhfkiVw9RC4qRC6YIXJBnsi1hMgFeSIX5IlcPUQuKkQumCFyQZ7ItYTIBXkiF+SJXD1ELipELpghckGeyLWEyAV5IhfkiVw9RC4qRC6YIXJBnsi1hMgFeSIX5IlcPUQuKkQumCFyQZ7ItYTIBXkiF+SJXD1ELipELpghckGeyLWEyAV5IhfkiVw9RC4qRC6YIXJBnsi1hMgFeSIX5IlcPUQuKkQumCFyQZ7ItYTIBXkiF+SJXD1ELipELpghckGeyLWEyAV5IhfkiVw9RC4qRC6YIXJBnsi1hMgFeSIX5IlcPUQuKkQumCFyQZ7ItYTIBXkiF+SJXD1ELipELpghckGeyLWEyAV5IhfkiVw9RC4qRC6YIXJBnsi1hMgFeSIX5IlcPUQuKkQumCFyQZ7ItYTIBXkiF+SJXD1ELipELpghckGeyLWEyAV5IhfkiVw9RC4qRC6YIXJBnsi1hMgFeSIX5IlcPUQuKkQumCFyQZ7ItYTIBXkiF+SJXD1ELipELpghckGeyLWEyAV5IhfkiVw9RC4qRC6YIXJBnsi1hMgFeSIX5IlcPUQuKkQumCFyQZ7ItYTIBXkiF+SJXD1ELipELpghckGeyLWEyAV5IhfkiVw9RC4qRC6YIXJBnsi1hMgFeSIX5IlcPUQuKkQumCFyQZ7ItYTIBXkiF+SJXD1ELipELpghckGeyLWEyAV5IhfkiVw9RC4qRC6YIXJBnsi1hMgFeSIX5IlcPUQuKkQumCFyQZ7ItYTIBXkiF+SJXD1ELipELpghckGeyLWEyAV5IhfkiVw9RC4qRC6YIXJBnsi1hMgFeSIX5IlcPUQuKkQumCFyQZ7ItYTIBXkiF+SJXD1ELipELpghckGeyLWEyAV5IhfkiVw9RC4qRC6YIXJBnsi1hMgFeSIX5IlcPUQuKkQumCFyQZ7ItYTIBXkiF+SJXD1ELipELpghckGeyLWEyAV5IhfkiVw9RC4qRC6YIXJBnsi1hMgFeSIX5IlcPUQuKkQumCFyQZ7ItYTIBXkiF+SJXD1ELipELpghckGeyLWEyAV5IhfkiVw9RC4qRC6YIXJBnsi1hMgFeSIX5IlcPUQuKkQumCFyQZ7ItYTIBXkiF+SJXD1ELipELpghckGeyLWEyAV5IhfkiVw9RC4qRC6YIXJBnsi1hMgFeSIX5IlcPUQuKkQumCFyQZ7ItYTIBXkiF+SJXD1ELipELpghckGeyLWEyAV5IhfkiVw9RC4qRC6YIXJBnsi1hMgFeSIX5IlcPUQuKkQumCFyQZ7ItYTIBXkiF+SJXD1ELipELpghckGeyLWEyAV5IhfkiVw9RC4qRC6YIXJBnsi1hMgFeSIX5IlcPUQuKkQumCFyQZ7ItYTIBXkiF+SJXD1ELipELpghckGeyLWEyAV5IhfkiVw9RC4qRC6YIXJBnsi1xC9+8Yvj8ePHDgFBd+/ePf761786BAT96U9/On7zm984xDMSuai4f//+8dZbbzkEhL3zzjvH9fW1Q0DQ73//++OPf/xjy2eJXM/gc5/7XFttBP453/jGN46f/exnDgFBr7/++vGtb33LIZ6RyEXFn//85+MLX/iCQ0DYF7/4xeO3v/2tQ0DQ97///eOVV15p+SyR6xmIXJAnckGeyNVD5KJC5IIZIhfkiVxLiFyQJ3JBnsjV43//98/Hq6/+nyd7663/6yg8lcgFM0QuyBO5lhC5IE/kgjyRC/JELpghckHevyxy/epXv7LCvvzlLx9vv/22W5gF981vfvN49dVX3cIsuFdeeeV46aWX3MIsuJ///OfHV7/6VbcwC+9rX/va8dOf/tQtzIL73ve+d/zgBz9o+az/NwBZ8OBcaOevNQAAAABJRU5ErkJggg==",
                                                             "visible": False,
                                                             "xanchor": "center",
                                                             "xref": "paper",
                                                             "yanchor": "middle"
                                                             },
                                                             {
                                                             "x": 0.5,
                                                             "y": 0.5,
                                                             "layer": "below",
                                                             "sizex": 1,
                                                             "sizey": 1,
                                                             "sizing": "stretch",
                                                             "source": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABLkAAAMZCAYAAADsgOatAAAACXBIWXMAAAsTAAALEwEAmpwYAAA53GlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4KPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS41LWMwMjEgNzkuMTU1NzcyLCAyMDE0LzAxLzEzLTE5OjQ0OjAwICAgICAgICAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iCiAgICAgICAgICAgIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIKICAgICAgICAgICAgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIgogICAgICAgICAgICB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIKICAgICAgICAgICAgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIKICAgICAgICAgICAgeG1sbnM6dGlmZj0iaHR0cDovL25zLmFkb2JlLmNvbS90aWZmLzEuMC8iCiAgICAgICAgICAgIHhtbG5zOmV4aWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vZXhpZi8xLjAvIj4KICAgICAgICAgPHhtcDpDcmVhdG9yVG9vbD5BZG9iZSBQaG90b3Nob3AgQ0MgMjAxNCAoTWFjaW50b3NoKTwveG1wOkNyZWF0b3JUb29sPgogICAgICAgICA8eG1wOkNyZWF0ZURhdGU+MjAxOC0xMS0wM1QxNTowOTo1OVo8L3htcDpDcmVhdGVEYXRlPgogICAgICAgICA8eG1wOk1vZGlmeURhdGU+MjAxOC0xMS0wM1QxNToyMzowNlo8L3htcDpNb2RpZnlEYXRlPgogICAgICAgICA8eG1wOk1ldGFkYXRhRGF0ZT4yMDE4LTExLTAzVDE1OjIzOjA2WjwveG1wOk1ldGFkYXRhRGF0ZT4KICAgICAgICAgPGRjOmZvcm1hdD5pbWFnZS9wbmc8L2RjOmZvcm1hdD4KICAgICAgICAgPHBob3Rvc2hvcDpDb2xvck1vZGU+MzwvcGhvdG9zaG9wOkNvbG9yTW9kZT4KICAgICAgICAgPHhtcE1NOkluc3RhbmNlSUQ+eG1wLmlpZDoyZTA5OWE3MC0wODllLTRmNmUtYWU4Zi05MGZlZmMwNGY0NDM8L3htcE1NOkluc3RhbmNlSUQ+CiAgICAgICAgIDx4bXBNTTpEb2N1bWVudElEPmFkb2JlOmRvY2lkOnBob3Rvc2hvcDpjOWYyM2I1Ni0yMDBhLTExN2MtOGFjYi1iMzc1ZDdmNWM1ZTM8L3htcE1NOkRvY3VtZW50SUQ+CiAgICAgICAgIDx4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ+eG1wLmRpZDpkNjkyMDZjMC0yNzhkLTRkMGMtOTI4YS01OTMwZTAxZjFhZDk8L3htcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD4KICAgICAgICAgPHhtcE1NOkhpc3Rvcnk+CiAgICAgICAgICAgIDxyZGY6U2VxPgogICAgICAgICAgICAgICA8cmRmOmxpIHJkZjpwYXJzZVR5cGU9IlJlc291cmNlIj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OmFjdGlvbj5jcmVhdGVkPC9zdEV2dDphY3Rpb24+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDppbnN0YW5jZUlEPnhtcC5paWQ6ZDY5MjA2YzAtMjc4ZC00ZDBjLTkyOGEtNTkzMGUwMWYxYWQ5PC9zdEV2dDppbnN0YW5jZUlEPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6d2hlbj4yMDE4LTExLTAzVDE1OjA5OjU5Wjwvc3RFdnQ6d2hlbj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OnNvZnR3YXJlQWdlbnQ+QWRvYmUgUGhvdG9zaG9wIENDIDIwMTQgKE1hY2ludG9zaCk8L3N0RXZ0OnNvZnR3YXJlQWdlbnQ+CiAgICAgICAgICAgICAgIDwvcmRmOmxpPgogICAgICAgICAgICAgICA8cmRmOmxpIHJkZjpwYXJzZVR5cGU9IlJlc291cmNlIj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OmFjdGlvbj5zYXZlZDwvc3RFdnQ6YWN0aW9uPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6aW5zdGFuY2VJRD54bXAuaWlkOjJlMDk5YTcwLTA4OWUtNGY2ZS1hZThmLTkwZmVmYzA0ZjQ0Mzwvc3RFdnQ6aW5zdGFuY2VJRD4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OndoZW4+MjAxOC0xMS0wM1QxNToyMzowNlo8L3N0RXZ0OndoZW4+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDpzb2Z0d2FyZUFnZW50PkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE0IChNYWNpbnRvc2gpPC9zdEV2dDpzb2Z0d2FyZUFnZW50PgogICAgICAgICAgICAgICAgICA8c3RFdnQ6Y2hhbmdlZD4vPC9zdEV2dDpjaGFuZ2VkPgogICAgICAgICAgICAgICA8L3JkZjpsaT4KICAgICAgICAgICAgPC9yZGY6U2VxPgogICAgICAgICA8L3htcE1NOkhpc3Rvcnk+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgICAgIDx0aWZmOlhSZXNvbHV0aW9uPjcyMDAwMC8xMDAwMDwvdGlmZjpYUmVzb2x1dGlvbj4KICAgICAgICAgPHRpZmY6WVJlc29sdXRpb24+NzIwMDAwLzEwMDAwPC90aWZmOllSZXNvbHV0aW9uPgogICAgICAgICA8dGlmZjpSZXNvbHV0aW9uVW5pdD4yPC90aWZmOlJlc29sdXRpb25Vbml0PgogICAgICAgICA8ZXhpZjpDb2xvclNwYWNlPjY1NTM1PC9leGlmOkNvbG9yU3BhY2U+CiAgICAgICAgIDxleGlmOlBpeGVsWERpbWVuc2lvbj4xMjA5PC9leGlmOlBpeGVsWERpbWVuc2lvbj4KICAgICAgICAgPGV4aWY6UGl4ZWxZRGltZW5zaW9uPjc5MzwvZXhpZjpQaXhlbFlEaW1lbnNpb24+CiAgICAgIDwvcmRmOkRlc2NyaXB0aW9uPgogICA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgIAo8P3hwYWNrZXQgZW5kPSJ3Ij8+moNNEQAAACBjSFJNAAB6JQAAgIMAAPn/AACA6QAAdTAAAOpgAAA6mAAAF2+SX8VGAAAdn0lEQVR42uzbwWadaxiG4Z5+LWHpeIsSe9RahEVIldBJh7FPqJ397Pn/3ITr4jmBd3j7vk9/AAAAAOCD++QEAAAAAHx0IhcAAAAAH57IBQAQ+fLl32MvL78cBADgRCIXAEBE5AIA2BG5AAAiIhcAwI7IBQAQEbkAAHZELgCAiMgFALAjcgEAREQuAIAdkQsAICJyAQDsiFwAABGRCwBgR+QCAIiIXAAAOyIXAEBE5AIA2BG5AAAiIhcAwI7IBQAQEbkAAHZELgCAiMgFALAjcgEAREQuAIAdkQsAICJyAQDsiFwAABGRCwBgR+QCAIiIXAAAOyIXAEBE5AIA2BG5AAAiIhcAwI7IBQAQEbkAAHZELgCAiMgFALAjcgEAREQuAIAdkQsAICJyAQDsiFwAABGRCwBgR+QCAIiIXAAAOyIXAEBE5AIA2BG5AAAiIhcAwI7IBQAQEbkAAHZELgCAiMgFALAjcgEAREQuAIAdkQsAICJyAQDs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ACAicgEA7IhcAAARkQsAYEfkAgCIiFwAADsiFwBAROQCANgRuQAAIiIXAMCOyAUAEBG5AAB2RC4AgIjIBQCwI3IBAERELgCAHZELACAicgEA7IhcAAARkQsAYEfkAgCIiFwAADsiFwBAROQCANgRuQAAIiIXAMCOyAUAEBG5AAB2RC4AgIjIBQCwI3IBAERELgCAHZELACAicgEA7IhcAAARkQsAYEfkAgCIiFwAADsiFwBAROQCANgRuQAAIiIXAMCOyAUAEBG5AAB2RC4AgIjIBQCwI3IBAERELgCAHZELACAicgEA7IhcAAARkQsAYEfkAgCIiFwAADsiFwBAROQCANgRuQAAIiIXAMCOyAUAEBG5AAB2RC4AgIjIBQCwI3IBAERELgCAHZELACAicgEA7IhcAAARkQsAYEfkAgCIiFwAADsiFwBAROQCANgRuQAAIiIXAMCOyAUAEBG5AAB2RC4AgIjIBQCwI3IBAERELgCAHZELACAicgEA7IhcAAARkQsAYEfkAgCIiFwAADsiFwBAROQCANgRuQAAIiIXAMCOyAUAEBG5AAB2RC4AgIjIBQCwI3IBAERELgCAHZELACAicgEA7IhcAAARkQsAYEfkAgCIiFwAADsiFwBAROQCANgRuQAAIiIXAMCOyAUAEBG5AAB2RC4AgIjIBQCwI3IBAERELgCAHZELACAicgEA7IhcAAARkQsAYEfkAgCIiFwAADsiFwBAROQCANgRuQAAIiIXAMCOyAUAEBG5AAB2RC4AgIjIBQCwI3IBAERELgCAHZELACAicgEA7IhcAAARkQsAYEfkAgCIiFwAADsiFwBAROQCANgRuQAAIiIXAMCOyAUAEBG5AAB2RC4AgIjIBQCwI3IBAERELgCAHZELACAicgEA7IhcAAARkQsAYEfkAgCIiFwAADsiFwBAROQCANgRuQAAIiIXAMCOyAUAEBG5AAB2RC4AgIjIBQCwI3IBAERELgCAHZELACAicgEA7IhcAAARkQsAYEfkAgCIiFwAADsiFwBAROQCANgRuQAAIiIXAMCOyAUAEBG5AAB2RC4AgIjIBQCwI3IBAERELgCAHZELACAicgEA7IhcAAARkQsAYEfkAgCIiFwAADsiFwBAROQCANgRuQAAIiIXAMCOyAUAEBG5AAB2RC4AgIjIBQCwI3IBAERELgCAHZEL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dkQuAICIyAUAsCNyAQBERC4AgB2RCwAgInIBAOyIXAAAEZELAGBH5AIAiIhcAAA7IhcAQETkAgDYEbkAACIiFwDAjsgFABARuQAAdkQuAICIyAUAsCNyAQBERC4AgB2RCwAgInIBAOyIXAAAEZELAGBH5AIAiIhcAAA7IhcAQETkAgDYEbkAACIiFwDAjsgFABARuQAAdkQuAICIyAUAsCNyAQBERC4AgB2RCwAgInIBAOyIXAAAEZELAGBH5AIAiIhcAAA7IhcAQETkAgDYEbkAACIiFwDAjsgFABARuQAAdkQuAICIyAUAsCNyAQBERC4AgB2RCwAgInIBAOyIXAAAEZELAGBH5AIAiIhcAAA7IhcAQETkAgDYEbkAACIiFwDAjsgFABARuQAAdkQuAICIyAUAsCNyAQBERC4AgB2RCwAgcr0+Hbvf3xwEAOBEIhcAQORyeTx2u706CADAiUQuAICI74oAADsiFwBAROQCANgRuQAAIiIXAMCOyAUAEBG5AAB2RC4AgIjIBQCwI3IBAERELgCAHZELACAicgEA7IhcAAARkQsAYEfkAgCIiFwAADsiFwBAROQCANgRuQAAIiIXAMCOyAUAEBG5AAB2RC4AgIjIBQCwI3IBAERELgCAHZELACAicgEA7IhcAAARkQsAYEfkAgCIiFwAADsiFwBAROQCANgRuQAAIiIXAMCOyAUAEBG5AAB2RC4AgIjIBQCwI3IBAERELgCAHZELACAicgEA7IhcAAARkQsAYEfkAgCIiFwAADsiFwBAROQCANgRuQAAIiIXAMCOyAUAEBG5AAB2RC4AgIjIBQCwI3IBAERELgCAHZELACAicgEA7IhcAAARkQsAYEfkAgCIiFwAADsiFwBAROQCANgRuQAAIiIXAMCOyAUAEBG5AAB2RC4AgIjIBQCwI3IBAERELgCAHZELACAicgEA7IhcAAARkQsAYEfkAgCIiFwAADsiFwBAROQCANgRuQAAIiIXAMCOyAUAEBG5AAB2RC4AgIjIBQCwI3IBAERELgCAHZELACAicgEA7IhcAAARkQsAYEfkAgCIiFwAADsiFwBAROQCANgRuQAAIiIXAMCOyAUAEBG5AAB2RC4AgIjIBQCwI3IBAERELgCAHZELACAicgEA7IhcAACR799/HPv9+z8HAQA4kcgFAAAAwIcncgEARN7f3/83AADO83cAudmU5KLkBDYAAAAASUVORK5CYII=",
                                                             "visible": True,
                                                             "xanchor": "center",
                                                             "yanchor": "middle"
                                                             }
                                                             ],
                                                    margin= {"t": 100},
                                                    xaxis={'autorange': True, 'fixedrange': True, 'range': (d4, d5), 'showline': True, 'ticks': "inside", 'title': "time", 'type': "date"},
                                                    yaxis={'autorange': True, 'fixedrange': True, 'range': [0.451383063814, 7.61242655506], 'title': "colours", 'type': "linear"},
                                                    ),
                                }
                                )
                      ], className = "row"),
            html.Div([
                      html.Div([
                                html.Hr(id='text-1', style=styles['hr']),
                                html.Br(),
                      ], className='row'),
                      html.Div([
                                dcc.Markdown('''**Information and Statistics**'''),
                                html.P(bf),
                                html.P(gc),
                                html.P(bg),
                                html.P(bh),
                                html.P('The half-life of Carbon 14 is 5600 years, which coincides with the length of the RCC-14'),
                                html.P('The Calendar has a start date of October, 26, 2010. It will reset on the same day in the year 7610'),
                                html.P('It takes approximately 56000 years for the C-14 to decay completely. Therefore, we can say that the calendar end-date will occur on October 25th 58010 (See Graph; Left). But since the carbon-14 cycle is self renewing, perhaps we can say that the calendar has no end-date?'),
                                html.P('To read more about Carbon 14 and its halflife check the link below;'),
                                dcc.Markdown('''[http://www.nucleide.org/DDEP_WG/Nuclides/C-14_com.pdf](http://www.nucleide.org/DDEP_WG/Nuclides/C-14_com.pdf)'''),
                                ], className='six columns', style={'width': '40%'}),
                      html.Div([
                                dcc.Graph(
                                          id='half-life',
                                          figure={
                                          'data':[
                                                  go.Scatter(
                                                             x= [2010, 7610, 13210, 18810, 24410, 30010, 35610, 41210, 46810, 52410, 58010],
                                                             y= [1461, 730.5, 365.25, 182.625, 91.3125, 45.65625, 22.828125, 11.4140625, 5.707, 2.85351, 1.42675],
                                                             hoverinfo= 'x+y',
                                                             line= {
                                                             'shape': 'spline',
                                                             'smoothing': 1.2
                                                             },
                                                             mode= "lines+markers",
                                                             name= "exponential",
                                                             showlegend= False,
                                                             ),
                                                  ],
                                          'layout' : go.Layout(
                                                               autosize= True,
                                                               paper_bgcolor= "#ffffff",
                                                               plot_bgcolor= "rgb(208, 248, 255)",
                                                               title= "Halflife Carbon 14",
                                                               xaxis= {
                                                               "autorange": True,
                                                               "fixedrange": True,
                                                               "range": [-3436.54114365, 59436.5411437],
                                                               "title": "years",
                                                               "type": "linear"
                                                               },
                                                               yaxis= {
                                                               "autorange": True,
                                                               "fixedrange": True,
                                                               "range": [-99.2659242424, 1561.69267424],
                                                               "title": "metagrams",
                                                               "type": "linear"
                                                               }
                                                               ),
                                          },
                                          ),
                                ], className='six columns', style={'width': '50%'}),
                      ], className = "row"),
            html.Div([
                      html.Br(),
                      html.Hr(id='input-boxes', style=styles['hr']),
                      html.H2('Rainbow Calendar Carbon-14 Search Dates'),
            ], className = "row"),
            html.P('The following application allows you to search accurately for most dates ranges after 1980-02-25. You might be able to use this application to search your birthdate or the birthdate of someone you know. To hear the full sequence converted to music visit;'),
            dcc.Markdown('''[https://soundcloud.com/thirdeyedevice/rainbow-calendar-seq](https://soundcloud.com/thirdeyedevice/rainbow-calendar-seq)'''),
            html.Label('Enter a range of dates in the format yyyy-mm-dd:'),
            html.Div([
                html.Div([
                    dcc.Input(id='start_time',
                              value='2010-08-31',
                              type='text',
                              style={'width': '100'}),
                    dcc.Input(id='end_time',
                              value='2010-12-03',
                              type='text',
                              style={'width': '100', 'margin-left': 14}),
                    html.Div(id='date-container-output'),
                ]),
            html.Br(),
            html.Div(children=None, id='date-container'),
            ], className = "row"),
            html.Br(),
            html.Hr(style=styles['hr']),
            html.H2('Rainbow Calendar C-14 Personality Profile'),
            html.P('Once you have found your birthdate, you can input the colour of the day you were born on from the buttons below. Then use the slider to select the number of days in your colour bracket. So using the example above; if you were born on October 31st 2010, your colour would be red and your number would be 10. This will give you a personality profile, not unlike a horoscope.'),
            html.Br(),
            html.Div([
                html.Div(
                    dcc.Slider(id='slider',
                        min=1,
                        max=10,
                        marks={
                            1: '1',
                            2: '2',
                            3: '3',
                            4: '4',
                            5: '5',
                            6: '6',
                            7: '7',
                            8: '8',
                            9: '9',
                            10: '10',
                        },
                    value=1),
                className='five columns offset-by-one'),
            ], className='row'),
            html.Div([
                dcc.RadioItems(id='radio',
                    options=[
                        {'label': 'Red', 'value': 'red'},
                        {'label': 'Orange', 'value': 'orange'},
                        {'label': 'Yellow', 'value': 'yellow'},
                        {'label': 'Green', 'value': 'green'},
                        {'label': 'Blue', 'value': 'blue'},
                        {'label': 'Indigo', 'value': 'ind'},
                        {'label': 'Violet', 'value': 'vio'},
                    ],
                    value='red', style={'margin-left': -35, 'margin-top': 70}),
            ], className='one column'),
            html.Div(id='intermediate-value2', style={'display': 'none'}),
            html.Br(),
            html.Div([  
                dcc.Textarea(id='textbox-1', value=xox, readOnly = True, style={'width': '35%', 'padding-top': 0, 'padding-bottom': 0, 'background-color': '#ffffff', 'border-radius': 1,  'resize': 'none', 'font-family': 'arial', 'size': 14, 'border-color': 'black', 'margin-top': 20, 'margin-right': 0, 'margin-left': 30},
                className='five columns offset-by-one'),
                html.Img(src = '/assets/chakras.jpg', style={'width': '40%', 'margin-top': 20}, className='four columns offset-by-one'),
            ], className='row'),
            html.Br(),
            html.Br(),
            html.Hr(style=styles['hr']),
            html.Div([
            html.Div(children=None, id='graph-output'),
            html.Br(),
            ], className='row'),
                 html.Div(
                 dcc.Slider(id='slider3',
                    min=1,
                    max=8,
                    marks={
                        1: {'label': '1980-1984', 'style': {'color': 'black'}},
                        2: {'label': '1984-1987', 'style': {'color': 'black'}},
                        3: {'label': '1987-1991', 'style': {'color': 'black'}},
                        4: {'label': '1991-1995', 'style': {'color': 'black'}},
                        5: {'label': '1995-1999', 'style': {'color': 'black'}},
                        6: {'label': '1999-2003', 'style': {'color': 'black'}},
                        7: {'label': '2003-2006', 'style': {'color': 'black'}},
                        8: {'label': '2006-2010', 'style': {'color': 'black'}},
                    },
                 value=1),
                 className='ten columns offset-by-one'),
            html.Br(),
            html.Br(),
            html.Hr(style=styles['hr']),
            html.H2('Rainbow Calendar Historical Research'),
            html.P('This app was designed to sort important historical events by colour, date and category, to see if a common theme or pattern emerges. Each of the events fits into 1 of 9 categories, including; war, financial collapse, political unrest, political agreement etc. The resutls are inconclusive. Possibly this is due to the small sample range of 72 events over a period of more than 37 years and covering a wide range of locations. The colour green however does show some kind of pattern and it appears that war, terrorism and political unrest are particularly prevalent during this period and tied to a specific country, which has seen more than its fair share of unrest. However, 1 in 7 does not appear to be a statistically significant result either.'),
            html.Br(),
            html.Br(),
            html.Div([ 
                 html.Div(children=None, id='piechart-container',
                 className='six columns', style={'margin-top': 40}),
                 html.Div(
                 dcc.Slider(id='slider2',
                    min=1,
                    max=8,
                    marks={
                        1: {'label': 'Red', 'style': {'color': 'red'}},
                        2: {'label': 'Orange', 'style': {'color': 'orange'}},
                        3: {'label': 'Yellow', 'style': {'color': '#fcd714'}},
                        4: {'label': 'Green', 'style': {'color': '#9ac432'}},
                        5: {'label': 'Blue', 'style': {'color': '#61c8f3'}},
                        6: {'label': 'Indigo', 'style': {'color': 'indigo'}},
                        7: {'label': 'Violet', 'style': {'color': 'violet'}},
                        8: {'label': 'White'},
                    },
                 value=1),
                 className='five columns'),
                 dcc.Textarea(id='textbox-2', readOnly = True, style={'width': '40%',  'height': 440,  'padding-top': 20, 'padding-bottom': 0, 'background-color': '#ffffff', 'border-radius': 1,  'resize': 'none', 'font-family': 'arial', 'size': 14, 'border-color': 'black', 'margin-top': 40, 'margin-right': 0},
                 className='six columns'),
            ], className='row'),
            html.Br(),
            html.Div([
                      html.Br(),
                      html.Hr(id='footer', style=styles['hr']),
                      html.Br(),
                      html.Footer(
                            html.Center('Cataphysical Research Society - 2018.' ),
                      ),
                      html.Br(),
            ], className = "row"),
      ]),    
)    


@app.callback(dash.dependencies.Output('graph-output', 'children'),
[dash.dependencies.Input('slider3', 'value')])
def func(value):
    if value == 1:
        return dcc.Graph(style={'height': '600px'},
        id='Rain-Cal-N17',
            figure={
                 'data': [
                     go.Scatter(
                         x=d17,
                         y= z1[:],
                         text= m[:],
                         mode='markers+lines',
                         opacity=0.7,
                         visible=True,
                         hoverinfo = "x+y+name",
                         marker={
                         'size': 13,
                         'line': {'width': 1},
                         'autocolorscale': False,
                         'cauto': False,
                         'cmax': 7,
                         'cmin': 1,
                         'color': z1[:],
                         'colorscale': [[0, "#ff0000"], [0.142857142857143, "#ffae01"], [0.3333333333333, "#fff600"], [0.5555555555555, "#0aff04"], [0.6666666666666, "#0569ff"], [0.777777777777, "#a201ff"], [0.8888888888888, "#ff03ea"], [1.0000000, "#ff03ea"]],
                         'colorsrc': "robotwax:157:00284a",
                         'reversescale': False,
                         'showscale': True,
                         "size": 16, 
                         "symbol": "star-triangle-up"
                         },
                         ),
                     ],
            
            'layout': go.Layout(
                            {'title': 'RCC-14 Historical Data Hi There!'},
                            margin= {"t": 100},
                            annotations= [
                                  {
                                    "x": "1980-04-18 03:01:15.3929", 
                                    "y": 3.22705816763, 
                                    "arrowhead": 1, 
                                    "arrowsize": 1.1, 
                                    "arrowwidth": 2, 
                                    "ax": 162, 
                                    "ay": -1, 
                                    "text": "18 April 1980 Zimbabwe; Rhodesia gains independence",
                                    "bgcolor": "rgb(19, 24, 26)",
                                    "arrowcolor": "rgb(19, 24, 26)"

                                  }, 
                                  {
                                    "x": "1980-04-24 03:25:36.7826", 
                                    "y": 4.28366474633, 
                                    "arrowhead": 1, 
                                    "arrowwidth": 2, 
                                    "ax": 194, 
                                    "ay": -1, 
                                    "text": "24 April 1980 Commando raid to rescue hostages in Teheran fails",
                                    "bgcolor": "rgb(19, 24, 26)",
                                    "arrowcolor": "rgb(19, 24, 26)"
                                  }, 
                                  {
                                    "x": "1980-05-18 03:54:30.6635", 
                                    "y": 2.19966548969, 
                                    "arrowhead": 1, 
                                    "arrowwidth": 2, 
                                    "ax": 116, 
                                    "ay": -2, 
                                    "text": "18 May 1980 Mount St. Helens erupts",
                                    "bgcolor": "rgb(19, 24, 26)",
                                    "arrowcolor": "rgb(19, 24, 26)"
                                  }, 
                                  {
                                    "x": "1980-09-22 04:45:36.2971", 
                                    "y": 4, 
                                    "arrowhead": 1, 
                                    "arrowwidth": 2, 
                                    "ax": 112, 
                                    "ay": -1, 
                                    "text": "22 September 1980 Iraq invades Iran",
                                    "bgcolor": "rgb(19, 24, 26)",
                                    "arrowcolor": "rgb(19, 24, 26)"
                                  }, 
                                  {
                                    "x": "1981-08-12 07:48:15.3676", 
                                    "y": 3.25158892399, 
                                    "arrowhead": 1, 
                                    "arrowwidth": 2, 
                                    "ax": 158, 
                                    "ay": -3, 
                                    "text": "12 August 1981 Personal computer launched by IBM",
                                    "bgcolor": "rgb(19, 24, 26)",
                                    "arrowcolor": "rgb(19, 24, 26)"
                                  }, 
                                  {
                                    "x": "1981-10-06 02:38:38.6889", 
                                    "y": 7.26905779595, 
                                    "arrowhead": 1, 
                                    "arrowwidth": 2, 
                                    "ax": 177, 
                                    "ay": 0, 
                                    "text": "6 October 1981 President Anwar Sadat assassinated in Cairo",
                                    "bgcolor": "rgb(19, 24, 26)",
                                    "arrowcolor": "rgb(19, 24, 26)"
                                  }, 
                                  {
                                    "x": "1982-03-01 01:19:50.1673", 
                                    "y": 6.320832559, 
                                    "arrowhead": 1, 
                                    "arrowwidth": 2, 
                                    "ax": 186, 
                                    "ay": -2, 
                                    "text": "1 March 1982 Venera 13 sends first colour photos from Venus",
                                    "bgcolor": "rgb(19, 24, 26)",
                                    "arrowcolor": "rgb(19, 24, 26)"
                                  }, 
                                  {
                                    "x": "1982-04-02 08:04:06.3342", 
                                    "y": 5.80635569597, 
                                    "arrowhead": 1, 
                                    "arrowwidth": 2, 
                                    "ax": -245, 
                                    "ay": -1, 
                                    "text": "2 April 1982 &nbsp;Argentine forces mounted amphibious landings on the Falkland Islands",
                                    "bgcolor": "rgb(19, 24, 26)",
                                    "arrowcolor": "rgb(19, 24, 26)"
                                  }, 
                                  {
                                    "x": "1982-06-05 23:31:24.3628", 
                                    "y": 4.33451031407, 
                                    "arrowhead": 1, 
                                    "arrowsize": 2, 
                                    "arrowwidth": 2, 
                                    "ax": 113, 
                                    "ay": -1, 
                                    "text": "6 June 1982 Israel invades Lebanon",
                                    "bgcolor": "rgb(19, 24, 26)",
                                    "arrowcolor": "rgb(19, 24, 26)"
                                  }, 
                                  {
                                    "x": "1983-04-04 06:10:46.5954", 
                                    "y": 5.20490615127, 
                                    "arrowhead": 1, 
                                    "arrowwidth": 2, 
                                    "ax": -176, 
                                    "ay": -2, 
                                    "text": "4 April 1983 Maiden voyage of US Space Shuttle Challenger",
                                    "bgcolor": "rgb(19, 24, 26)",
                                    "arrowcolor": "rgb(19, 24, 26)"
                                  }
                            ],                                                                                      
                            autosize= True, 
                            barmode= "stack", 
                            dragmode= "pan",
                            font= {"color": "rgb(255, 255, 255)"}, 
                            paper_bgcolor= "rgb(19, 24, 26)", 
                            plot_bgcolor="rgb(19, 24, 26)",
                            xaxis={'autorange': False, 'fixedrange': True, 'range':  ["1979-11-29 22:29:06.0351", "1984-03-23 01:30:53.9649"], "rangeslider": {
                            "autorange": True, 
                            "range": ["1979-11-21 16:50:28.6807", "1984-03-31 07:09:31.3193"], 
                            "thickness": 0.15, 
                            "visible": True, 
                            "yaxis": {"rangemode": "match"},
                            },
                            },
                            yaxis=  {
                               "autorange": True, 
                               "fixedrange": True, 
                               "range": [0.428316052914, 7.57168394709], 
                               "title": "colours",
                               "type": "linear"
                           },
                ),
            },
        )
    elif value == 2:
        return dcc.Graph(style={'height': '600px'},
        id='Rain-Cal-N17',
            figure={
                 'data': [
                       go.Scatter(
                                  x=d22,
                                  y= z1[:],
                                  text= m[:],
                                  mode='markers+lines',
                                  opacity=0.7,
                                  visible=True,
                                  hoverinfo = "x+y+name",
                                  marker={
                                  'size': 13,
                                  'line': {'width': 1},
                                  'autocolorscale': False,
                                  'cauto': False,
                                  'cmax': 7,
                                  'cmin': 1,
                                  'color': z1[:],
                                  'colorscale': [[0, "#ff0000"], [0.142857142857143, "#ffae01"], [0.3333333333333, "#fff600"], [0.5555555555555, "#0aff04"], [0.6666666666666, "#0569ff"], [0.777777777777, "#a201ff"], [0.8888888888888, "#ff03ea"], [1.0000000, "#ff03ea"]],
                                  'colorsrc': "robotwax:157:00284a",
                                  'reversescale': False,
                                  'showscale': True,
                                  "size": 16, 
                                  "symbol": "star-triangle-up"
                                  },
                                  ),
                       ],
              
              'layout': go.Layout(
                                  {'title': 'RCC-14 Historical Data'},
                                  margin= {"t": 100},
                                  annotations= [
                                    {
                                      "x": "1984-05-13 02:57:32.5952", 
                                      "y": 5.15298560302, 
                                      "arrowcolor": "rgb(19, 24, 26)", 
                                      "arrowhead": 1, 
                                      "arrowsize": 1.1, 
                                      "arrowwidth": 2, 
                                      "ax": 262, 
                                      "ay": -4, 
                                      "bgcolor": "rgb(19, 24, 26)", 
                                      "text": "13 May 1984 Explosion destroys a third of the Soviet Northern Fleet’s surface-to-air missiles"
                                    }, 
                                    {
                                      "x": "1985-01-17 07:47:47.8603", 
                                      "y": 6.08208638187, 
                                      "arrowcolor": "rgb(19, 24, 26)", 
                                      "arrowhead": 1, 
                                      "arrowwidth": 2, 
                                      "ax": 234, 
                                      "ay": -17, 
                                      "bgcolor": "rgb(19, 24, 26)", 
                                      "text": "3 December 1984 The Bhopal disaster also referred to as the Bhopal gas tragedy"
                                    }, 
                                    {
                                      "x": "1985-07-22 17:07:09.8984", 
                                      "y": 5.01774840689, 
                                      "arrowcolor": "rgb(19, 24, 26)", 
                                      "arrowhead": 1, 
                                      "arrowwidth": 2, 
                                      "ax": 96, 
                                      "ay": 33, 
                                      "bgcolor": "rgb(19, 24, 26)", 
                                      "text": "23 June 1985  Air India Flight 182 disaster passenger jet explosion off the coast of Ireland"
                                    }, 
                                    {
                                      "x": "1985-09-22 16:11:41.0534", 
                                      "y": 1.94666037291, 
                                      "arrowcolor": "rgb(19, 24, 26)", 
                                      "arrowhead": 1, 
                                      "arrowwidth": 2, 
                                      "ax": 129, 
                                      "ay": -2, 
                                      "bgcolor": "rgb(19, 24, 26)", 
                                      "text": "19 September 1985 Mexico City earthquake"
                                    }, 
                                    {
                                      "x": "1985-11-29 05:35:11.5385", 
                                      "y": 4.99339155063, 
                                      "arrowcolor": "rgb(19, 24, 26)", 
                                      "arrowhead": 1, 
                                      "arrowwidth": 2, 
                                      "ax": 191, 
                                      "ay": 4, 
                                      "bgcolor": "rgb(19, 24, 26)", 
                                      "text": "15 November 1985 the UK and Ireland sign the Anglo-Irish Treaty"
                                    }, 
                                    {
                                      "x": "1986-11-06 09:14:44.3736", 
                                      "y": 6.03705451971, 
                                      "arrowcolor": "rgb(19, 24, 26)", 
                                      "arrowhead": 1, 
                                      "arrowwidth": 2, 
                                      "ax": 107, 
                                      "ay": 0, 
                                      "bgcolor": "rgb(19, 24, 26)", 
                                      "text": "28 January 1986 Challenger disaster"
                                    }, 
                                    {
                                      "x": "1986-03-19 04:21:47.1981", 
                                      "y": 5.45702147746, 
                                      "arrowcolor": "rgb(19, 24, 26)", 
                                      "arrowhead": 1, 
                                      "arrowwidth": 2, 
                                      "ax": -199, 
                                      "ay": -2, 
                                      "bgcolor": "rgb(19, 24, 26)", 
                                      "text": "28 February 1986 Prime Minister of Sweden Olof Palme was shot dead"
                                    }, 
                                    {
                                      "x": "1986-03-22 00:46:21.888", 
                                      "y": 6.0471088034, 
                                      "arrowcolor": "rgb(19, 24, 26)", 
                                      "arrowhead": 1, 
                                      "arrowwidth": 2, 
                                      "ax": -257, 
                                      "ay": -1, 
                                      "bgcolor": "rgb(19, 24, 26)", 
                                      "text": "13 March 1986 Europes Giotto space probe passed closest to the nucleus Halley\’s Comet"
                                    }, 
                                    {
                                      "x": "1986-05-07 09:40:50.6233", 
                                      "y": 1.04913854142, 
                                      "arrowcolor": "rgb(19, 24, 26)", 
                                      "arrowhead": 1, 
                                      "arrowsize": 2, 
                                      "arrowwidth": 2, 
                                      "ax": 103, 
                                      "ay": -2, 
                                      "bgcolor": "rgb(19, 24, 26)", 
                                      "text": "26 April 1986 Chernobyl disaster"
                                    }, 
                                    {
                                      "x": "1987-10-19 06:10:46.5954", 
                                      "y": 5.20490615127, 
                                      "arrowcolor": "rgb(19, 24, 26)", 
                                      "arrowhead": 1, 
                                      "arrowwidth": 2, 
                                      "ax": -176, 
                                      "ay": -2, 
                                      "bgcolor": "rgb(19, 24, 26)", 
                                      "text": "19 October 1987 Black Monday"
                                    }
                                  ],                                                                        
                                  autosize= True, 
                                  barmode= "stack", 
                                  dragmode= "pan",
                                  font= {"color": "rgb(255, 255, 255)"}, 
                                  paper_bgcolor= "rgb(19, 24, 26)", 
                                  plot_bgcolor="rgb(19, 24, 26)",
                                  xaxis={'autorange': False, 'fixedrange': True, 'range': ["1983-09-26 07:38:26.5612", "1988-01-26 16:21:33.4388"], "rangeslider": {
                                  "autorange": True, 
                                  "range": ["1983-09-26 07:38:26.5612", "1988-01-26 16:21:33.4388"], 
                                  "thickness": 0.15,
                                  "visible": True, 
                                  "yaxis": {"rangemode": "match"},
                                  },
                                  },
                                  yaxis=  {
                                     "autorange": True, 
                                     "fixedrange": True, 
                                     "range": [0.428316052914, 7.57168394709], 
                                     "title": "colours",
                                     "type": "linear"
                                  },
                      ),
            },
        ),

    elif value == 3:
        return dcc.Graph(style={'height': '600px'},
        id='Rain-Cal-N17',
            figure={
                 'data': [
                       go.Scatter(
                                  x=d27,
                                  y= z1[:],
                                  text= m[:],
                                  mode='markers+lines',
                                  opacity=0.7,
                                  visible=True,
                                  hoverinfo = "x+y+name",
                                  marker={
                                  'size': 13,
                                  'line': {'width': 1},
                                  'autocolorscale': False,
                                  'cauto': False,
                                  'cmax': 7,
                                  'cmin': 1,
                                  'color': z1[:],
                                  'colorscale': [[0, "#ff0000"], [0.142857142857143, "#ffae01"], [0.3333333333333, "#fff600"], [0.5555555555555, "#0aff04"], [0.6666666666666, "#0569ff"], [0.777777777777, "#a201ff"], [0.8888888888888, "#ff03ea"], [1.0000000, "#ff03ea"]],
                                  'colorsrc': "robotwax:157:00284a",
                                  'reversescale': False,
                                  'showscale': True,
                                  "size": 16, 
                                  "symbol": "star-triangle-up"
                                  },
                                  ),
                       ],
              
              'layout': go.Layout(
                                  {'title': 'RCC-14 Historical Data'},
                                  margin= {"t": 100},
                                  annotations= [
                                    {
                                      "x": "1988-11-03 22:20:01.6147", 
                                      "y": 1.05879082696, 
                                      "arrowcolor": "rgb(19, 24, 26)", 
                                      "arrowhead": 1, 
                                      "arrowsize": 1.1, 
                                      "arrowwidth": 2, 
                                      "ax": 195, 
                                      "ay": -3, 
                                      "bgcolor": "rgb(19, 24, 26)", 
                                      "text": "2 November 1988 Internet virus jams over 6000 military computers"
                                    }, 
                                    {
                                      "x": "1988-11-03 00:20:52.6451", 
                                      "y": 7.03564975678, 
                                      "arrowcolor": "rgb(19, 24, 26)", 
                                      "arrowhead": 1, 
                                      "arrowwidth": 2, 
                                      "ax": 120, 
                                      "ay": -1, 
                                      "bgcolor": "rgb(19, 24, 26)", 
                                      "text": "7 December 1988 Armenian earthquake"
                                    }, 
                                    {
                                      "x": "1988-12-21 04:06:45.3413", 
                                      "y": 3.05434329395, 
                                      "arrowcolor": "rgb(19, 24, 26)", 
                                      "arrowhead": 1, 
                                      "arrowwidth": 2, 
                                      "ax": 117, 
                                      "ay": 0, 
                                      "bgcolor": "rgb(19, 24, 26)", 
                                      "text": "21 December 1988 Lockerbie bombing"
                                    }, 
                            ],                                                    

                                  autosize= True, 
                                  barmode= "stack", 
                                  dragmode= "pan",
                                  font= {"color": "rgb(255, 255, 255)"}, 
                                  paper_bgcolor= "rgb(19, 24, 26)", 
                                  plot_bgcolor="rgb(19, 24, 26)",
                                  xaxis={'autorange': False, 'fixedrange': True, 'range':  ("1987-07-28 07:38:26.5612", "1992-01-19 16:21:33.4388"), "rangeslider": {
                                  "autorange": True, 
                                  "range": ("1987-07-28 07:38:26.5612", "1992-01-19 16:21:33.4388"),  
                                  "thickness": 0.15, 
                                  "visible": True, 
                                  "yaxis": {"rangemode": "match"},
                                  },
                                  },
                                  yaxis=  {
                                     "autorange": True, 
                                     "fixedrange": True, 
                                     "range": [0.428316052914, 7.57168394709], 
                                     "title": "colours",
                                     "type": "linear"
                                   },
                      ),
            },
        ),
    elif value == 4:
        return dcc.Graph(style={'height': '600px'},
        id='Rain-Cal-N17',
            figure={
                 'data': [
                       go.Scatter(
                                  x=d32,
                                  y= z1[:],
                                  text= m[:],
                                  mode='markers+lines',
                                  opacity=0.7,
                                  visible=True,
                                  hoverinfo = "x+y+name",
                                  marker={
                                  'size': 13,
                                  'line': {'width': 1},
                                  'autocolorscale': False,
                                  'cauto': False,
                                  'cmax': 7,
                                  'cmin': 1,
                                  'color': z1[:],
                                  'colorscale': [[0, "#ff0000"], [0.142857142857143, "#ffae01"], [0.3333333333333, "#fff600"], [0.5555555555555, "#0aff04"], [0.6666666666666, "#0569ff"], [0.777777777777, "#a201ff"], [0.8888888888888, "#ff03ea"], [1.0000000, "#ff03ea"]],
                                  'colorsrc': "robotwax:157:00284a",
                                  'reversescale': False,
                                  'showscale': True,
                                  "size": 16, 
                                  "symbol": "star-triangle-up"
                                  },
                                  ),
                       ],
              
              'layout': go.Layout(
                                  {'title': 'RCC-14 Historical Data'},
                                  margin= {"t": 100},
                                  annotations= [
                                    {
                                      "x": "1991-12-25 04:46:42.2305", 
                                      "y": 7.06462821404, 
                                      "arrowcolor": "rgb(19, 24, 26)", 
                                      "arrowhead": 1, 
                                      "arrowwidth": 2, 
                                      "ax": 157, 
                                      "ay": 7, 
                                      "bgcolor": "rgb(19, 24, 26)", 
                                      "text": "25 December 1991 Gorbachev resigns as president"
                                    }, 
                                    {
                                      "x": "1993-01-01 03:18:25.3699", 
                                      "y": 3.05371785962, 
                                      "arrowcolor": "rgb(19, 24, 26)", 
                                      "arrowhead": 1, 
                                      "arrowwidth": 2, 
                                      "ax": -152, 
                                      "ay": -1, 
                                      "bgcolor": "rgb(19, 24, 26)", 
                                      "text": "1 January 1993  The European Single Market begins"
                                    }, 
                                    {
                                      "x": "1993-02-26 03:49:16.663", 
                                      "y": 6.05642807505, 
                                      "arrowcolor": "rgb(19, 24, 26)", 
                                      "arrowhead": 1, 
                                      "arrowwidth": 2, 
                                      "ax": 99, 
                                      "ay": -2, 
                                      "bgcolor": "rgb(19, 24, 26)", 
                                      "text": "26 February 1993 WTC bombing"
                                    }, 
                                    {
                                      "x": "1993-04-19 04:52:40.7289", 
                                      "y": 3.02015288395, 
                                      "arrowcolor": "rgb(19, 24, 26)", 
                                      "arrowhead": 1, 
                                      "arrowwidth": 2, 
                                      "ax": 93, 
                                      "ay": -1, 
                                      "bgcolor": "rgb(19, 24, 26)", 
                                      "text": "19 April 1993 Waco siege ends"
                                    }, 
                                    {
                                      "x": "1994-01-17 07:45:12.6059", 
                                      "y": 5.02362751911, 
                                      "arrowcolor": "rgb(19, 24, 26)", 
                                      "arrowhead": 1, 
                                      "arrowwidth": 2, 
                                      "ax": 155, 
                                      "ay": -2, 
                                      "bgcolor": "rgb(19, 24, 26)", 
                                      "text": "17 January 1994 Northridge earthquake; Los Angeles"
                                    }, 
                                    {
                                      "x": "1994-07-05 22:31:15.6356", 
                                      "y": 5.99742876998, 
                                      "arrowcolor": "rgb(19, 24, 26)", 
                                      "arrowhead": 1, 
                                      "arrowwidth": 2, 
                                      "ax": -226, 
                                      "ay": -24, 
                                      "bgcolor": "rgb(19, 24, 26)", 
                                      "text": "22 July 1994 The last fragments of Comet P/Shoemaker-Levy 9 collided with Jupiter"
                                    }, 
                                    {
                                      "x": "1995-02-02 22:53:17.7168", 
                                      "y": 4.06921473245, 
                                      "arrowcolor": "rgb(19, 24, 26)", 
                                      "arrowhead": 1, 
                                      "arrowwidth": 2, 
                                      "ax": -100, 
                                      "ay": -2, 
                                      "bgcolor": "rgb(19, 24, 26)", 
                                      "text": "17 January 1995 Kobe earthquake"
                                    }, 
                                    {
                                      "x": "1995-04-19 08:09:33.1548", 
                                      "y": 0.990410006949, 
                                      "arrowcolor": "rgb(19, 24, 26)", 
                                      "arrowhead": 1, 
                                      "arrowwidth": 2, 
                                      "ax": -101, 
                                      "ay": -9, 
                                      "bgcolor": "rgb(19, 24, 26)", 
                                      "text": "19 April 1995 Oklahoma bombing"
                                    }
                                  ], 
                                  autosize= True, 
                                  barmode= "stack", 
                                  dragmode= "pan",
                                  font= {"color": "rgb(255, 255, 255)"}, 
                                  paper_bgcolor= "rgb(19, 24, 26)", 
                                  plot_bgcolor="rgb(19, 24, 26)",
                                  xaxis={'autorange': False, 'fixedrange': True, 'range':  ("1991-05-19", "1995-09-18"), "rangeslider": {
                                  "autorange": True, 
                                  "range": ("1991-05-19", "1995-04-28"),  
                                  "thickness": 0.15, 
                                  "visible": True, 
                                  "yaxis": {"rangemode": "match"},
                                  },
                                  },
                                  yaxis=  {
                                     "autorange": True, 
                                     "fixedrange": True, 
                                     "range": [0.428316052914, 7.57168394709], 
                                     "title": "colours",
                                     "type": "linear"
                                   },
                      ),
            },
        ),
    elif value == 5:
        return dcc.Graph(style={'height': '600px'},
        id='Rain-Cal-N17',
            figure={
                 'data': [
                       go.Scatter(
                                  x=d37,
                                  y= z1[:],
                                  text= m[:],
                                  mode='markers+lines',
                                  opacity=0.7,
                                  visible=True,
                                  hoverinfo = "x+y+name",
                                  marker={
                                  'size': 13,
                                  'line': {'width': 1},
                                  'autocolorscale': False,
                                  'cauto': False,
                                  'cmax': 7,
                                  'cmin': 1,
                                  'color': z1[:],
                                  'colorscale': [[0, "#ff0000"], [0.142857142857143, "#ffae01"], [0.3333333333333, "#fff600"], [0.5555555555555, "#0aff04"], [0.6666666666666, "#0569ff"], [0.777777777777, "#a201ff"], [0.8888888888888, "#ff03ea"], [1.0000000, "#ff03ea"]],
                                  'colorsrc': "robotwax:157:00284a",
                                  'reversescale': False,
                                  'showscale': True,
                                  "size": 16, 
                                  "symbol": "star-triangle-up"
                                  },
                                  ),
                       ],
              
              'layout': go.Layout(
                                  {'title': 'RCC-14 Historical Data'},
                                  margin= {"t": 100},
                            annotations= [
                                  {
                                    "x": "1997-02-22 03:01:15.3929", 
                                    "y": 3.11705816763, 
                                    "arrowhead": 1, 
                                    "arrowsize": 1.1, 
                                    "arrowwidth": 2, 
                                    "ax": 174, 
                                    "ay": -1, 
                                    "text": "22 February 1997 Dolly the sheep announced to public",
                                    "bgcolor": "rgb(19, 24, 26)",
                                    "arrowcolor": "rgb(19, 24, 26)"

                                  }, 
                                  {
                                    "x": "1998-04-10 03:25:36.7826", 
                                    "y": 4.28366474633, 
                                    "arrowhead": 1, 
                                    "arrowwidth": 2, 
                                    "ax": 134, 
                                    "ay": -1, 
                                    "text": "10 April 1998 The Good Friday Agreement",
                                    "bgcolor": "rgb(19, 24, 26)",
                                    "arrowcolor": "rgb(19, 24, 26)"
                                  }, 
                            ],                                                    

                                  autosize= True, 
                                  barmode= "stack", 
                                  dragmode= "pan",
                                  font= {"color": "rgb(255, 255, 255)"}, 
                                  paper_bgcolor= "rgb(19, 24, 26)", 
                                  plot_bgcolor="rgb(19, 24, 26)",
                                  xaxis={'autorange': False, 'fixedrange': True, 'range':  (d33, d34), "rangeslider": {
                                  "autorange": True, 
                                  "range": (d33, d34),  
                                  "thickness": 0.15, 
                                  "visible": True, 
                                  "yaxis": {"rangemode": "match"},
                                  },
                                  },
                                  yaxis=  {
                                     "autorange": True, 
                                     "fixedrange": True, 
                                     "range": [0.428316052914, 7.57168394709], 
                                     "title": "colours",
                                     "type": "linear"
                                   },
                      ),
            },
        ),
    elif value == 6:
        return dcc.Graph(style={'height': '600px'},
        id='Rain-Cal-N17',
            figure={
                 'data': [
                       go.Scatter(
                                  x=d42,
                                  y= z1[:],
                                  text= m[:],
                                  mode='markers+lines',
                                  opacity=0.7,
                                  visible=True,
                                  hoverinfo = "x+y+name",
                                  marker={
                                  'size': 13,
                                  'line': {'width': 1},
                                  'autocolorscale': False,
                                  'cauto': False,
                                  'cmax': 7,
                                  'cmin': 1,
                                  'color': z1[:],
                                  'colorscale': [[0, "#ff0000"], [0.142857142857143, "#ffae01"], [0.3333333333333, "#fff600"], [0.5555555555555, "#0aff04"], [0.6666666666666, "#0569ff"], [0.777777777777, "#a201ff"], [0.8888888888888, "#ff03ea"], [1.0000000, "#ff03ea"]],
                                  'colorsrc': "robotwax:157:00284a",
                                  'reversescale': False,
                                  'showscale': True,
                                  "size": 16, 
                                  "symbol": "star-triangle-up"
                                  },
                                  ),
                       ],
              
              'layout': go.Layout(
                                  {'title': 'RCC-14 Historical Data'},
                                  margin= {"t": 100},
                            annotations= [
                                  {
                                    "x": "1999-10-31 03:01:15.3929", 
                                    "y": 1.22705816763, 
                                    "arrowhead": 1, 
                                    "arrowsize": 1.1, 
                                    "arrowwidth": 2, 
                                    "ax": 195, 
                                    "ay": -1, 
                                    "text": "31 October 1999 EgyptAir flight MS804 crashes over Atlantic",
                                    "bgcolor": "rgb(19, 24, 26)",
                                    "arrowcolor": "rgb(19, 24, 26)"

                                  }, 
                                 {
                                    "x": "2000-01-01 07:48:15.3676", 
                                    "y": 5.25158892399, 
                                    "arrowhead": 1, 
                                    "arrowwidth": 2, 
                                    "ax": 118, 
                                    "ay": -3, 
                                    "text": "1 January 2000 Y2K bug fails to happen",
                                    "bgcolor": "rgb(19, 24, 26)",
                                    "arrowcolor": "rgb(19, 24, 26)"
                                  }, 
                                  {
                                    "x": "2001-02-12 03:25:36.7826", 
                                    "y": 6.28366474633, 
                                    "arrowhead": 1, 
                                    "arrowwidth": 2, 
                                    "ax": 254, 
                                    "ay": -1, 
                                    "text": "12 February 2001 the NASA NEAR Shoemaker spacecraft lands on asteroid 433 Eros",
                                    "bgcolor": "rgb(19, 24, 26)",
                                    "arrowcolor": "rgb(19, 24, 26)"
                                  }, 
                                  {
                                    "x": "2001-09-11 03:54:30.6635", 
                                    "y": 4.19966548969, 
                                    "arrowhead": 1, 
                                    "arrowwidth": 2, 
                                    "ax": 110, 
                                    "ay": -2, 
                                    "text": "11 September 2001 9/11 Attacks",
                                    "bgcolor": "rgb(19, 24, 26)",
                                    "arrowcolor": "rgb(19, 24, 26)"
                                  }, 
                                  {
                                    "x": "2003-02-01 04:45:36.2971", 
                                    "y": 3.22, 
                                    "arrowhead": 1, 
                                    "arrowwidth": 2, 
                                    "ax": -202, 
                                    "ay": -1, 
                                    "text": "1 February 2003 US Space Shuttle Columbia breaks up on reentry",
                                    "bgcolor": "rgb(19, 24, 26)",
                                    "arrowcolor": "rgb(19, 24, 26)"
                                  }, 
                             ],                                                    
                                  autosize= True, 
                                  barmode= "stack", 
                                  dragmode= "pan",
                                  font= {"color": "rgb(255, 255, 255)"}, 
                                  paper_bgcolor= "rgb(19, 24, 26)", 
                                  plot_bgcolor="rgb(19, 24, 26)",
                                  xaxis={'autorange': False, 'fixedrange': True, 'range':  (d38, d39), "rangeslider": {
                                  "autorange": True, 
                                  "range": (d38, d49),  
                                  "thickness": 0.15, 
                                  "visible": True, 
                                  "yaxis": {"rangemode": "match"},
                                  },
                                  },
                                  yaxis=  {
                                     "autorange": True, 
                                     "fixedrange": True, 
                                     "range": [0.428316052914, 7.57168394709], 
                                     "title": "colours",
                                     "type": "linear"
                                   },
                      ),
            },
        ),
    elif value == 7:
        return dcc.Graph(style={'height': '600px'},
        id='Rain-Cal-N17',
            figure={
                 'data': [
                       go.Scatter(
                                  x=d47,
                                  y= z1[:],
                                  text= m[:],
                                  mode='markers+lines',
                                  opacity=0.7,
                                  visible=True,
                                  hoverinfo = "x+y+name",
                                  marker={
                                  'size': 13,
                                  'line': {'width': 1},
                                  'autocolorscale': False,
                                  'cauto': False,
                                  'cmax': 7,
                                  'cmin': 1,
                                  'color': z1[:],
                                  'colorscale': [[0, "#ff0000"], [0.142857142857143, "#ffae01"], [0.3333333333333, "#fff600"], [0.5555555555555, "#0aff04"], [0.6666666666666, "#0569ff"], [0.777777777777, "#a201ff"], [0.8888888888888, "#ff03ea"], [1.0000000, "#ff03ea"]],
                                  'colorsrc': "robotwax:157:00284a",
                                  'reversescale': False,
                                  'showscale': True,
                                  "size": 16, 
                                  "symbol": "star-triangle-up"
                                  },
                                  ),
                       ],
              
              'layout': go.Layout(
                                  {'title': 'RCC-14 Historical Data'},
                                  margin= {"t": 100},
                            annotations= [
                                  {
                                    "x": "2003-03-20 03:01:15.3929", 
                                    "y": 3.22705816763, 
                                    "arrowhead": 1, 
                                    "arrowsize": 1.1, 
                                    "arrowwidth": 2, 
                                    "ax": 162, 
                                    "ay": -1, 
                                    "text": "20 March 2003  Iraq War The invasion phase",
                                    "bgcolor": "rgb(19, 24, 26)",
                                    "arrowcolor": "rgb(19, 24, 26)"

                                  }, 
                                  {
                                    "x": "2004-01-03 03:25:36.7826", 
                                    "y": 4.28366474633, 
                                    "arrowhead": 1, 
                                    "arrowwidth": 2, 
                                    "ax": 194, 
                                    "ay": -1, 
                                    "text": "3 January 2004 Mars Rover Spirit lands on Mars",
                                    "bgcolor": "rgb(19, 24, 26)",
                                    "arrowcolor": "rgb(19, 24, 26)"
                                  }, 
                                  {
                                    "x": "2004-03-11 03:54:30.6635", 
                                    "y": 2.19966548969, 
                                    "arrowhead": 1, 
                                    "arrowwidth": 2, 
                                    "ax": 116, 
                                    "ay": -2, 
                                    "text": "11 March 2004 The Madrid Train Bombings",
                                    "bgcolor": "rgb(19, 24, 26)",
                                    "arrowcolor": "rgb(19, 24, 26)"
                                  }, 
                                  {
                                    "x": "2004-12-26 04:45:36.2971", 
                                    "y": 4, 
                                    "arrowhead": 1, 
                                    "arrowwidth": 2, 
                                    "ax": 112, 
                                    "ay": -1, 
                                    "text": "26 December 2004 Boxing day Tsunami",
                                    "bgcolor": "rgb(19, 24, 26)",
                                    "arrowcolor": "rgb(19, 24, 26)"
                                  }, 
                                  {
                                    "x": "2005-01-14 07:48:15.3676", 
                                    "y": 3.25158892399, 
                                    "arrowhead": 1, 
                                    "arrowwidth": 2, 
                                    "ax": 158, 
                                    "ay": -3, 
                                    "text": "14 January 2005 the Huygens probe lands on Titan",
                                    "bgcolor": "rgb(19, 24, 26)",
                                    "arrowcolor": "rgb(19, 24, 26)"
                                  }, 
                                  {
                                    "x": "2005-07-07 02:38:38.6889", 
                                    "y": 7.26905779595, 
                                    "arrowhead": 1, 
                                    "arrowwidth": 2, 
                                    "ax": 177, 
                                    "ay": 0, 
                                    "text": "7 July 2005 7/7 Attacks London",
                                    "bgcolor": "rgb(19, 24, 26)",
                                    "arrowcolor": "rgb(19, 24, 26)"
                                  }, 
                            ],                                                    

                                  autosize= True, 
                                  barmode= "stack", 
                                  dragmode= "pan",
                                  font= {"color": "rgb(255, 255, 255)"}, 
                                  paper_bgcolor= "rgb(19, 24, 26)", 
                                  plot_bgcolor="rgb(19, 24, 26)",
                                  xaxis={'autorange': False, 'fixedrange': True, 'range':  (d43, d44), "rangeslider": {
                                  "autorange": True, 
                                  "range": (d43, d44),  
                                  "thickness": 0.15, 
                                  "visible": True, 
                                  "yaxis": {"rangemode": "match"},
                                  },
                                  },
                                  yaxis=  {
                                     "autorange": True, 
                                     "fixedrange": True, 
                                     "range": [0.428316052914, 7.57168394709], 
                                     "title": "colours",
                                     "type": "linear"
                                   },
                      ),
            },
        ),
    else:
        return dcc.Graph(style={'height': '600px'},
        id='Rain-Cal-N17',
            figure={
                 'data': [
                       go.Scatter(
                                  x=d52,
                                  y= z1[:],
                                  text= m[:],
                                  mode='markers+lines',
                                  opacity=0.7,
                                  visible=True,
                                  hoverinfo = "x+y+name",
                                  marker={
                                  'size': 13,
                                  'line': {'width': 1},
                                  'autocolorscale': False,
                                  'cauto': False,
                                  'cmax': 7,
                                  'cmin': 1,
                                  'color': z1[:],
                                  'colorscale': [[0, "#ff0000"], [0.142857142857143, "#ffae01"], [0.3333333333333, "#fff600"], [0.5555555555555, "#0aff04"], [0.6666666666666, "#0569ff"], [0.777777777777, "#a201ff"], [0.8888888888888, "#ff03ea"], [1.0000000, "#ff03ea"]],
                                  'colorsrc': "robotwax:157:00284a",
                                  'reversescale': False,
                                  'showscale': True,
                                  "size": 16, 
                                  "symbol": "star-triangle-up"
                                  },
                                  ),
                       ],
              
              'layout': go.Layout(
                                  {'title': 'RCC-14 Historical Data'},
                                  margin= {"t": 100},
                            annotations= [
                                  {
                                    "x": "2008-09-15 03:01:15.3929", 
                                    "y": 7.22705816763, 
                                    "arrowhead": 1, 
                                    "arrowsize": 1.1, 
                                    "arrowwidth": 2, 
                                    "ax": 147, 
                                    "ay": -1, 
                                    "text": "15 September 2008 Lehman Brothers goes bust",
                                    "bgcolor": "rgb(19, 24, 26)",
                                    "arrowcolor": "rgb(19, 24, 26)"

                                  }, 
                                  {
                                    "x": "2008-11-04 03:25:36.7826", 
                                    "y": 3.28366474633, 
                                    "arrowhead": 1, 
                                    "arrowwidth": 2, 
                                    "ax": 134, 
                                    "ay": -1, 
                                    "text": "4 November 2008 Obama elected POTUS",
                                    "bgcolor": "rgb(19, 24, 26)",
                                    "arrowcolor": "rgb(19, 24, 26)"
                                  }, 
                                  {
                                    "x": "2010-03-11 03:54:30.6635", 
                                    "y": 6.19966548969, 
                                    "arrowhead": 1, 
                                    "arrowwidth": 2, 
                                    "ax": -86, 
                                    "ay": -2, 
                                    "text": "11 March 2010 Japan tsunami",
                                    "bgcolor": "rgb(19, 24, 26)",
                                    "arrowcolor": "rgb(19, 24, 26)"
                                  }, 
                                  {
                                    "x": "2010-04-20 04:45:36.2971", 
                                    "y": 5.8, 
                                    "arrowhead": 1, 
                                    "arrowwidth": 2, 
                                    "ax": -132, 
                                    "ay": -1, 
                                    "text": "20 April 2010  The Deepwater Horizon oil spill",
                                    "bgcolor": "rgb(19, 24, 26)",
                                    "arrowcolor": "rgb(19, 24, 26)"
                                  }, 
                            ],                                                    

                                  autosize= True, 
                                  barmode= "stack", 
                                  dragmode= "pan",
                                  font= {"color": "rgb(255, 255, 255)"}, 
                                  paper_bgcolor= "rgb(19, 24, 26)", 
                                  plot_bgcolor="rgb(19, 24, 26)",
                                  xaxis={'autorange': False, 'fixedrange': True, 'range':  (d48, d49), "rangeslider": {
                                  "autorange": True, 
                                  "range": (d48, d49),  
                                  "thickness": 0.15, 
                                  "visible": True, 
                                  "yaxis": {"rangemode": "match"},
                                  },
                                  },
                                  yaxis=  {
                                     "autorange": True, 
                                     "fixedrange": True, 
                                     "range": [0.428316052914, 7.57168394709], 
                                     "title": "colours",
                                     "type": "linear"
                                   },
                      ),
            },
        ),

@app.callback(dash.dependencies.Output('textbox-2', 'value'),
              [dash.dependencies.Input('slider2', 'value')])
def func(slider2):
    if slider2==1:
        y = [colour_dates != 'Red']
        z = nd.ma.masked_array(colour_dates,y)
        a = ma.masked_where(colour_dates != 'Red', dates)
        a = a.tolist()
        g = zip(z, a)
        g = (list(g))
        xy = list(itertools.chain(*g))
        k = [x for x in xy if x is not None]
        k = str(k)
        k = k.replace(' masked,', '')
        k = k.replace(' masked', '')
        k = k.replace('masked,', '')
        k = k.replace('[', '')
        k = k.replace(']', '')
        k = k.replace('\'', '')
        k = k.replace(',', '\n')
        return(k)
    elif slider2==2:
        y = [colour_dates != 'Orange']
        z = nd.ma.masked_array(colour_dates,y)
        z = z.tolist()
        a = ma.masked_where(colour_dates != 'Orange', dates)
        a = a.tolist()
        g = zip(z, a)
        g = (list(g))
        xy = list(itertools.chain(*g))
        k = [x for x in xy if x is not None]
        k = str(k)
        k = k.replace(' masked,', '')
        k = k.replace(' masked', '')
        k = k.replace('masked,', '')
        k = k.replace('[', '')
        k = k.replace(']', '')
        k = k.replace('\'', '')
        k = k.replace(',', '\n')
        return(k)
    elif slider2==3:
        y = [colour_dates != 'Yellow']
        z = nd.ma.masked_array(colour_dates,y)
        z = z.tolist()
        a = ma.masked_where(colour_dates != 'Yellow', dates)
        a = a.tolist()
        g = zip(z, a)
        g = (list(g))
        xy = list(itertools.chain(*g))
        k = [x for x in xy if x is not None]
        k = str(k)
        k = k.replace(' masked,', '')
        k = k.replace(' masked', '')
        k = k.replace('masked,', '')
        k = k.replace('[', '')
        k = k.replace(']', '')
        k = k.replace('\'', '')
        k = k.replace(',', '\n')
        return(k)
    elif slider2==4:
        y = [colour_dates != 'Green']
        z = nd.ma.masked_array(colour_dates,y)
        z = z.tolist()
        a = ma.masked_where(colour_dates != 'Green', dates)
        a = a.tolist()
        g = zip(z, a)
        g = (list(g))
        xy = list(itertools.chain(*g))
        k = [x for x in xy if x is not None]
        k = str(k)
        k = k.replace(' masked,', '')
        k = k.replace(' masked', '')
        k = k.replace('masked,', '')
        k = k.replace('[', '')
        k = k.replace(']', '')
        k = k.replace('\'', '')
        k = k.replace(',', '\n')
        return(k)
    elif slider2==5:
        y = [colour_dates != 'Blue']
        z = nd.ma.masked_array(colour_dates,y)
        z = z.tolist()
        a = ma.masked_where(colour_dates != 'Blue', dates)
        a = a.tolist()
        g = zip(z, a)
        g = (list(g))
        xy = list(itertools.chain(*g))
        k = [x for x in xy if x is not None]
        k = str(k)
        k = k.replace(' masked,', '')
        k = k.replace(' masked', '')
        k = k.replace('masked,', '')
        k = k.replace('[', '')
        k = k.replace(']', '')
        k = k.replace('\'', '')
        k = k.replace(',', '\n')
        return(k)
    elif slider2==6:
        y = [colour_dates != 'Indigo']
        z = nd.ma.masked_array(colour_dates,y)
        z = z.tolist()
        a = ma.masked_where(colour_dates != 'Indigo', dates)
        a = a.tolist()
        g = zip(z, a)
        g = (list(g))
        xy = list(itertools.chain(*g))
        k = [x for x in xy if x is not None]
        k = str(k)
        k = k.replace(' masked,', '')
        k = k.replace(' masked', '')
        k = k.replace('masked,', '')
        k = k.replace('[', '')
        k = k.replace(']', '')
        k = k.replace('\'', '')
        k = k.replace(',', '\n')
        return(k)
    elif slider2==7:
        y = [colour_dates != 'Violet']
        z = nd.ma.masked_array(colour_dates,y)
        z = z.tolist()
        a = ma.masked_where(colour_dates != 'Violet', dates)
        a = a.tolist()
        g = zip(z, a)
        g = (list(g))
        xy = list(itertools.chain(*g))
        k = [x for x in xy if x is not None]
        k = str(k)
        k = k.replace(' masked,', '')
        k = k.replace(' masked', '')
        k = k.replace('masked,', '')
        k = k.replace('[', '')
        k = k.replace(']', '')
        k = k.replace('\'', '')
        k = k.replace(',', '\n')
        return(k)
    else:
        zlist = zip(colour_dates, dates)
        for i in zlist:
            k = ('\n'.join(map(str, zlist)))
        k = k.replace('(', '')
        k = k.replace(')', '')
        k = k.replace('\'', '')
        k = k.replace(',', '\n')
        return(k)

@app.callback(dash.dependencies.Output('piechart-container', 'children'),
              [dash.dependencies.Input('slider2', 'value')])
def update(value):
        if value == 1:
            y = [colour_dates != 'Red']
            zd = nd.ma.masked_array(category,y)
            zd=zd.tolist()
            a = zd.count('Political Unrest')
            b = zd.count('Terrorism')
            c = zd.count('War')
            d = zd.count('Natural disaster')
            e = zd.count('Technological Innovation')
            f = zd.count('Manmade disaster')
            g = zd.count('Transportation disaster')
            h = zd.count('Political agreement')
            i = zd.count('Financial crash')
            j = zd.count('Political change')
            return html.Div(dcc.Graph(
                figure=go.Figure(
                    data=[
                        go.Pie(values= [a, b, c, d, e, f, g, h, i, j],
                                direction= 'counterclockwise', 
                                labels= ['Political Unrest', 'Terrorism', 'War', 'Natural disaster', 'Technological Innovation', 'Manmade disaster', 'Transportation disaster', 'Political agreement', 'Financial crash', 'Political change'], 
                            sort= False, 
                            marker={'colors':["#ef55f1", "#fb84ce", "#fcd471", "#f0ed35", "#96d310", "#61c10b", "#439064", "#3d719a""#2e21ea", "#6324f5"]})], layout={'title':'RED: In Categories'},
                        ),
                ),
            )
        elif value == 2:
            y = [colour_dates != 'Orange']
            zd = nd.ma.masked_array(category,y)
            zd=zd.tolist()
            a = zd.count('Political Unrest')
            b = zd.count('Terrorism')
            c = zd.count('War')
            d = zd.count('Natural disaster')
            e = zd.count('Technological Innovation')
            f = zd.count('Manmade disaster')
            g = zd.count('Transportation disaster')
            h = zd.count('Political agreement')
            i = zd.count('Financial crash')
            j = zd.count('Political change')
            return html.Div(dcc.Graph(
                figure=go.Figure(
                    data=[
                        go.Pie(values= [a, b, c, d, e, f, g, h, i, j],
                                direction= 'counterclockwise', 
                                labels= ['Political Unrest', 'Terrorism', 'War', 'Natural disaster', 'Technological Innovation', 'Manmade disaster', 'Transportation disaster', 'Political agreement',  'Financial crash', 'Political change'], 
                            sort= False, 
                            marker={'colors':["#ef55f1", "#fb84ce", "#fcd471", "#f0ed35", "#96d310", "#61c10b", "#439064", "#3d719a""#2e21ea", "#6324f5"]})], layout={'title':'ORANGE: In Categories'},
                        ),
                ),
            )
        elif value == 3:
            y = [colour_dates != 'Yellow']
            zd = nd.ma.masked_array(category,y)
            zd=zd.tolist()
            a = zd.count('Political Unrest')
            b = zd.count('Terrorism')
            c = zd.count('War')
            d = zd.count('Natural disaster')
            e = zd.count('Technological Innovation')
            f = zd.count('Manmade disaster')
            g = zd.count('Transportation disaster')
            h = zd.count('Political agreement')
            i = zd.count('Financial crash')
            j = zd.count('Political change')
            return html.Div(dcc.Graph(
                figure=go.Figure(
                    data=[
                        go.Pie(values= [a, b, c, d, e, f, g, h, i, j],
                                direction= 'counterclockwise', 
                                labels= ['Political Unrest', 'Terrorism', 'War', 'Natural disaster', 'Technological Innovation', 'Manmade disaster', 'Transportation disaster', 'Political agreement',  'Financial crash', 'Political change'], 
                            sort= False, 
                            marker={'colors':["#ef55f1", "#fb84ce", "#fcd471", "#f0ed35", "#96d310", "#61c10b", "#439064", "#3d719a""#2e21ea", "#6324f5"]})], layout={'title':'YELLOW: In Categories'},
                        ),
                ),
            )
        elif value == 4:
            y = [colour_dates != 'Green']
            zd = nd.ma.masked_array(category,y)
            zd=zd.tolist()
            a = zd.count('Political Unrest')
            b = zd.count('Terrorism')
            c = zd.count('War')
            d = zd.count('Natural disaster')
            e = zd.count('Technological Innovation')
            f = zd.count('Manmade disaster')
            g = zd.count('Transportation disaster')
            h = zd.count('Political agreement')
            i = zd.count('Financial crash')
            j = zd.count('Political change')
            return html.Div(dcc.Graph(
                figure=go.Figure(
                    data=[
                        go.Pie(values= [a, b, c, d, e, f, g, h, i, j],
                                direction= 'counterclockwise', 
                                labels= ['Political Unrest', 'Terrorism', 'War', 'Natural disaster', 'Technological Innovation', 'Manmade disaster', 'Transportation disaster', 'Political agreement', 'Financial crash', 'Political change'], 
                            sort= False, 
                            marker={'colors':["#ef55f1", "#fb84ce", "#fcd471", "#f0ed35", "#96d310", "#61c10b", "#439064", "#3d719a""#2e21ea", "#6324f5"]})], layout={'title':'GREEN: In Categories'},
                        ),
                ),
            )
        elif value == 5:
            y = [colour_dates != 'Blue']
            zd = nd.ma.masked_array(category,y)
            zd=zd.tolist()
            a = zd.count('Political Unrest')
            b = zd.count('Terrorism')
            c = zd.count('War')
            d = zd.count('Natural disaster')
            e = zd.count('Technological Innovation')
            f = zd.count('Manmade disaster')
            g = zd.count('Transportation disaster')
            h = zd.count('Political agreement')
            i = zd.count('Financial crash')
            j = zd.count('Political change')
            return html.Div(dcc.Graph(
                figure=go.Figure(
                    data=[
                        go.Pie(values= [a, b, c, d, e, f, g, h, i, j],
                                direction= 'counterclockwise', 
                                labels= ['Political Unrest', 'Terrorism', 'War', 'Natural disaster', 'Technological Innovation', 'Manmade disaster', 'Transportation disaster', 'Political agreement', 'Financial crash', 'Political change'], 
                            sort= False, 
                            marker={'colors':["#ef55f1", "#fb84ce", "#fcd471", "#f0ed35", "#96d310", "#61c10b", "#439064", "#3d719a""#2e21ea", "#6324f5"]})], layout={'title':'BLUE: In Categories'},
                        ),
                ),
            )
        elif value == 6:
            y = [colour_dates != 'Indigo']
            zd = nd.ma.masked_array(category,y)
            zd=zd.tolist()
            a = zd.count('Political Unrest')
            b = zd.count('Terrorism')
            c = zd.count('War')
            d = zd.count('Natural disaster')
            e = zd.count('Technological Innovation')
            f = zd.count('Manmade disaster')
            g = zd.count('Transportation disaster')
            h = zd.count('Political agreement')
            i = zd.count('Financial crash')
            j = zd.count('Political change')
            return html.Div(dcc.Graph(
                figure=go.Figure(
                    data=[
                        go.Pie(values= [a, b, c, d, e, f, g, h, i, j],
                                direction= 'counterclockwise', 
                                labels= ['Political Unrest', 'Terrorism', 'War', 'Natural disaster', 'Technological Innovation', 'Manmade disaster', 'Transportation disaster', 'Political agreement', 'Financial crash', 'Political change'], 
                            sort= False, 
                            marker={'colors':["#ef55f1", "#fb84ce", "#fcd471", "#f0ed35", "#96d310", "#61c10b", "#439064", "#3d719a""#2e21ea", "#6324f5"]})], layout={'title':'INDIGO: In Categories'},
                        ),
                ),
            )
        elif value == 7:
            y = [colour_dates != 'Violet']
            zd = nd.ma.masked_array(category,y)
            zd=zd.tolist()
            a = zd.count('Political Unrest')
            b = zd.count('Terrorism')
            c = zd.count('War')
            d = zd.count('Natural disaster')
            e = zd.count('Technological Innovation')
            f = zd.count('Manmade disaster')
            g = zd.count('Transportation disaster')
            h = zd.count('Political agreement')
            i = zd.count('Financial crash')
            j = zd.count('Political change')
            return html.Div(dcc.Graph(
                figure=go.Figure(
                    data=[
                        go.Pie(values= [a, b, c, d, e, f, g, h, i, j],
                                direction= 'counterclockwise', 
                                labels= ['Political Unrest', 'Terrorism', 'War', 'Natural disaster', 'Technological Innovation', 'Manmade disaster', 'Transportation disaster', 'Political agreement', 'Financial crash', 'Political change'], 
                            sort= False, 
                            marker={'colors':["#ef55f1", "#fb84ce", "#fcd471", "#f0ed35", "#96d310", "#61c10b", "#439064", "#3d719a""#2e21ea", "#6324f5"]})], layout={'title':'VIOLET: In Categories'},
                        ),
                ),
            )
        else:
            return html.Div(dcc.Graph(
                figure=go.Figure(
                    data=[
                        go.Pie(values= [10, 4, 13, 14, 11, 13, 7],
                                direction= 'counterclockwise', 
                                labels= ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"], 
                                sort= False, 
                                marker={'colors':['red', 'orange',  '#fcd714', '#9ac432', '#61c8f3', 'indigo', 'violet']})], layout={'title':'ALL COLOURS'},
                    ),
                ),
            )
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
@app.callback(
              Output('date-container', 'children'),
              [Input('start_time', 'value'), Input('end_time', 'value')]
              )
def func(start_date, end_date):
    import itertools
    year,month,day = start_date.split('-')
    d6 = datetime.date(int(year),int(month),int(day))
    year,month,day = end_date.split('-')
    d7 = datetime.date(int(year),int(month),int(day))
    from datetime import date
    d0 = date(1980, 2, 26)
    delta3 = d6 - d0
    d8 = delta3.days
    delta4 = d7 - d0
    d9 = delta4.days
    d133 = d9 - d8
    
    ci = []
    for i in range(d9 + 1):
        ci.append(d6 + timedelta(i))

# data and y axis

    e = int(d8/1400)

    f = int(d9/1400)

    g = d8 % 1400
    h = d9 % 1400
    
    def func(g):
        if g == 0:
            g = 1400
        else:
            g = g
        return(g)
    
    g = (func(g))

    def func(h):
        if h == 0:
            h = 1400
        else:
            h = h
        return(h)
        
    h = (func(h))
    s = f - e
    def func(z1):
        if  e==f and g != 1400:
            e7 = z1[g:(h+1)]
            return(e7)
        elif e == f and g == 1400:
            i = z1 + z1
            j = h + 1400
            k = i[g:j+1]
            return(k)
        elif h !=1400 and g != 1400:
            gggg = 2
            if gggg == 2 and s==1:
                i = z1[g:]
                j = z1[:(h+1)]
                k = i + j
                return(k)
        elif g ==1400 and h != 1400:
            gggg = 3
            if gggg == 3 and s==1:
                i = z1*(s+1)
                j = z1[:(h+1)]
                k = (i + j)
                mo = d133 + 1400
                mm = k[g:mo+1]
                return(mm)
        elif g != 1400 and h ==1400:
            gggg = 4
            if gggg == 4 and s==1:
                i = z1[g:]
                return(i)
        elif g == 1400 and h ==1400:
            gggg = 6
            if gggg == 6 and s==1:
                i = z1+z1
                j = h + 1400
                k = i[g:(j+1)]
                return(k)
        elif h !=1400 and g != 1400:
            gggg = 24
            if gggg == 24 and s>=2:
                mo = s+1
                i = (z1*mo)
                k = i[g:(d133+1)]
                return(k)
        elif g ==1400 and h != 1400:
            gggg = 16
            if gggg == 16 and s>=2:
                i = z1*(s+2)
                j = h + (1400*(s+2))
                k = i[g:(j+1)]
                return(k)
        elif g !=1400 and h == 1400:
            gggg = 17
            if gggg == 17 and s>=2:
                i = z1*s
                j = i[g:]
                return(j)
        elif g ==1400 and h == 1400:
            gggg = 18
            if gggg == 18 and s>=2:
                i = z1*(s+1)
                j = i[g:]
                return(j)

    u=(func(z1))

#text

    b = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 6, 4, 7, 3, 8, 2, 9, 1,
     10, 9, 1, 8, 2, 7, 3, 6, 4, 5, 5, 4, 6, 3, 7, 2, 8, 1, 9]
    
    a8 = nd.array(['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'] * 38)
    a8 = a8.tolist()
    r = []
    for x, y in zip(a8, b):
        r.extend([x] * y)
    a9 = nd.array(['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'] * 38)
    a9 = np.roll(a9, -3, axis=0)
    a9 = a9.tolist()
    r1 = []
    for x, y in zip(a9, b):
        r1.extend([x] * y)
    k1 = r + r1
    a10 = nd.array(['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'] * 38)
    a10 = np.roll(a10, -6, axis=0)
    a10 = a10.tolist()
    r2 = []
    for x, y in zip(a10, b):
        r2.extend([x] * y)
    k2 = k1 + r2
    a11 = nd.array(['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'] * 38)
    a11 = np.roll(a11, -9, axis=0)
    a11 = a11.tolist()
    r3 = []
    for x, y in zip(a11, b):
        r3.extend([x] * y)
    k3 = k2 + r3
    a12 = nd.array(['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'] * 38)
    a12 = np.roll(a12, -12, axis=0)
    a12 = a12.tolist()
    r4 = []
    for x, y in zip(a12, b):
        r4.extend([x] * y)
    k4 = k3 + r4
    a13 = nd.array(['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'] * 38)
    a13 = np.roll(a13, -15, axis=0)
    a13 = a13.tolist()
    r5 = []
    for x, y in zip(a13, b):
        r5.extend([x] * y)
    k5 = k4 + r5
    a14 = nd.array(['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'] * 38)
    a14 = np.roll(a14, -18, axis=0)
    a14 = a14.tolist()
    r6 = []
    for x, y in zip(a14, b):
        r6.extend([x] * y)
    m = k5 + r6
    
    def func(m):
        if  e==f and g != 1400:
            n = m[g:(h+1)]
            return(n)
        elif e == f and g == 1400:
            n = m + m
            o = h + 1400
            p = n[g:(o+1)]
            return(p)
        elif h !=1400 and g != 1400:
            gggg = 2
            if gggg == 2 and s==1:
                n = m[g:]
                o = m[:(h+1)]
                p = n + o
                return(p)
        elif g ==1400 and h != 1400:
            gggg = 3
            if gggg == 3 and s==1:
                n = m + m
                o = m[:(h+1)]
                p = (n + o)
                v1 = p[g:(d133+1)]
                return(v1)
        elif g != 1400 and h ==1400:
            gggg = 4
            if gggg == 4 and s==1:
                n = m[g:]
                return(n)
        elif g == 1400 and h ==1400:
            gggg = 6
            if gggg == 6 and s==1:
                n = m+m
                o = h + 1400
                p = n[g:(o+1)]
                return(p)
        elif h !=1400 and g != 1400:
            gggg = 2
            if gggg == 2 and s>=2:
                me = s+1
                n = (m*me)
                p = n[g:(d133+1)]
                return(p)
        elif g ==1400 and h != 1400:
            gggg = 16
            if gggg == 16 and s>=2:
                n = m*(s+2)
                o = h + (1400*(s+2))
                p = n[g:(o+1)]
                return(p)
        elif g !=1400 and h == 1400:
            gggg = 17
            if gggg == 17 and s>=2:
                n = m*s
                o = n[g:]
                return(o)
        elif g ==1400 and h == 1400:
            gggg = 18
            if gggg == 18 and s>=2:
                n = m*(s+1)
                o = n[g:]
                return(o)

    e4=(func(m))

    return dcc.Graph(
        id='Rain-Cal-N15',
            figure={
                 'data': [
                          go.Scatter(
                                     x=ci,
                                     y=u[:],
                                     text= e4[:],
                                     mode='markers+lines',
                                     opacity=0.7,
                                     marker={
                                     'size': 13,
                                     'line': {'width': 1},
                                     'symbol': 'octagon',
                                     'autocolorscale': False,
                                     'cauto': False,
                                     'cmax': 7,
                                     'cmin': 1,
                                     'color': u[:],
                                     'colorscale': [[0, "#ff0000"], [0.142857142857143, "#ffae01"], [0.3333333333333, "#fff600"], [0.5555555555555, "#0aff04"], [0.6666666666666, "#0569ff"], [0.777777777777, "#a201ff"], [0.8888888888888, "#ff03ea"], [1.0000000, "#ff03ea"]],
                                     'colorsrc': "robotwax:157:00284a",
                                     'reversescale': False,
                                     'showscale': True,
                                     },
                                     ),
                          ],
                 'layout': go.Layout(
                                     {'title': 'RCC-14 Search Dates'},
                                     margin= {"t": 100},
                                     xaxis={'autorange': True, 'fixedrange': True, 'range': (d6, d7), 'showline': True, 'ticks': "inside", 'title': "time", 'type': "date"},
                                     yaxis={'autorange': False, 'fixedrange': False, 'range': [0.451383063814, 7.61242655506], 'title': "colours", 'type': "linear"},
                                     ),
                 },
    ),
  
@app.callback(dash.dependencies.Output('textbox-1', 'value'),
              [dash.dependencies.Input('slider', 'value'),
               dash.dependencies.Input('radio', 'value')])
def func(slider, radio_value):
    if slider==1 and radio_value == 'red':
        x = itertools.chain(One, Red)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==2 and radio_value=='red':
        x = itertools.chain(Two, Red)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==3 and radio_value=='red':
        x = itertools.chain(Three, Red)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==4 and radio_value=='red':
        x = itertools.chain(Four, Red)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==5 and radio_value=='red':
        x = Five + Red
        return(''.join(map(str, x)))
    elif slider==6 and radio_value=='red':
        x = itertools.chain(Six, Red)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==7 and radio_value=='red':
        x = itertools.chain(Seven, Red)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==8 and radio_value=='red':
        x = itertools.chain(Eight, Red)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==9 and radio_value=='red':
        x = itertools.chain(Nine, Red)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==10 and radio_value=='red':
        x = itertools.chain(Ten, Red)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==1 and radio_value == 'orange':
        x = itertools.chain(One, Orange)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==2 and radio_value=='orange':
        x = itertools.chain(Two, Orange)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==3 and radio_value=='orange':
        x = itertools.chain(Three, Orange)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==4 and radio_value=='orange':
        x = itertools.chain(Four, Orange)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==5 and radio_value=='orange':
        x = itertools.chain(Five, Orange)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==6 and radio_value=='orange':
        x = itertools.chain(Six, Orange)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==7 and radio_value=='orange':
        x = itertools.chain(Seven, Orange)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==8 and radio_value=='orange':
        x = itertools.chain(Eight, Orange)
        return(''.join(map(str, x)))
    elif slider==9 and radio_value=='orange':
        x = itertools.chain(Nine, Orange)
        return(''.join(map(str, x)))
    elif slider==10 and radio_value=='orange':
        x = itertools.chain(Ten, Orange)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==1 and radio_value == 'yellow':
        x = itertools.chain(One, Yellow)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==2 and radio_value=='yellow':
        x = itertools.chain(Two, Yellow)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==3 and radio_value=='yellow':
        x = itertools.chain(Three, Yellow)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==4 and radio_value=='yellow':
        x = itertools.chain(Four, Yellow)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==5 and radio_value=='yellow':
        x = itertools.chain(Five, Yellow)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==6 and radio_value=='yellow':
        x = itertools.chain(Six, Yellow)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==7 and radio_value=='yellow':
        x = itertools.chain(Seven, Yellow)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==8 and radio_value=='yellow':
        x = itertools.chain(Eight, Yellow)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==9 and radio_value=='yellow':
        x = itertools.chain(Nine, Yellow)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==10 and radio_value=='yellow':
        x = itertools.chain(Ten, Yellow)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==1 and radio_value == 'green':
        x = itertools.chain(One, Green)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==2 and radio_value=='green':
        x = itertools.chain(Two, Green)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==3 and radio_value=='green':
        x = itertools.chain(Three, Green)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==4 and radio_value=='green':
        x = itertools.chain(Four, Green)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==5 and radio_value=='green':
        x = itertools.chain(Five, Green)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==6 and radio_value=='green':
        x = itertools.chain(Six, Green)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==7 and radio_value=='green':
        x = itertools.chain(Seven, Green)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==8 and radio_value=='green':
        x = itertools.chain(Eight, Green)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==9 and radio_value=='green':
        x = itertools.chain(Nine, Green)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==10 and radio_value=='green':
        x = itertools.chain(Ten, Green)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==1 and radio_value == 'blue':
        x = itertools.chain(One, Blue)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==2 and radio_value=='blue':
        x = itertools.chain(Two, Blue)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==3 and radio_value=='blue':
        x = itertools.chain(Three, Blue)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==4 and radio_value=='blue':
        x = itertools.chain(Four, Blue)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==5 and radio_value=='blue':
        x = itertools.chain(Five, Blue)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==6 and radio_value=='blue':
        x = itertools.chain(Six, Blue)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==7 and radio_value=='blue':
        x = itertools.chain(Seven, Blue)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==8 and radio_value=='blue':
        x = itertools.chain(Eight, Blue)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==9 and radio_value=='blue':
        x = itertools.chain(Nine, Blue)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==10 and radio_value=='blue':
        x = itertools.chain(Ten, Blue)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==1 and radio_value == 'ind':
        x = itertools.chain(One, Indigo)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==2 and radio_value=='ind':
        x = itertools.chain(Two, Indigo)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==3 and radio_value=='ind':
        x = itertools.chain(Three, Indigo)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==4 and radio_value=='ind':
        x = itertools.chain(Four, Indigo)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==5 and radio_value=='ind':
        x = itertools.chain(Five, Indigo)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==6 and radio_value=='ind':
        x = itertools.chain(Six, Indigo)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==7 and radio_value=='ind':
        x = itertools.chain(Seven, Indigo)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==8 and radio_value=='ind':
        x = itertools.chain(Eight, Indigo)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==9 and radio_value=='ind':
        x = itertools.chain(Nine, Indigo)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==10 and radio_value=='ind':
        x = itertools.chain(Ten, Indigo)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==1 and radio_value == 'vio':
        x = itertools.chain(One, Violet)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==2 and radio_value=='vio':
        x = itertools.chain(Two, Violet)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==3 and radio_value=='vio':
        x = itertools.chain(Three, Violet)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==4 and radio_value=='vio':
        x = itertools.chain(Four, Violet)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==5 and radio_value=='vio':
        x = itertools.chain(Five, Violet)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==6 and radio_value=='vio':
        x = itertools.chain(Six, Violet)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==7 and radio_value=='vio':
        x = itertools.chain(Seven, Violet)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==8 and radio_value=='vio':
        x = itertools.chain(Eight, Violet)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==9 and radio_value=='vio':
        x = itertools.chain(Nine, Violet)
        x = list(x)
        return(''.join(map(str, x)))
    elif slider==10 and radio_value=='vio':
        x = itertools.chain(Ten, Violet)
        x = list(x)
        return(''.join(map(str, x)))



if __name__ == '__main__':
    app.run_server(debug=True)

