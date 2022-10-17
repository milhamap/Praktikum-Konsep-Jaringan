**LAPORAN PRAKTIKUM KONSEP JARINGAN**

| Nama | Muhammad Ilham Adi Pratama |
|:----:|:--------------------------:|
|Kelas | 2 D4 IT A                  |
| NRP  | 3121600014                 |

# Traceroute And Time To Live


**APA ITU TRACEROUTE**

Traceroute adalah perintah untuk menunjukkan rute yang dilewati paket untuk mencapai tujuan. Ini dilakukan dengan mengirim pesan Internet Control Message Protocol Echo Request Ke tujuan dengan nilai Time to Live yang semakin meningkat. Dalam operasi sistem Windows, traceroute ini dikenal sebagai tracert.

Pembacaan traceroute biasanya akan menampilkan tiga kolom terpisah untuk waktu hop, kaarena setiap traceroute mengirimkan tiga informasi terpisah ke setiap komputer. Di bagian paling atas daftar, traceroute akan memberikan batas berapa banyak garis hop yang akan ditampilkan. Umumnya, jumlah maksimal berkisar di angka 30 hop.

Saat traceroute mengalami kesulitan mengakses komputer, akan tampil pesan “Request timed out”. Setiap kolom hop akan menampilkan tanda bintang, bukan milidetik.

**BAGAIMANA CARA KERJA TRACEROUTE**

Setelah memberikan perintah traceroute, utilitas akan memulai pengiriman paket menggunakan Internet Control Message Protocol (ICMP), termasuk Time to Live (TTL) yang dirancang untuk dilampaui oleh router pertama yang menerimanya. ICMP dan TTL ini akan mengembalikan pesan Time Exceed. Hal ini memungkinkan traceroute menentukan waktu yang diperlukan untuk ke hop router pertama. Meningkatkan time limit, mengirimkan ulang paket sehingga akan mencapai paket router kedua di jalur tujuan, yang mengembalikan pesan time exceeded lainnya, dan sebagainya.

Traceroute menentukan kapan paket telah mencapai tujuan dengan memasukkaan nomor port yang berada di luar jumlah normal. Ketika diterima, pesan “Port Unreachable akan dikembalikan. Ini memungkinkan traceroute untuk mengukur panjang waktu hop terakhir.

**APA ITU TIME TO LIVE (TTL)**

Time to live atau hop limit adalah mekanisme yang membatasi umur atau lifetime data dalam komputer atau jaringan. Nilai TTL menentukan paket harus diteruskan ke router selajutnya (next hop router) atau di-discard. Nilai default TTL adalah 64 maksimum 255 (8bits) dan nilainya akan berkurang 1 setiap paket data melewati router (layer 3), beberapa saat sebelum forwarded decision dan router tidak akan melewatkan traffik ke route selanjutknya apabila TTL yang dia terima bernilai 1

**BAGAIMANA CARA KERJA TIME TO LIVE (TTL)**
Istilah TTL sering kita jumpai pada saat kita melakukan "ping" pada suatu jaringan komputer.

[![ping.png](https://i.postimg.cc/bdc1wPGx/ping.png)](https://postimg.cc/rRjDfvNs)

Nilai TTL ini menunjukkan berapa lama paket data tersebut bisa beredar dalam suatu jaringan. Ketika suatu packet data melewati router maka nilai TTL yang diterima akan berkurang 1 dan pada standart nya nilai TTL pada windows adalah 128.

[![ttl.webp](https://i.postimg.cc/SxG13T5T/ttl.webp)](https://postimg.cc/5X6mF3fL)

Jika nilai TTL sudah mencapai 0, maka packet data tersebut akan di discard oleh router.
# PRAKTIKUM TRACE ROUTE dan TTL

**TOPOLOGI YANG DIGUNAKAN**

[![image.png](https://i.postimg.cc/QxjmjzV6/image.png)](https://postimg.cc/grB8DNVR)

Topologi diatas terdiri dari 3 buah router, 2 buah PC, dan 2 buah switch. Jenis router yang digunakan adalah Router-PT yang dimodifikasi portnya sesuai kebutuhan.

**Konfigurasi IP Route**

[![image.png](https://i.postimg.cc/zvzx22gP/image.png)](https://postimg.cc/HcN0V23Q)

|  Devices 	| Interface 	|      IP     	|
|:--------:	|:---------:	|:-----------:	|
| Router 0 	|   Fa0/0   	| 192.168.2.2 	|
|          	|   Fa1/0   	| 192.168.1.2 	|
| Router 1 	|   Fa0/0   	| 192.168.1.1 	|
|          	|   Fa1/0   	| 192.168.3.2 	|
|           |   Fa6/0   	| 192.168.5.1   |
| Router 2 	|   Fa0/0   	| 192.168.2.1 	|
|          	|   Fa1/0   	| 192.168.3.1 	|
|           |   Fa6/0   	| 192.168.4.1   |

**Konfigurasi IP PC**

[![image.png](https://i.postimg.cc/B6spt7MQ/image.png)](https://postimg.cc/2qchKwsP)

|  Devices 	| Interface 	|      IP     	|
|:--------:	|:---------:	|:-----------:	|
|    PC0   	|   Fa0/0   	| 192.168.4.2 	|
|    PC1   	|   Fa0/0   	| 192.168.5.2 	|

**Konfigurasi Static Routing Pada Komputer**

[![image.png](https://i.postimg.cc/cLBM2Bdp/image.png)](https://postimg.cc/ZW0dy3BH)

|  Devices 	| Destination Network 	|    Netmask    	|     Via     	|    Metric    	|
|:--------:	|:-------------------:	|:-------------:	|:-----------:	|:------------:	|
| Router 0 	|     192.168.4.0     	| 255.255.255.0 	| 192.168.2.1 	| 10 (Default) 	|
|          	|     192.168.5.0     	| 255.255.255.0 	| 192.168.1.1 	| 10 (Default) 	|
| Router 1 	|     192.168.4.0     	| 255.255.255.0 	| 192.168.3.1 	| 10 (Default) 	|
|          	|     192.168.2.0     	| 255.255.255.0 	| 192.168.1.2 	| 10 (Default) 	|
| Router 2 	|     192.168.5.0     	| 255.255.255.0 	| 192.168.3.2 	| 10 (Default) 	|
|          	|     192.168.1.0     	| 255.255.255.0 	| 192.168.2.2 	| 10 (Default) 	|


Dalam konfigurasi static routing diatas, dapat dilakukan dengan cara memasukkan perintah pada CLI. Struktur perintah untuk memberikan konfigurasi di atas sebagai berikut, "ip route [destination network] [netmask] [via] [metric]".

**Percobaan TracerRoute**
Perintah untuk melakukan traceroute atau tracert adalah sebagai berikut.

1. Windows : "tracert [IP Tujuan]".
2. Linux : traceroute [IP Tujuan]".

Pada Jalur Atas

[![image.png](https://i.postimg.cc/PJJRrF5v/image.png)](https://postimg.cc/CnyNc7Dw)

pada gambar di atas bahwa pc0 (192.168.4.2) melakukan tracert ke pc1 (192.168.5.2) melalui router 2 (192.168.3.1) lalu ke router 1 (192.168.3.2) dan akhirnya ke pc1 (192.168.5.2) dan saya coba sebanyak 3 kali menghasilkan nilai yang sama.

[![image.png](https://i.postimg.cc/T1hTM08C/image.png)](https://postimg.cc/RJrkwcZH)

dan saya coba tracert 3 kali pada pc1 (192.168.5.2) melakukan tracert ke pc0 (192.168.4.2) melalui router 1 (192.168.5.1) lalu ke router 2 (192.168.3.1) dan akhirnya ke pc0 (192.168.4.2).

Konfigurasi untuk jalur bawah pada route 1 dan 2
[![image.png](https://i.postimg.cc/RZWJQ1N1/image.png)](https://postimg.cc/Xr0vnCKX)

[![image.png](https://i.postimg.cc/PJJRrF5v/image.png)](https://postimg.cc/CnyNc7Dw)

Kemudian saya coba untuk tracert lagi dari pc0 (192.168.4.2) ke pc1 (192.168.5.2) melalui router 2 (192.168.3.1) lalu ke router 1 (192.168.3.2) dan akhirnya ke pc1 (192.168.5.2) dan saya coba sebanyak 3 kali menghasilkan nilai yang sama.

[![image.png](https://i.postimg.cc/T1hTM08C/image.png)](https://postimg.cc/RJrkwcZH)

dan saya coba tracert 3 kali pada pc1 (192.168.5.2) melakukan tracert ke pc0 (192.168.4.2) melalui router 1 (192.168.5.1) lalu ke router 2 (192.168.3.1) dan akhirnya ke pc0 (192.168.4.2).

**Mengubah Metric Static Routing**
|  Devices 	| Destination Network 	|    Netmask    	|     Via     	|    Metric    	|
|:--------:	|:-------------------:	|:-------------:	|:-----------:	|:------------:	|
| Router 0 	|     192.168.4.0     	| 255.255.255.0 	| 192.168.2.1 	| 10 (Default) 	|
|          	|     192.168.5.0     	| 255.255.255.0 	| 192.168.1.1 	| 10 (Default) 	|
| Router 1 	|     192.168.4.0     	| 255.255.255.0 	| 192.168.3.1 	| 10 (Default) 	|
|          	|     192.168.2.0     	| 255.255.255.0 	| 192.168.1.2 	|       1      	|
| Router 2 	|     192.168.5.0     	| 255.255.255.0 	| 192.168.3.1 	| 10 (Default) 	|
|          	|     192.168.1.0     	| 255.255.255.0 	| 192.168.2.2 	|       1      	|

Jalur yang paling efisien dapat diubah dengan cara mengubah nilai metric pada konfigurasi static routing. Pada percobaan kali ini, jalur yang paling efisien adalah jalur yang melalui router 1.

[![pc0test2.png](https://i.postimg.cc/7Z3s2HyQ/pc0test2.png)](https://postimg.cc/nXLG8trv)

Terlihat pada gambar di atas bahwa pc0 (192.168.4.2) melakukan tracert ke pc1 (192.168.5.2) setelah menambahkan static router yang baru dengan metric 1. Jalur yang dilalui oleh paket data tersebut adalah jalur yang melalui router 2 (192.168.4.1) lalu ke router 0 (192.168.2.2) lalu ke router1 (192.168.1.1) dan akhirnya ke pc1 (192.168.5.2).

[![pc1test2.png](https://i.postimg.cc/MZ1d4ZnZ/pc1test2.png)](https://postimg.cc/kDXQRmNL)

Begitu juga dengan pc1 (192.168.5.2) melakukan tracert ke pc0 (192.168.4.2). Jalu yang dilalui oleh paket data tersebut adalah jalur yang melalui router 1 (102.168.5.1) lalu ke router 0 (192.168.1.2) lalu ke router2 (192.168.2.1) dan akhirnya ke pc0 (192.168.4.2).

Dapat dilihat bahwa jalur yang dilalui oleh paket data tersebut berbeda dengan sebelumnya. Hal ini dikarenakan adanya routing yang berbeda-beda pada masing-masing router. Dalam routing ini, router akan memilih jalur yang memiliki metric terkecil. Sehingga pemilihan jalur dipengaruhi oleh metric. Pada percobaan kali ini, jalur yang paling efisien adalah jalur yang melalui router 1. Ini dikarenakan metric yang digunakan untuk routing yang melalui router 0 adalah 1 dan metric yang digunakan untuk routing yang melalui router 1 dan 2 adalah 10.
