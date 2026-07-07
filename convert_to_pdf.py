import os, sys
from playwright.sync_api import sync_playwright

PAGES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pages")
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")

def convert_all():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    html_files = sorted(f for f in os.listdir(PAGES_DIR) if f.endswith(".html") and f != "toolbar.js")

    if not html_files:
        print("ERROR: Tiada fail HTML dijumpai dalam pages/")
        sys.exit(1)

    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 794, "height": 1123})
        page = context.new_page()

        for fname in html_files:
            src = os.path.join(PAGES_DIR, fname)
            out_name = fname.replace(".html", ".pdf")
            out_path = os.path.join(OUTPUT_DIR, out_name)

            try:
                page.goto(f"file://{os.path.abspath(src)}", wait_until="networkidle")
                page.wait_for_timeout(1000)

                page.pdf(
                    path=out_path,
                    format="A4",
                    print_background=True,
                    margin={"top": "5mm", "bottom": "5mm", "left": "5mm", "right": "5mm"},
                )
                size_kb = os.path.getsize(out_path) / 1024
                print(f"OK: {fname} -> {out_name} ({size_kb:.1f} KB)")
                results.append((fname, "BERJAYA", size_kb))
            except Exception as e:
                print(f"FAIL: {fname} -> {str(e)}")
                results.append((fname, "GAGAL", 0))

        browser.close()

    print("\n=== RINGKASAN ===")
    for fname, status, size in results:
        print(f"  [{status}] {fname} ({size:.1f} KB)" if status == "BERJAYA" else f"  [{status}] {fname}")
    print(f"\nJumlah: {len(results)} fail, BERJAYA: {sum(1 for r in results if r[1]=='BERJAYA')}, GAGAL: {sum(1 for r in results if r[1]=='GAGAL')}")

if __name__ == "__main__":
    convert_all()