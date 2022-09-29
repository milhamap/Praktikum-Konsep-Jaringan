**LAPORAN PRAKTIKUM KONSEP JARINGAN**

| Nama | Muhammad Ilham Adi Pratama |
|:----:|:--------------------------:| 
|Kelas | 2 D4 IT A                  |
| NRP  | 3121600014                 |


**TUGAS PRAKTIKUM**
Topologi yang saya gunakan adalah sebagi berikut Topologi tersebut terdiri dari 1 router, 3 switch, dan 9 pc-client dengan 3 VLAN (192.168.10.1 - 10  & 192.168.20.1 - 20 & 192.168.20.1 - 20)

[![image.png](https://i.postimg.cc/NftgPVkK/image.png)](https://postimg.cc/PN6sCScH)

**Configuration VLAN Database (Router)**

[![image.png](https://i.postimg.cc/90f3KJhs/image.png)](https://postimg.cc/wynbs53k)

Atur unutk VLAN 10 berinama dengan Admin, VLAN 20 berinama dengan Developer dan VLAn 30 berinama dengan Management pada Router.

**Configuration VLAN Database (Switch)**

[![image.png](https://i.postimg.cc/RFh8SqWD/image.png)](https://postimg.cc/vgRXXYLr)

Atur unutk VLAN 10 berinama dengan Admin, VLAN 20 berinama dengan Developer dan VLAn 30 berinama dengan Management pada masing masing Switch.

**Configuration IP VLAN pada Router**

[![image.png](https://i.postimg.cc/W33XPKdm/image.png)](https://postimg.cc/1gkpGvc4)

Kita tambahkan IP untuk masing masing VLAN, VLAN 10 tambahkan IP Address 192.168.10.1, VLAN 20 tambahkan IP Address 192.168.20.1, VLAN 30 tambahkan IP Address 192.168.30.1

**Configuration Port yang dilalui oleh VLAN**

[![image.png](https://i.postimg.cc/fTQNKjtW/image.png)](https://postimg.cc/z376DhF4)

Set untuk port yang dilalui Switch ke Switch kedalam mode Trunk.

**Configuration IP pada masing masing PC**

[![image.png](https://i.postimg.cc/B6dXNLHW/image.png)](https://postimg.cc/N9ksj0db)

Disini saya konsep jadi terdapat 3 lantai, dan masing masing lantai memiliki 1 VLAN, untuk lantai 3 yaitu VLAN 10, kita set masing masing PC dengan terurut untuk IP (192.168.10.2, 192.168.10.3, 192.168.10.4) dengan default gateway (IP untuk VLAN) 192.168.10.1. 

Kemudian kita set lantai 2 untuk VLAN 20, kita atur masing masing PC dengan terurut untuk IP (192.168.20.2, 192.168.20.3, 192.168.20.4) dengan default gateway (IP untuk VLAN) 192.168.20.1.

Kemudian kita set lantai 1 untuk VLAN 30, kita atur masing masing PC dengan terurut untuk IP (192.168.30.2, 192.168.30.3, 192.168.30.4) dengan default gateway (IP untuk VLAN) 192.168.30.1.

**Tes Ping untuk masing masing PC**

[![image.png](https://i.postimg.cc/W1XwNvQD/image.png)](https://postimg.cc/k2RbskM9)

Ping diatas berasal dari PC7 192.168.30.1 - 192.168.30.3 (VLAN 30) berhasil melakukan ping pada IP PC8 192.168.30.1 - 192.168.30.4 (VLAN 30) dikarenakan PC tersebut dalam satu network yaitu VLAN 30.

Bagaimana jika PC7 melakukan ping pada IP PC yang berbeda network?, dalam kasus ini melakukan ping pada PC2 192.168.10.1 - 192.168.10.2 (VLAN 10) maka yang dihasilkan adalah Request timed out dikarenakan untuk setiap PC sudah memiliki VLAN dan PC7 mencoba mengakses PC2 yang diluar dari network yang sudah didaftarkan.
