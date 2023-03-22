# Kişinin adı,kilo ve boy bilgilerini alıp kilo indekslerini hesaplamak
#0-19.0=>Zayıf
#19.0-24.9=>Normal
#25.0-29.9=>Kilolu
#29.9-35.0=>Obez
name=input("ad-soyad:")
kg=float(input("kilonuz:"))
hg=float(input("boyunuz:"))
index=(kg)/(hg**2)
zayif=(index>=0)and(index<=19.0)
normal=(index>=19.0)and(index<=24.9)
kilolu=(index>=25.0)and(index<=29.9)
obez=(index>=29.9)and(index<=35.0)
print(f"{name} kilo indeksin:{index} ve kilo değerlendirmen zayıf :{zayif}")
print(f"{name} kilo indeksin:{index} ve kilo değerlendirmen normal:{normal}")
print(f"{name} kilo indeksin:{index} ve kilo değerlendirmen kilolu:{kilolu}")
print(f"{name} kilo indeksin:{index} ve kilo değerlendirmen obez:{obez}")
