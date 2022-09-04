| Nama | Muhammad Ilham Adi Pratama|
|:----:|:-------------------------:|
| NRP  |        3121600014         |
|Kelas | 2 D4 Teknik Informatika A |
|Matkul| Praktikum Konsep Jaringan |
## Documentation Task Wireshark
# Colors Rule
Wireshark menggunakan warna untuk membantu mengidentifikasi jenis lalu lintas secara sekilas. Secara default, Green adalah lalu lintas TCP, Dark Blue adalah lalu lintas DNS, Light Blue adalah lalu lintas UDP, dan Dark mengidentifikasi paket TCP dengan masalah — misalnya, mereka bisa saja dikirim tidak sesuai pesanan.
| Color in Wireshark |                                  Packet Type                                 |
|:------------------:|:----------------------------------------------------------------------------:|
|    Light purple    |                                    TCP, TLS                                  |
|       Purple       |                                     DCERPC                                   |
|        Pink        |                                      ICMP                                    |
|       Cream        |                                      ARP                                     |
|       White        |                                   Broadcast                                  |
|        Gray        |                                 System Event                                 |
|     Light blue     |                                      UDP                                     |
|        Black       |                              Packets with errors                             |
|     Light green    |                                 HTTP traffic                                 |
|    Light yellow    | Windows-specific traffic,  including Server Message Blocks (SMB) and NetBIOS |
|     Dark yellow    |                                    Routing                                   |
|      Dark gray     |                         TCP SYN, FIN and ACK traffic                         |
|         Red        |                            Invalid Display Filter                            |

Light blue, Pink and Light purple	
[![image.png](https://i.postimg.cc/rwhn2tZb/image.png)](https://postimg.cc/sMh9p1r9)

Black Color
[![image.png](https://i.postimg.cc/X7StsFtk/image.png)](https://postimg.cc/V5g76SfJ)

Dark gray, Cream and Red
[![image.png](https://i.postimg.cc/y8rPbCkC/image.png)](https://postimg.cc/pmzzm7fs)

## Packet Analyzer

[![image.png](https://i.postimg.cc/CMmfNHRW/image.png)](https://postimg.cc/RqJFCtQR)

Dengan menggunakan ping pada default gateway yang diberikan oleh router (wifi) sudah bisa melakukan analisa suatu packet dengan bantuan Wireshark.

[![image.png](https://i.postimg.cc/1584Kxhq/image.png)](https://postimg.cc/1fZ99jzm)

Gambar di atas menunjukkan bahwa IP Address pada adaptor wifi yakni 192.168.18.98 dan default gatewaynya 192.168.18.1 dengan data tersebut kita bisa mengetahui packet yang terlintas pada Wireshark.

[![image.png](https://i.postimg.cc/W3fTD34f/image.png)](https://postimg.cc/9RTvKcZG)
Dalam box Internet Protocol terdapat:
-  Version: 4
Menunjukkan versi yang digunakan adalah versi 4
- Header length: 20 bytes
Menunjukkan panjangnya header yang ada di lapisan network adalah
sebesar 20 bytes
- Source: 192.168.18.98 Destination: 192.168.18.1
Menunjukkan IP dari source yaitu 192.168.18.98 dan IP dari destination
yaitu 192.168.18.1
- Kesimpulan:
Lapisan network, panjangnya header yang diberikan sebesar 20 bytes
dengan IP source 192.168.18.98 dan IP destination yaitu 192.168.18.1

## ICMP pada whireshark
Internet Control Message Protocol (ICMP) adalah salah satu protokol inti dari keluarga
protokol internet. ICMP utamanya digunakan oleh sistem operasi komputer jaringan untuk
mengirim pesan kesalahan yang menyatakan, sebagai contoh, bahwa komputer tujuan tidak
bisa dijangkau. ICMP berbeda tujuan dengan TCP dan UDP dalam hal ICMP tidak digunakan
secara langsung oleh aplikasi jaringan milik pengguna. salah satu pengecualian adalah
aplikasi ping yang mengirim pesan ICMP Echo Request (dan menerima Echo Reply) untuk
menentukan apakah komputer tujuan dapat dijangkau dan berapa lama paket yang dikirimkan
dibalas oleh komputer tujuan. (id.wikipedia.org)

[![image.png](https://i.postimg.cc/NMLwwcx8/image.png)](https://postimg.cc/zbmQn463)

Dari gambar ICMP diatas saat echo ping request tersebut, icmp bertype 8, code 0, dengan
algoritma checksum 0x493e, banyak identifier (ident ifikasi) (BE) 1 bytes dan Sequence
Number (BE) 1053 byte, sedangkan banyak identifier (ident ifikasi) (LE) 256 bytes dan Sequence
Number (LE) 7428 byte. Serta hasil diatas menunjukkan saat proses request ping, paket
dari source (192.168.18.98) IP address dari komputer kita akan merequest ({echo (ping)
request) ke destinat ion (192.168.18.1) IP address router wifi biznet.

[![image.png](https://i.postimg.cc/RZFrtmjk/image.png)](https://postimg.cc/ppg1NwVC)

Dalam box frame terdapat:
a) Arrival Time: Sep  4, 2022 10:02:09.696163000 SE Asia Standard Time
Menunjukkan waktu saat pengiriman data
b) [Time delta from previous captured frame: 0.192803000 seconds]
[Time delta from previous displayed frame: 0.192803000 seconds]
[Time since reference or first frame: 88.162285000 seconds]
Menunjukkan waktu sebelum capture dari frame, yaitu 0.192803000 seconds dan waktu sejak awal frame 88.162285000 seconds.
c) Frame Number: 280
Menunjukkan nomor dari frame tersebut yaitu 280
d) Frame Length: 74 bytes (592 bits)
Menunjukkan panjangnya frame adalah sebasar 74 bytes
e) [Protocols in frame: eth:ethertype:ip:icmp:data]
Menunjukkan protokol-protokol apa saja yang ada di frame 280 yaitu ada Ethernet, Internet Protocol (IP), Internet Control Message Protocol (ICMP) & Data
d) Kesimpulan:
Lapisan ini menunjukkan apa saja yang ada dalam satu frame yaitu
JOBSHEET TEUM
seperti protokol-protokol yang ada di lapisan ini Ethernet, Internet Protocol (IP), Transmission Control Protocol (TCP), Hypertext Transfer Protocol (HTTP), dan data-text-lines.