#NIM/Nama: 13519082/Jeanne D'Arc Amara Hanieka
#Tucil 2 Strategi Algoritma

#inisiasi array global
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
    return daftarmatkulawal #hasil akhirnya dimasukin sini

def hapus(a, b): #untuk menghapus isi elemen array (dengan indeks a) jika nilainya sama dengan b
    for i in range(len(daftarmatkulawal[a])):
        if daftarmatkulawal[a][i-1] == b:
            del daftarmatkulawal[a][i-1] #ini bagian menghapusnya, pake del

def prosesPemilihan(banyakmatkulawal): #ini untuk proses ngurutin dan masukin ke array hasil akhir
    z = 0
    while z < banyakmatkulawal:
        list_temp = [] #untuk tempat nyimpen sementara, setiap pengulangan ke reset (kan kalo dah ilang, yaudah cari korban baru)
        for i in range(len(daftarmatkulawal)):
            if len(daftarmatkulawal[i]) == 1: #kalo misalnya suatu matkul tidak punya prasyarat/prasyarat sudah terpenuhi semua, panjangnya cuma 1
                choose_temp = daftarmatkulawal[i][0] #maka, hasilnya dimasukkin ke arr lain buat di simpen
                list_temp.append(choose_temp) #dimasukin ke tempat nyimpen sementara tadi
                z += 1
        arrakhir.append(list_temp) #nilai yang di tempat sementara tadi (matkul-matkul yg gapunya prereq) dimasukkin ke arr akhir
        for j in range(len(list_temp)):
            for k in range(len(daftarmatkulawal)):
                hapus(k, list_temp[j]) #menghapus kalo ada matkul yang sama di matkul lain (kalo si matkul yang di list_temp jadi prereq, dihapus di tempat lain itu)

def printHasil(arrayakhir): #untuk ngeprint, intinya
    for semester in range (len(arrayakhir)):
        print("Semester", semester+1 ,": ",end = '') #munculin semester, pake 1 2 3 saja karena romawi susah :(
        banyakpersemester = len(arrayakhir[semester])   
        for matkul in range(len(arrayakhir[semester])):
            if (banyakpersemester==1):
                print(arrayakhir[semester][matkul],end = '') #kalo udah terakhir, ngeprintnya gapake koma
            else:
                print(arrayakhir[semester][matkul]+ ", ", end = '') #kalo belom, ngeprintnya pake koma
                banyakpersemester-=1
        print(end='\n')    


#MAIN
#nama programnya "Lulus" karena orang ngambil matkul biar lulus dan saya pengen lulus matkul ini dan lulus kuliah juga :D
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
#jadi karena ada prosedur yang pake banyak nilai awal terus"an meskipun daftarmatkulawal berkurang, makanya di copy dulu ke array baru (yang bukan assignment)
arraymatkulawal = daftarmatkulawal.copy()

#prosesnya
prosesPemilihan(len(arraymatkulawal))

#ngeprintnya
printHasil(arrakhir)

print("\n")