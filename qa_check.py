import os, sys
from pypdf import PdfReader

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
FINAL_PATH = os.path.join(OUTPUT_DIR, "MISI_EJEN_KEMUDAHAN_AWAM_FULL_KIT.pdf")

issues = []
passes = []

def check(desc, condition, detail=""):
    if condition:
        passes.append("  [OK] " + desc + (" - " + detail if detail else ""))
    else:
        issues.append("  [FAIL] " + desc + (" - " + detail if detail else ""))

print("=" * 60)
print("  QA SEMAKAN AUTOMATIK - MISI EJEN KEMUDAHAN AWAM")
print("=" * 60)

# 1. Kewujudan fail
exists = os.path.exists(FINAL_PATH)
size = os.path.getsize(FINAL_PATH) if exists else 0
check("Fail gabungan wujud", exists, "Saiz: %.2f MB" % (size/1024/1024))
check("Saiz > 0", size > 0, "%d bytes" % size)

# 2. Bilangan halaman
if exists:
    try:
        reader = PdfReader(FINAL_PATH)
        num_pages = len(reader.pages)
        check("Bilangan halaman = 12", num_pages == 12, "%d halaman" % num_pages)
    except Exception as e:
        issues.append("  [FAIL] Gagal baca PDF - %s" % str(e))
        num_pages = 0
else:
    num_pages = 0

# 3. Saiz setiap PDF individu
print("\n[SAIZ] Semakan saiz PDF individu:")
pdf_files = sorted(f for f in os.listdir(OUTPUT_DIR) if f.startswith("A4_") and f.endswith(".pdf"))
small_pdfs = []
for fname in pdf_files:
    path = os.path.join(OUTPUT_DIR, fname)
    sz = os.path.getsize(path)
    size_kb = sz / 1024
    status = "[OK]" if sz >= 20 * 1024 else "[KECIL]"
    if sz < 20 * 1024:
        small_pdfs.append(fname)
    print("  %s %s: %.1f KB" % (status, fname, size_kb))
check("Tiada PDF < 20KB", len(small_pdfs) == 0, "Risalah: " + ", ".join(small_pdfs) if small_pdfs else "")

# 4. Dimensi halaman
print("\n[DIMENSI] Semakan dimensi halaman:")
if exists and num_pages > 0:
    all_a4 = True
    for i, page in enumerate(reader.pages):
        box = page.mediabox
        w = box.width
        h = box.height
        w_mm = w / 72 * 25.4
        h_mm = h / 72 * 25.4
        status = "[OK]" if (200 < w_mm < 220 and 280 < h_mm < 310) else "[SALAH]"
        if status == "[SALAH]":
            all_a4 = False
        print("  %s Halaman %d: %.1fmm x %.1fmm" % (status, i+1, w_mm, h_mm))
    check("Semua halaman A4 (+-210x297mm)", all_a4)
else:
    check("Semua halaman A4 (+-210x297mm)", False, "PDF tidak dapat dibaca")

# 5. Ringkasan
print("\n" + "=" * 60)
print("  RINGKASAN QA")
print("=" * 60)
for p in passes:
    print(p)
if issues:
    for i in issues:
        print(i)
    print("\nWARNING: %d isu dijumpai - perlu semakan manual" % len(issues))
else:
    print("\nSEMUA LULUS - Tiada isu dijumpai")

print("\nPDF gabungan: %s" % FINAL_PATH)
print("Halaman: %d/12, Saiz: %.2f MB" % (num_pages, size/1024/1024))