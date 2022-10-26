**LAPORAN PRAKTIKUM KONSEP JARINGAN**

| Nama | Muhammad Ilham Adi Pratama |
|:----:|:--------------------------:|
|Kelas | 2 D4 IT A                  |
| NRP  | 3121600014                 |

# ROUTING DYNAMIC


**APA ITU Dynamic Routing**

Dynamic routing adalah suatu metode routing yang memungkinkan router untuk mengetahui rute ke suatu jaringan tanpa harus dikonfigurasi secara manual. Dynamic routing menggunakan routing protocol untuk menentukan rute ke suatu jaringan. Routing protocol yang digunakan dalam percobaan kali ini adalah RIP (Routing Information Protocol). Cara Kerja Dynamic Routing adalah sebagai berikut:

1. Router mengirimkan routing table ke semua router yang terhubung pada jaringan.
2. Router yang menerima routing table akan melakukan update routing table sesuai dengan routing table yang diterima.
3. Setelah update routing table, router akan mengirimkan routing table yang sudah diupdate ke semua router yang terhubung pada jaringan.
4. Langkah 2 dan 3 akan terus berulang sampai semua router pada jaringan memiliki routing table yang sama.



**APA ITU Routing Information Protocol (RIP)**

RIP adalah suatu routing protocol yang digunakan untuk melakukan routing pada jaringan IP. RIP menggunakan metode distance vector untuk menentukan rute ke suatu jaringan.

Metode distance vector ini adalah metode routing yang menggunakan vektor jarak untuk menentukan rute ke suatu jaringan. Vektor jarak ini merupakan jarak dari router ke suatu jaringan. Vektor jarak ini disebut dengan hop count. Hop count adalah jumlah router yang dilewati untuk menuju suatu jaringan.

**BAGAIMANA CARA KERJA RIP**
Host mendengar pada alamat broadcast jika ada update routing dari gateway. Host akan memeriksa terlebih dahulu routing table lokal jika menerima update routing . Jika rute belum ada, informasi segera dimasukkan ke routing table.

# PRAKTIKUM TRACE ROUTE dan TTL

**TOPOLOGI YANG DIGUNAKAN**

[![image.png](https://i.postimg.cc/m2vkD7cH/image.png)](https://postimg.cc/vcvb2gtY)

Pada topologi diatas masih menggunakan topologi yang lama dimana terdiri dari 3 buah router, 2 buah PC, dan 2 buah switch. Jenis router yang digunakan adalah Router-PT yang dimodifikasi portnya sesuai kebutuhan.

**Konfigurasi IP Route**

[![image.png](https://i.postimg.cc/3NyLtsFW/image.png)](https://postimg.cc/tnjtTmfH)

Kita konfigurasi IP untuk Interface masing masing Route, pada gambar diatas kita set IP untuk Interface Fa0/0 pada Router0 dengan IP 192.168.3.1

*langkah langkah konfigurasi IP Route*
1. Pergi ke config
2. Pilih Interface yang ingin di setel IP nya
3. Masukkan IP untuk Interface tadi
4. Masukkan Subnet Mask untuk Interface tadi

|  Devices 	| Interface 	|      IP     	|
|:--------:	|:---------:	|:-----------:	|
| Router 0 	|   Fa0/0   	| 192.168.3.1 	|
|          	|   Fa1/0   	| 192.168.2.1 	|
|          	|   Fa6/0   	| 192.168.4.1 	|
| Router 1 	|   Fa0/0   	| 192.168.3.2 	|
|          	|   Fa1/0   	| 192.168.1.1 	|
|           |   Fa6/0   	| 192.168.5.1   |
| Router 2 	|   Fa0/0   	| 192.168.2.2 	|
|          	|   Fa1/0   	| 192.168.1.2 	|

**Konfigurasi IP PC**

[![image.png](https://i.postimg.cc/7ZwZTBQ7/image.png)](https://postimg.cc/0bXsTCv2)

Kita konfigurasikan untuk IP pada masing masing PC, dengan kasus diatas kita set untuk IP untuk PC0 dengan 192.168.4.2

*langkah langkah konfigurasi IP*
1. Pergi ke dekstop 
2. Pilih IP Configuration
3. Masukkan IP = 192.168.4.2
4. Subnet Mask = 255.255.255.0 
5. Default Gateway = 192.168.4.1

|  Devices 	|  Subnet Mask  |      IP     	|Default Gateway|
|:--------:	|:------------:	|:-----------:	|:-----------:	|
|    PC0   	| 255.255.255.0 | 192.168.4.2 	| 192.168.4.1 	|
|    PC1   	| 255.255.255.0 | 192.168.5.2 	| 192.168.5.1 	|

**Konfigurasi Routing Dengan RIP**

[![image.png](https://i.postimg.cc/VLcY3GwT/image.png)](https://postimg.cc/qgjVKGzX)

Kita konfigurasikan untuk RIP pada masing masing Route, pada gambar diatas kita set RIP untuk Route 0 dengan 
1. 192.168.2.0 
2. 192.168.3.0 
3. 192.168.4.0
tetapi dikarenakan kita mencoba dulu untuk jalur atas maka kita tambahkan 192.168.3.0 dan 192.168.4.0

*langkah langkah konfigurasi RIP pada Route*
1. Pergi ke config
2. Pilih RIP
3. Masukkan Network ID
4. Pilih add

|  Devices 	| Destination Network 	
|:--------:	|:-------------------:		
| Router 0 	|     192.168.2.0     	
|          	|     192.168.3.0     
|          	|     192.168.4.0     
| Router 1 	|     192.168.1.0     
|          	|     192.168.3.0     
|          	|     192.168.5.0     
| Router 2 	|     192.168.1.0     
|          	|     192.168.2.0  

Dalam konfigurasi Dynamic routing diatas dengan RIP, dapat dilakukan dengan cara memasukkan perintah pada CLI. 

        Router(config)#router rip
        Router(config-router)#network 192.168.1.0
        Router(config-router)#network 192.168.2.0

**Convergent Dan Test**
[![image.png](https://i.postimg.cc/qvRWYyNS/image.png)](https://postimg.cc/QH26KBkJ)

Konvergensi adalah keadaan satu set router yang memiliki informasi topologi yang sama tentang internetwork di mana mereka beroperasi. Untuk satu set router telah konvergen , mereka harus telah mengumpulkan semua informasi topologi yang tersedia dari satu sama lain melalui protokol routing yang diimplementasikan , informasi yang mereka kumpulkan tidak boleh bertentangan dengan informasi topologi router lain di set, dan itu harus mencerminkan keadaan sebenarnya dari jaringan. Dengan kata lain: dalam jaringan konvergensi semua router "setuju" seperti apa topologi jaringan itu.

Konvergensi merupakan gagasan penting untuk satu set router yang terlibat dalam routing dinamis . Semua Protokol Gateway Interior mengandalkan konvergensi agar berfungsi dengan baik. Untuk konvergen itu adalah keadaan normal dari sistem otonom operasional . Exterior Gateway Routing Protocol BGP biasanya tidak pernah konvergen karena Internet terlalu besar untuk perubahan yang dapat dikomunikasikan dengan cukup cepat.

Terlihat pada percobaan di atas bahwa paket yang dikirimkan dari PC0 ke PC1 adalah sebagai berikut:

1. PC0 mengirimkan paket ke router 0.
2. Router 0 menerima paket dan mengirimkan paket ke router 1.
3. Router 1 menerima paket dan mengirimkan paket ke PC1.
4. PC1 menerima paket.

Tracert di atas ialah percobaan yang pertama kali jadi belum ada routing table yang ada di router 1. Routing table akan terupdate setelah router 1 menerima routing table dari router 0. Terdapat jeda waktu disana karena routing table belum terupdate maka dari itu sistem convergent di mulai pada saat routing table masih belum terbentuk.
