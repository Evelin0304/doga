kliensek=[]
with open('kliensek.txt','r',encoding='utf-8') as forras \
    open('kliensek_adat.txt','w',encoding='utf-8') as cel:
    fejlec=forras.readline()
    for sor in forras:
        adat=sor.strip().split(',')
        kliens={'server': adat[0], 'cm':adat[1],'Admin':adat[2],'Pc':adat[3],'gigabit':adat[4],}
        kliensek.append(kliens)
        print(kliens,file=cel)
print(f'{kliensek}')