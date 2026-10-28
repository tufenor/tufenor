// Playwright → PDF A5 a partir de dist/curso.html
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const dist = path.resolve(__dirname, '..', 'dist');
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.join(dist, process.env.BOOK_HTML || 'curso.html'), { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.emulateMedia({ media: 'print' });
  await page.pdf({ path: path.join(dist, (process.env.BOOK_OUT || 'LULA-GANHOU-Curso-Completo') + '.pdf'), width: '148mm', height: '210mm', printBackground: true, preferCSSPageSize: true });
  await browser.close();
  console.log('PDF gerado');
})();
