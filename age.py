import pygal

ruler_name = '''Hong Xiuquan
Mao Zedong
Adolf Hitler
Chiang Kai-Shek
Joseph Stalin
Hirohito
Leopold II of Belgium
Ranavalona I
Pol Pot
Omar al-Bashir (Alive)
Suharto
Mengistu Haile Mariam
Ho Chi Minhand the Viet Cong
Benito Mussolini
Saddam Hussein
Francisco Franco
Idi Amin
Josip Broz Tito
Ivan the Terrible
Siad Barre'''.split("\n")


ruler_age = '''50
82
56
87
74
87
74
83
72
75
86
82
79
61
69
82
78
87
53
75'''.split("\n")

average_life = '''74.6
74.6
78.7
74.6
64.7
80.5
78.6
63.9
66.6
62.4'''.split('\n')

average_life = list(map(float, average_life))

ruler_age = list(map(int, ruler_age))

bar = pygal.Bar(x_label_rotation=90)

bar.add("Current (2019) Average life expectancy of Male of similar geogloical location", average_life)
bar.add("Death age of top 10 Rulers with highest death count", ruler_age[:10])
bar.x_labels = ruler_name[:10]
bar.y_labels = range(0,110, 10)

bar.render_to_file("rule age.svg")