(function() {
  var style = document.createElement('style');
  style.textContent =
    '#export-toolbar{position:fixed;bottom:0;left:0;right:0;z-index:99999;' +
    'background:#332211;color:#FFF;padding:3mm 6mm;' +
    'display:flex;align-items:center;gap:3mm;font-family:Arial,sans-serif;' +
    'font-size:10pt;box-shadow:0 -2px 10px rgba(0,0,0,0.3);' +
    'justify-content:center;flex-wrap:wrap;}' +
    '.tb-label{font-weight:bold;color:#CBB17E}' +
    '.tb-btn{background:#CBB17E;color:#332211;border:none;' +
    'padding:2mm 5mm;border-radius:4px;cursor:pointer;' +
    'font-size:10pt;font-weight:bold;}' +
    '.tb-btn:hover{background:#EFE3C3}' +
    '.tb-pdf{background:#E06666;color:#FFF}' +
    '.tb-png{background:#4A90E2;color:#FFF}' +
    '.tb-docx{background:#6AA84F;color:#FFF}' +
    '.tb-size{color:#887755;font-size:8pt;margin-left:2mm}' +
    '.tb-home{background:transparent;color:#CBB17E;text-decoration:none;font-size:9pt;margin-right:auto}' +
    '.tb-home:hover{color:#EFE3C3}' +
    '@media print{#export-toolbar{display:none!important}}';
  document.head.appendChild(style);

  var bar = document.createElement('div');
  bar.id = 'export-toolbar';
  bar.innerHTML =
    '<a class="tb-home" href="../index.html">Kembali</a>' +
    '<span class="tb-label">Eksport:</span>' +
    '<button class="tb-btn tb-pdf" onclick="window.print()">PDF A4</button>' +
    '<button class="tb-btn tb-png" id="btn-png" onclick="exportPNG()">PNG</button>' +
    '<button class="tb-btn tb-docx" onclick="exportDOCX()">DOCX</button>' +
    '<span class="tb-size">A4 - 210x297mm</span>';
  document.body.appendChild(bar);

  var s = document.createElement('script');
  s.src = 'https://cdn.jsdelivr.net/npm/html2canvas@1.4.1/dist/html2canvas.min.js';
  document.head.appendChild(s);
})();

window.exportPNG = function() {
  if (typeof html2canvas === 'undefined') {
    var check = setInterval(function() {
      if (typeof html2canvas !== 'undefined') { clearInterval(check); doExportPNG(); }
    }, 200);
    setTimeout(function() { clearInterval(check); }, 10000);
    return;
  }
  doExportPNG();
};

function doExportPNG() {
  var btn = document.getElementById('btn-png');
  btn.textContent = '...'; btn.disabled = true;
  html2canvas(document.body, {
    scale: 3, width: 794, height: 1123,
    useCORS: true, backgroundColor: '#FFF', logging: false
  }).then(function(canvas) {
    var a = document.createElement('a');
    a.download = (document.title || 'page').replace(/[^a-zA-Z0-9]/g, '_') + '.png';
    a.href = canvas.toDataURL('image/png');
    a.click();
    btn.textContent = 'PNG'; btn.disabled = false;
  }).catch(function(e) {
    alert('Ralat PNG: ' + e.message);
    btn.textContent = 'PNG'; btn.disabled = false;
  });
}

window.exportDOCX = function() {
  var html = document.documentElement.outerHTML;
  var doc = '<!DOCTYPE html>' +
    '<html xmlns:o="urn:schemas-microsoft-com:office:office" ' +
    'xmlns:w="urn:schemas-microsoft-com:office:word" ' +
    'xmlns="http://www.w3.org/TR/REC-html40">' +
    '<head><meta charset="UTF-8"><title>' + document.title + '</title>' +
    '<!--[if gte mso 9]><xml><w:WordDocument><w:View>Print</w:View></w:WordDocument></xml><![endif]-->' +
    '<style>body{font-family:Arial;margin:2cm;color:#000}p{margin:0}</style></head>' +
    '<body>' + document.body.innerHTML.replace(/<script[\s\S]*?<\/script>/gi, '') +
    '</body></html>';

  var blob = new Blob([doc], { type: 'application/msword' });
  var a = document.createElement('a');
  a.download = (document.title || 'page').replace(/[^a-zA-Z0-9]/g, '_') + '.doc';
  a.href = URL.createObjectURL(blob);
  a.click();
  URL.revokeObjectURL(a.href);
};