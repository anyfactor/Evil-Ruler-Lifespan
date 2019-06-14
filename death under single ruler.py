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
Omar al-Bashir
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

rule_death = '''31_622_777
30851094
18564944
10511124
7035624
6480741
6244998
2500000
2171381
1639936
906658
670820
396401
314998
250000
227321
223607
219363
124900
100000'''.split('\n')

rule_death = list(map(int, rule_death))

bar = pygal.Bar(x_label_rotation=90)

bar.add("Deaths under Single Ruler", rule_death[:10])
bar.x_labels = ruler_name[:10]

bar.render_to_file("rule death.svg")