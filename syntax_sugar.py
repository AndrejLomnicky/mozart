import math
# komprehensie
#uloha cislo 1
cisla = [x**2 for x in range(1,10)]
#uloha cislo 2
zoznam = [1,2,3,4,5,6,7,8,9,10]
parne = [x for x in zoznam if x % 2 == 0]
#uloha cislo 3
ovocie = ["jablko", "hruška", "slivka", "mango"]
v_ovocie = [ovocie.upper() for ovocie in ovocie]
#dlhe úlohy
kom1 = [i for i in range(1,51) if i % 3 ==0 or i % 5 ==0]

kom2 = [a + b + c for a in "ABC" for b in "2468" for c in "/+-"]

kom3 = [rok for rok in range(1000, 2001) if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0]

str4 = "Veľký čínsky múr je teda šesťkrát dlhší ako vzdialenosť medzi východným a západným americkým pobrežím"
slova = str4.split()
kom4 = [(slovo.upper(), slovo.lower(), len(slovo)) for slovo in slova] #robim trojice

vec = [-4, -2, 0, 2, 4]
kom_5_1 = [x * 2 for x in vec]
kom_5_2 = [x for x in vec if x > 0]
kom_5_3 = [abs(x) for x in vec]

fruit = ['  banana', '  loganberry ', 'passion fruit  ']
kom6 = [x.strip() for x in fruit]

kom7 = [(x, x ** 2) for x in range(0,5)]

kom8 = [(x, math.sin(math.radians(x)), math.cos(math.radians(x))) for x in range(0, 181, 10)]










