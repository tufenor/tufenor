// Detecta conteúdo invadindo o rodapé (folga mínima de 4 mm) e conta páginas.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(__dirname, '..', 'dist', 'curso.html'));
  await page.evaluate(() => document.fonts.ready);
  await page.emulateMedia({ media: 'print' });
  const res = await page.evaluate(() => {
    const MM = 96 / 25.4, bad = [];
    const pages = [...document.querySelectorAll('.page')];
    for (const p of pages) {
      const r = p.getBoundingClientRect();
      const footer = p.querySelector('.footer');
      const limit = footer ? footer.getBoundingClientRect().top - 4 * MM : r.bottom;
      let maxB = 0;
      p.querySelectorAll('.content *').forEach(el => {
        if (el.closest('svg') && el.tagName !== 'svg') return;
        const b = el.getBoundingClientRect();
        if (b.height > 0 && b.width > 0) maxB = Math.max(maxB, b.bottom);
      });
      const right = [...p.querySelectorAll('.content *')].some(el => !(el.closest('svg') && el.tagName !== 'svg') && el.getBoundingClientRect().right > r.right + 1);
      if (maxB > limit + 0.5 || right) bad.push({ page: p.dataset.num, overflowMM: +((maxB - limit) / MM).toFixed(1), right });
    }
    return { total: pages.length, bad };
  });
  await browser.close();
  console.log(`Páginas: ${res.total}`);
  if (res.bad.length) { console.log('OVERFLOW:', JSON.stringify(res.bad)); process.exit(1); }
  console.log('Overflow: 0');
})();
