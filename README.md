&nbsp;Schrödinger’s LED



Bu proje, bir kuantum bilgisayarından (IBM Quantum) alınan gerçek rastgelelik verisinin, bir mikrodenetleyici (Arduino Nano) üzerinden fiziksel dünyaya aktarılmasını hedefler.



&nbsp;Sistem Mimarisi

\- Kuantum Katmanı: Qiskit kütüphanesi ile süperpozisyon durumundaki bir qubit ölçülerek gerçek rastgele sayı üretilir.

\- İletişim: Python üzerinden UART (Serial) protokolü ile mikrodenetleyiciye veri aktarımı sağlanır.

\- Donanım: Gelen veriye göre LED, kuantum durumunun "çökmesi" (collapse) sonucunda 'Açık' veya 'Kapalı' duruma geçer.



&nbsp;Donanım Bileşenleri

\- Arduino Nano

\- Mor LED (Kuantum durum göstergesi)

\- 220 Ohm Direnç

