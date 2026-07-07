# ARAHAN INDUK: Penghasilan Kit A4 Boleh Cetak
## Modul "Misi Ejen Penjaga Kemudahan Awam" — Treasure Hunt PAK-21
### Program Rasmi Pergerakan Puteri Islam Malaysia — Sekolah Kebangsaan (Tahun 6)

**Tujuan dokumen ini:** Panduan utama untuk ejen AI menghasilkan kit cetakan Treasure Hunt bagi **Program Rasmi Pergerakan Puteri Islam Malaysia (PPIM)** — Kegiatan Kokurikulum Sekolah Kebangsaan, Tahap 2 (Tahun 6). **Rujukan wajib:** `MODUL TREASURE HUNT.docx` — semua kandungan teks, soalan, skema jawapan dan markah MESTI diambil tepat dari MODUL tersebut. Tiada pengubahan kandungan dibenarkan.

**Output akhir:** 12 keping A4 (210mm x 297mm), 300 DPI, digabung menjadi satu PDF `MISI_EJEN_KEMUDAHAN_AWAM_FULL_KIT.pdf`.

---

## 0. ARAHAN AM UNTUK SEMUA EJEN AI (BACA DAHULU)

1. **Rujukan kandungan utama:** `MODUL TREASURE HUNT.docx` — semua teks, petunjuk, markah, dan susunan stesen adalah tepat dari dokumen ini.

2. **Aset grafik:** Guna emoji/ikon Unicode sahaja (🏥 📚 🚒 👮 🚏 🛝 🕌 🍛 ⚽ 🏆 🏅 🎁 ✏️ 📖 ⭐). Tiada ilustrasi tersuai diperlukan. Aset PNG sedia ada: `treasure_hunt_kemudahan_awam.png` sebagai rujukan gaya visual.

3. **Bahasa:** Semua teks dalam Bahasa Melayu standard, mesra murid Tahun 6.

4. **Warna latar umum:** `#EFE3C3` (Warm Parchment) dan `#CBB17E` (Muted Gold). Teks utama: `#332211` (Dark Espresso).

5. **Kod warna setiap stesen (konsisten di semua halaman berkaitan):**
   | Stesen | Warna | Kod Hex |
   |---|---|---|
   | Stesen 1 – Kenali Saya | Soft Sky Blue | `#4A90E2` |
   | Stesen 2 – Betul atau Salah | Pastel Salmon | `#E06666` |
   | Stesen 3 – Cari Kesalahan | Earth Green | `#6AA84F` |
   | Stesen 4 – Kotak Misteri | Bright Amber | `#F6B26B` |
   | Stesen 5 – Cabaran Akhir | Royal Purple | `#8E7CC3` |

6. **Fon:** Tajuk Slab-Serif Impact / Comic Bold, sub-tajuk Sans-Serif Bold min 16pt, teks arahan Sans-Serif 11–12pt *line spacing* 1.25.

7. **Setiap halaman:** nombor halaman bawah, margin cetak selamat 5mm.

8. **Penamaan fail:** `A4_[NN]_[nama].pdf`, contoh: `A4_01_Poster_Misi.pdf`.

9. **Jangan ubah kandungan kurikulum, skema jawapan atau markah — kekalkan tepat seperti dalam MODUL TREASURE HUNT.docx.**

---

## 1. PEMBAHAGIAN TUGAS ANTARA EJEN

- **Agen A (Layout/HTML — ChatGPT/Claude):** Bina HTML/CSS cetakan untuk setiap halaman berdasarkan spesifikasi di bawah. Output: fail `.html` dengan `@page { size: A4; }` dalam CSS.

- **Agen B (Tiada — guna emoji Unicode):** Tiada ilustrasi tersuai diperlukan. Semua ikon menggunakan emoji Unicode.

- **Agen C (Kandungan Teks):** Salin-tampal SEMUA teks tepat dari `MODUL TREASURE HUNT.docx` — soalan, petunjuk, skema jawapan, markah. Tiada parafrasa.

- **Agen D (QA/Cetak — DeepSeek):** Semak setiap halaman: resolusi 300 DPI, tiada teks terpotong, kontras cukup untuk fotostat hitam-putih, margin cetak selamat.

---

## 2. SPESIFIKASI 12 HALAMAN A4

### Halaman 1 — Poster Misi / Muka Depan
- Tajuk: "MISI EJEN PENJAGA KEMUDAHAN AWAM — TREASURE HUNT"
- Cerita Misi (teks tepat dari MODUL): "Amaran! Bandar Harmoni berada dalam bahaya..."
- Bahan Diperlukan (5 bullet dari MODUL)
- Lokasi stesen ringkas: Kelas → Perpustakaan → Surau → Kantin → Padang
- Latar parchment + gold, gaya detektif vintage (rujuk `treasure_hunt_kemudahan_awam.png`)

### Halaman 2 — Peta Harta Karun
- Aliran menegak: MULA → Stesen 1-5 → HARTA KARUN
- 5 lokasi: Dalam Kelas, Perpustakaan, Surau, Kantin, Padang
- Anak panah putus-putus merah antara stesen
- Petak "🏆 HARTA KARUN (Bilik Guru / Kelas)" di hujung
- Guna emoji 📍 untuk penanda stesen
- Boleh cetak A3, tapi versi A4 ini untuk edaran murid

### Halaman 3 — Sampul 1: Kenali Kemudahan Awam (Biru `#4A90E2`)
- Header: "MISI 1 — Kenali Kemudahan Awam"
- Arahan: "Namakan kemudahan awam berikut dan nyatakan SATU fungsi."
- 6 ikon emoji berturutan: 🏥 📚 🚒 👮 🚏 🛝
- Setiap ikon ada ruang Nama: ___ dan Fungsi: ___
- Petunjuk (tepat dari MODUL): "Saya tempat orang membaca buku."
- Kotak markah "MARKAH: ___/12"

### Halaman 4 — Sampul 2: Betul atau Salah (Salmon `#E06666`)
- Header: "MISI 2 — Betul atau Salah?"
- 4 situasi (tepat dari MODUL):
  1. Ali menconteng tandas awam. (Salah)
  2. Siti membuang sampah ke dalam tong. (Betul)
  3. Amir mematahkan buaian. (Salah)
  4. Farah beratur menaiki bas. (Betul)
- Setiap situasi: kotak tanda ✔/✖ + ruang Alasan: ___
- Cabaran tambahan: "Mengapa kita tidak boleh merosakkan kemudahan awam?"
- Petunjuk: "Pergi ke tempat orang berwuduk dan bersolat."
- Kotak markah "MARKAH: ___/8"

### Halaman 5 — Sampul 3: Cari 5 Kesalahan (Hijau `#6AA84F`)
- Header: "MISI 3 — Cari 5 Kesalahan"
- Guru tampal gambar (ruang ilustrasi/placeholder): sampah, vandalisme, kerusi rosak, pokok dipatahkan, lampu pecah
- Arahan: "Cari 5 kesalahan dalam gambar."
- Ruang senarai 1-5 bergaris

### Halaman 6 — Sampul 3: Cadangan Penyelesaian
- Sambungan: "Cadangkan satu cara mengatasi setiap masalah."
- Ruang 1-5 bergaris untuk cadangan
- Petunjuk: "Cari tempat orang membeli makanan."
- Kotak markah "MARKAH: ___/10"
- (Boleh cetak dupleks dengan Halaman 5)

### Halaman 7 — Sampul 4: Kotak Misteri (Jingga `#F6B26B`)
- Header: "MISI 4 — Kotak Misteri"
- Arahan: guru sediakan gambar dalam kotak misteri (Hospital, Balai Polis, Padang, Perpustakaan, Jalan Raya)
- Murid ambil satu gambar, terangkan dalam 30 saat
- Ruang: ✔ Nama: ___ ✔ Fungsi: ___ ✔ Cara menjaganya: ___
- Petunjuk: "Pergi ke kawasan murid bersukan."
- Kotak markah "MARKAH: ___/10"

### Halaman 8 — Sampul 5: Cabaran Akhir KBAT (Ungu `#8E7CC3`)
- Header: "MISI AKHIR — Cabaran KBAT"
- Soalan (tepat dari MODUL): "Jika semua kemudahan awam rosak... Apakah kesannya kepada: rakyat, sekolah, negara"
- 3 ruang bergaris
- "Kemudian cipta slogan." + ruang
- Teks tahniah: "Anda berjaya menamatkan semua misi!"
- Kotak markah "MARKAH: ___/10"

### Halaman 9 — Lembaran Jawapan Kumpulan
- Ruang NAMA KUMPULAN, NAMA AHLI
- Jadual: Stesen | Markah Maksimum | Markah Diperoleh
  - 1 | /12
  - 2 | /8
  - 3 | /10
  - 4 | /10
  - 5 | /10
  - JUMLAH | /50
- Boleh tambah ruang bintang penilaian

### Halaman 10 — Kad Petunjuk Guru (4 dalam 1 muka surat)
- Grid 2×2, setiap kad berwarna mengikut stesen:
  - 📚 "Banyak buku di sini." (Ke Perpustakaan)
  - 🕌 "Tempat umat Islam menunaikan solat." (Ke Surau)
  - 🍛 "Ramai murid makan di sini." (Ke Kantin)
  - ⚽ "Tempat bersukan." (Ke Padang)

### Halaman 11 — Idea Harta Karun
- Tajuk: "Idea Harta Karun"
- Senarai ganjaran (tepat dari MODUL):
  🍬 Gula-gula | ✏️ Pensel | 📖 Penanda buku | ⭐ Pelekat | 🏅 Sijil
- Ikon/gambar setiap item, boleh guna sebagai senarai semak guru

### Halaman 12 — Sijil Ejen Penjaga Kemudahan Awam
- Border hiasan emas
- Tajuk: "SIJIL EJEN PENJAGA KEMUDAHAN AWAM"
- Teks: "Diberikan kepada _______________ kerana berjaya menyelesaikan Treasure Hunt Kemudahan Awam. Tahniah!"
- Ikon pingat 🏅 di tengah
- Ruang Tarikh & Tandatangan Guru

---

## 3. SENARAI SEMAK AKHIR (QA) SEBELUM CETAK

- [ ] Semua fail wujud (12 halaman) dan dinamakan `A4_[NN]_[nama].pdf`
- [ ] Kandungan teks 100% tepat dari `MODUL TREASURE HUNT.docx`
- [ ] Kod warna stesen konsisten
- [ ] Markah tepat (12+8+10+10+10 = 50)
- [ ] Emoji/ikon dipaparkan dengan betul
- [ ] Boleh dibaca pada saiz cetak sebenar
- [ ] Versi hitam-putih/grayscale masih jelas
- [ ] PDF gabungan disusun mengikut turutan 1→12
