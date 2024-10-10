halozat=[]
with open('halozat.txt','r',encoding='utf-8') as forras \
    open('halozat.txt','w',encoding='utf-8') as cel:
    fejlec=forras.readline()
    for sor in forras:
        adat=sor.strip().split(',')
        halo={'admin': adat[1], 'pt controller':adat[1],'SWR':adat[3],'SWL':adat[2],'PC':adat[4], 'server':adat[1]}
        halozat.append(admin)
        print(halo,file=cel)
print(f'{halozat}')
