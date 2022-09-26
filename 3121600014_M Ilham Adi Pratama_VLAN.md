**LAPORAN PRAKTIKUM KONSEP JARINGAN**

| Nama | Muhammad Ilham Adi Pratama |
|:----:|:--------------------------:| 
|Kelas | 2 D4 IT A                  |
| NRP  | 3121600014                 |

**TUGAS VLAN**

**Pengertian Vlan**

VLAN adalah singkatan dari Virtual Local Area Network, guna menghindari
keterbatasan fisik LAN melalui sifat yang dimilikinya, memungkinkan
skala jaringan dan segmentasi guna meningkatkan langkah-langkah keamanan
dan mengurangi adanya latensi jaringan. VLAN adalah subnetwork yang
dapat mengelompokkan kumpulan perangkat pada jaringan area lokal fisik
(LAN) yang terpisah.

**Fungsi VLAN**

Fungsi Virtual Local Area Network atau VLAN adalah mengakomodir
konfigurasi pada jaringan komputer fisik menjadi beberapa domain siaran.

Meski memiliki domain siaran berbeda, jalur yang dihasilkan oleh VLAN
tersebut masih melewati perangkat penghubung yang sama. Biasanya
dikonfigurasikan dengan mikrotik atau cisco.

**Cara kerja VLAN**

Berikut adalah setail langkah demi langkah tentang cara kerja Virtual
Local Area Network : 

1.  Virtual Local Area Network dalam jaringan diidentifikasi dengan
    nomor

2.  Rentang yang valid adalah 1-4094. Pada saklar Virtual Local Area
    Network, anda menetapkan port dengan nomor Virtual Local Area
    Network yang tepat 

3.  Saklar kemudian memungkinkan data yang perlu dikirim antara berbagai
    port yang memiliki Virtual Local Area Network yang sama 

4.  Karena hampir semua jaringan lebih besar dari satu saklar, harus ada
    cara untuk mengirim lalu lintas antara dua saklar

5.  Salah satu cara sederhana dan mudah untuk melakukannya adalah dengan
    menetapkan port pada setiap switch jaringan. Dengan Virtual Local
    Area Network dan menjalankan kabel antara keduanya. 

**TUGAS PRAKTIKUM**
Topologi yang saya gunakan adalah sebagi berikut Topologi tersebut terdiri dari 1 router, 1 switch, dan 3 pc-client dengan 2 VLAN (172.17.10.1 - 10  & 192.168.30.1 - 30 ) dan 1 Non-VLAN (192.168.1.1).

[![image.png](https://i.postimg.cc/0QjC0pwj/image.png)](https://postimg.cc/47CtJHwR)

**Configuration IP (PC)**

[![image.png](https://i.postimg.cc/bYTtwGDF/image.png)](https://postimg.cc/RqWFPZTc)

PC 0: IP GATEWAY -> 172.17.10.2 Subnet Mask -> 255.255.0.0 (IP VLAN Route 10) PC 1: IP GATEWAY -> 192.168.30.3 Subnet Mask -> 255.255.255.0 (IP VLAN Route 30) PC 2: IP GATEWAY -> 192.168.1.3 Subnet Mask -> 255.255.255.0 (IP NON VLAN Router)


**Configuration IP (Router)**

[![image.png](https://i.postimg.cc/MTYNL0PS/image.png)](https://postimg.cc/zbVxbhYt)

Router 0 : Interface Fa0/0 -> 192.168.1.1 (Configuration Non-VLAN IP)

**Conifguration VLAN Database (Switch)**

[![image.png](https://i.postimg.cc/Y066PKx2/image.png)](https://postimg.cc/gL0Lw751)

Switch 0 ada 2 VLAN yang akan di gunakan yaitu VLAN Nomer [10]  VLAN Nommer [30]

**Configuration VLAN Database (Router)**

[![image.png](https://i.postimg.cc/Nf7h6KmS/image.png)](https://postimg.cc/LnX0R6y3)

Router 0 : VLAN -> VLAN Number [10] -> VLAN Number [30]


**Configuration IP VLAN (Router)**

[![12.png](https://i.postimg.cc/VvLFvw44/12.png)](https://postimg.cc/CBX8rW3f)

Router 0 : Interface Fa0/0.10 -> 172.17.10.2 untuk VLAN 10 ,Interface Fa0/1.30 -> 192.168.30.3 (Configuration VLAN 30 )

**Test Ping To Other VLAN And Non-VLAN**

[![image.png](https://i.postimg.cc/8cwzntxf/image.png)](https://postimg.cc/8fJG7BpT)

Ping di atas berasal dari PC0 172.17.10.1 - 172.17.10.2 (VLAN 10) berhasil melakukan ping pada IP PC1 192.168.30.1 - 192.168.30.3 (VLAN 30) yang dimana kedua IP tersebut berbeda network dan subnetting tanpa bantuan routing static karena pada Router 0 mereka terkoneksi secara Directly Connected dan bukan Remote Network.

Sehingga tidak diperlukan routing static atau semacamnya, VLAN seakaan terdapat 2 kabel pada router dengan IP yang berbeda. Dengan menambahkan IP pada virtual dengan imbuhan [.number] pada interfaces yang terkoneksi pada router secara nyata.