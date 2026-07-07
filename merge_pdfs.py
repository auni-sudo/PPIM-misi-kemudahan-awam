import os, sys
from pypdf import PdfWriter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
FINAL_NAME = "MISI_EJEN_KEMUDAHAN_AWAM_FULL_KIT.pdf"

def merge():
    writer = PdfWriter()
    pdf_files = sorted(
        f for f in os.listdir(OUTPUT_DIR)
        if f.startswith("A4_") and f.endswith(".pdf")
    )

    if not pdf_files:
        print("ERROR: Tiada fail PDF dijumpai dalam output/")
        sys.exit(1)

    if len(pdf_files) != 12:
        print(f"AMARAN: Jumlah PDF = {len(pdf_files)}, sepatutnya 12. Semak sebelum gabung.")

    print(f"PDF ditemui: {len(pdf_files)} fail")
    for fname in pdf_files:
        path = os.path.join(OUTPUT_DIR, fname)
        writer.append(path)
        print(f"  + {fname}")

    final_path = os.path.join(OUTPUT_DIR, FINAL_NAME)
    with open(final_path, "wb") as f:
        writer.write(f)

    size_mb = os.path.getsize(final_path) / (1024 * 1024)
    print(f"\nGabungan siap: {FINAL_NAME}")
    print(f"Lokasi: {final_path}")
    print(f"Saiz: {size_mb:.2f} MB")
    print(f"Halaman: {len(pdf_files)}")

if __name__ == "__main__":
    merge()