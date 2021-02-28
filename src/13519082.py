#NIM/Nama: 13519082/Jeanne D'Arc Amara Hanieka
#Tucil 2 Strategi Algoritma

arraymatkulawal = []
arrakhir = []

def membacaFile(namafile):
    global daftarmatkulawal
    bukafile = open('../test/'+namafile+'.txt', "r")
    baris = bukafile.read().splitlines() #taro ke array
    bukafile.close()

    jumlah = len(baris) #panjang baris
    for i in range(jumlah):
        baris[i] = baris[i].replace('.', '') #ngilangin .
        baris[i] = baris[i].replace(',', '') #ngilangin ,
    arraybersih = [None]*len(baris) #define array baru sepanjang array sblomnya
    for i in range(0, len(baris)):    
        arraybersih[i] = baris[i]; #dipindahin ke array baru biar tidak bingung

    banyakbaris = len(arraybersih)
    daftarmatkulawal = [None]*(len(arraybersih)) #define array baru sepanjang array sblomnya    
    for i in range(banyakbaris):
        for j in range(len(arraybersih[i])):
            daftarmatkulawal[i] = arraybersih[i].split(" ")
    return daftarmatkulawal

def hapus(a, b):
    for i in range(len(daftarmatkulawal[a])):
        if daftarmatkulawal[a][i-1] == b:
            del daftarmatkulawal[a][i-1]

def prosesPemilihan(banyakmatkulawal):
    z = 0
    while z < banyakmatkulawal:
        list_temp = []
        for i in range(len(daftarmatkulawal)):
            if len(daftarmatkulawal[i]) == 1:
                choose_temp = daftarmatkulawal[i][0]
                list_temp.append(choose_temp)
                z += 1
        arrakhir.append(list_temp)
        for j in range(len(list_temp)):
            for k in range(len(daftarmatkulawal)):
                hapus(k, list_temp[j])
        list_temp = []

def printHasil(arrayakhir):
    for semester in range (len(arrayakhir)):
        print("Semester", semester+1 ,": ",end = '')
        banyakpersemester = len(arrayakhir[semester])   
        for matkul in range(len(arrayakhir[semester])):
            if (banyakpersemester==1):
                print(arrayakhir[semester][matkul],end = '')
            else:
                print(arrayakhir[semester][matkul]+ ", ", end = '')
                banyakpersemester-=1
        print(end='\n')    

print("\n")
print("""
██╗     ██╗   ██╗██╗     ██╗   ██╗███████╗
██║     ██║   ██║██║     ██║   ██║██╔════╝
██║     ██║   ██║██║     ██║   ██║███████╗
██║     ██║   ██║██║     ██║   ██║╚════██║
███████╗╚██████╔╝███████╗╚██████╔╝███████║
╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝
 
 T E N T U K A N  M A T K U L  A N D A !
""")

#baca filenya
bacanamafile = input("Masukkan nama file (cukup tuliskan nama file tanpa extension): ")
print("\n")
membacaFile(bacanamafile)

#masukin yang awal biar safe yuhu, yang di utak atik yang daftar matkul awal
arraymatkulawal = daftarmatkulawal.copy()

#prosesnya
prosesPemilihan(len(arraymatkulawal))

#ngeprintnya
printHasil(arrakhir)

print("\n")