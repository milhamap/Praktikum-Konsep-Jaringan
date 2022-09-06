| Nama | Muhammad Ilham Adi Pratama |
|:----:|:--------------------------:|
|Kelas | 2 D4 IT A                  |
| NRP  | 3121600014                 |

## Cisco Packet Tracer

_Case Pertama_ (PC1 => PC2)
Jelaskan proses mengirim data dari PC1 ke PC2

_Case Kedua_ (PC1 => PC2)
Apabila PC1 sudah pernah nge-_ping_ pada PC2, apakah melakukan _broadcast_ lagi?

_Case Ketiga_ (PC2 => PC1)
Apabila PC1 sudah pernah mengirim data ke PC2 kemudian PC2 ingin mengirim data ke PC1 apakah perlu melakukan _broadcast_?

[![image.png](https://i.postimg.cc/PJhykVRD/image.png)](https://postimg.cc/34SmX17r)

Terdapat 3 Komputer yang terhubung pada _Network Devices_ dalam hal ini adalah Hub yang sudah disetel untuk _IPV4 Address_ pada masong masing PC seperti gambar dibawah ini,

[![image.png](https://i.postimg.cc/NfZy92QJ/image.png)](https://postimg.cc/MvbZgTMV)

PC0 di setel untuk _IPV4 Address_ 192.168.1.1, kemudian PC1 di setel untuk _IPV4 Address_ 192.168.1.2, dan PC2 di setel untuk _IPV4 Address_ 192.168.1.3

[![image.png](https://i.postimg.cc/jSGkFctH/image.png)](https://postimg.cc/hX1rJ9Jv)

Kemudian tekan pada kanan bawah, masuk ke _simulation_ kemudian _Show All/None_ dan _Edit Filters_ maka akan muncul tampilan seperti dibawah ini

[![image.png](https://i.postimg.cc/DZm5gpMd/image.png)](https://postimg.cc/Fd5jFpm7)

centang untuk ARP dan ICMP pada 

_Case Pertama_

1. Pastikan tidak ada IP Address yang disimpan oleh PC1

[![image.png](https://i.postimg.cc/HWRXkpcz/image.png)](https://postimg.cc/Thjpkvc5)

2. Lakukan _request packet_ ke IP _192.168.1.3_

[![image.png](https://i.postimg.cc/ry1tG7fC/image.png)](https://postimg.cc/Wt43TYLh)

3. Kemudian cek apa yang dikirim oleh PC1, dapat dilihat pada gambar dibawah ini, terdapat Packet Boardcast yang dikirim yaitu _FFFF.FFFF.FFFF_, maksudnya PC1 mencari siapa yang memiliki _IP Address_ 192.168.1.3 pada _Network Devices_ dengan menggunakan _broadcast_

[![image.png](https://i.postimg.cc/3xVRQZLx/image.png)](https://postimg.cc/w15HhD8C)

4. Kemudian cek pada _Command Prompt_ PC1 saat proses _request packet_ dan cek ada _cache_ IP yang disimpan oleh PC1 yaitu IP dari PC2 dengan alamat 192.168.1.3 

[![image.png](https://i.postimg.cc/SsMdyV7Q/image.png)](https://postimg.cc/47XVP6Sj)

_Case Kedua_

1. Lakukan _request packet_ ke PC2 lagi

[![image.png](https://i.postimg.cc/hGsGwq7V/image.png)](https://postimg.cc/t11yZwkg)

2. Dikarenakan PC1 pernah melakukan _request packet_ pada PC2, maka tidak perlu melakukan _broadcast_ lagi, karena _IP Address_ PC2 sudah tersimpan pada _cache ARP_ PC1

[![image.png](https://i.postimg.cc/Hk0R4Yf4/image.png)](https://postimg.cc/qNR1pTBz)

3. Dapat dicek dengan menggunakan perintah _arp -a_

[![image.png](https://i.postimg.cc/rwxbq1c9/image.png)](https://postimg.cc/WdpSnJdD)

####_Case Ketiga_

1. Lakukan _request packet_ dari PC2 ke PC1 dengan _IP Address_ 192.168.1.2

[![image.png](https://i.postimg.cc/5NTrLPnJ/image.png)](https://postimg.cc/CzCJVs3r)

2. Dikarenakan PC2 pernah _receive packet_ dari PC1, maka _IP Address_ dari PC1 sudah tersimpan pada PC2, dan tidak perlu melakukan _broadcast_ lagi

[![image.png](https://i.postimg.cc/W37R7Mtn/image.png)](https://postimg.cc/S2jtSY62)

3. Dapat dicek dengan menggunakan perintah _arp -a_

[![image.png](https://i.postimg.cc/N0k9Rz8P/image.png)](https://postimg.cc/HJjkg3hQ)

Jadi kesimpulannya, jika suatu komputer belum pernah _request packet_ dan belum pernah _receive packet_ pada komputer yang akan dituju, maka perlu melakukan proses _broadcast_ untuk mengenali _IP Address_ pada komputer yang dituju