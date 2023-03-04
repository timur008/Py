class Country:
    name = None
    language = None
    life_quality = 0
class President(Country):
    name = None
    rep = 0
class Region(Country):
    dialect = None
    name = None
    life_quality = 0
class Mayor(Region):
    name = None
    rep = 0

Ukraine = Country()
Donetsk = Region()
Ukraine.name = "Ukraine"
Ukraine.language = "Ukrainian"
Ukraine.life_quality = 111
Donetsk.life_quality = 3
Donetsk.name = "Donetsk region"
print(Ukraine.name)
print(Ukraine.language)
print(Ukraine.life_quality, "out of 200")
print(Donetsk.life_quality, "out of 5")
print(Donetsk.name)