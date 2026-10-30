// Detecta texto sobreposto: retângulos de texto de elementos diferentes que se cruzam.
const { chromium } = require('playwright');
const file = process.argv[2] || 'dist/curso.html';
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + require('path').resolve(file));
  await p.waitForTimeout(1500);
  const res = await p.evaluate(() => {
    const out = [];
    document.querySelectorAll('.page').forEach((page, pi) => {
      const rects = [];
      const w = document.createTreeWalker(page, NodeFilter.SHOW_TEXT);
      let n;
      while ((n = w.nextNode())) {
        if (!n.textContent.trim()) continue;
        const el = n.parentElement;
        if (el.closest('svg')) continue;
        const cs = getComputedStyle(el);
        if (cs.visibility === 'hidden' || cs.display === 'none' || +cs.opacity === 0) continue;
        const r = document.createRange(); r.selectNodeContents(n);
        for (const c of r.getClientRects()) if (c.width > 1 && c.height > 1) {
          // só o miolo da letra: a caixa da fonte (sobretudo a Anton) é bem maior que o glifo
          const k = c.height * 0.22;
          const q = { left: c.left, right: c.right, top: c.top + k, bottom: c.bottom - k, width: c.width, height: c.height - 2 * k };
          rects.push({ el, q, t: n.textContent.trim().slice(0, 40) });
        }
      }
      for (let i = 0; i < rects.length; i++) for (let j = i + 1; j < rects.length; j++) {
        const A = rects[i], B = rects[j];
        const same = A.el === B.el || A.el.contains(B.el) || B.el.contains(A.el);
        // no mesmo elemento, só conta se forem linhas diferentes (entrelinha apertada demais)
        if (same && Math.abs(A.q.top - B.q.top) < 2) continue;
        const x = Math.min(A.q.right, B.q.right) - Math.max(A.q.left, B.q.left);
        const y = Math.min(A.q.bottom, B.q.bottom) - Math.max(A.q.top, B.q.top);
        if (x <= 1 || y <= 1) continue;
        const small = Math.min(A.q.width * A.q.height, B.q.width * B.q.height);
        if ((x * y) / small < 0.15) continue;
        out.push(`p${pi + 1}: "${A.t}" × "${B.t}"`);
      }
    });
    return out;
  });
  const uniq = [...new Set(res)];
  console.log(uniq.length ? uniq.join('\n') : 'Sem texto sobreposto');
  console.log('Total:', uniq.length);
  await b.close();
})();
