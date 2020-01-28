[![WTFPL](http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-4.png)](http://www.wtfpl.net/)

---

<div style="text-align:center;"><img src="https://vignette1.wikia.nocookie.net/warhammer40k/images/2/29/Aquila.jpg"/></div>

---

# Imperial Dating System converter

Based on the information from the [Wiki](https://warhammer40k.fandom.com/wiki/Imperial_Dating_System).

## Usage

Creating an instance of the object with no parameters will convert the current date (at the moment).
```
from pydate40k.Date40k import Date40k

d = Date40k()
print(d)
>>> 944 019.M3
```

Using a date string with the [format](https://www.tutorialspoint.com/python/time_strptime.htm) `"%Y-%m-%d %H:%M:%S"` will convert that date, on any invalid format, the current date will be returned instead.
```
from pydate40k.Date40k import Date40k

d = Date40k("1999-05-11 13:00:00")
print(d)
>>> 360 999.M2
```

---

*GW, Games Workshop, Citadel, Black Library, Forge World, Warhammer, the Twin-tailed Comet logo, Warhammer 40,000, the ‘Aquila’ Double-headed Eagle logo, Space Marine, 40K, 40,000, Warhammer Age of Sigmar, Battletome, Stormcast Eternals, White Dwarf, Blood Bowl, Necromunda, Space Hulk, Battlefleet Gothic, Dreadfleet, Mordheim, Inquisitor, Warmaster, Epic, Gorkamorka, and all associated logos, illustrations, images, names, creatures, races, vehicles, locations, weapons, characters, and the distinctive likenesses thereof, are either ® or TM, and/or © Games Workshop Limited, variably registered around the world. All Rights Reserved.*
