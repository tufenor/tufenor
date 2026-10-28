// Preenche o espaço livre no pé das páginas com chamadas de tabloide.
// Mede cada página já diagramada e injeta um bloco do tamanho certo antes da linha de fonte.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const FILE = path.join(ROOT, 'dist', 'curso.html');
const CROWD = fs.readFileSync(path.join(ROOT, 'src', 'svg', 'crowd-wide.svg'), 'utf8');
// Ganchos do escopo (Seção 3.4): cada número aqui tem fonte no corpo do curso
const HOOKS = [
  ['MAIS 4 ANOS', 'Você vai ficar?'],
  ['TAXAÇÃO', 'Mais 4 anos de taxação. Quanto mais vão tirar de você?'],
  ['DÍVIDA', 'A dívida passou de R$ 11 trilhões. Adivinha quem paga essa conta.'],
  ['LIBERDADE', 'Seu dinheiro. Suas regras. Sua liberdade.'],
  ['URGENTE', 'Um imposto novo a cada 27 dias. Seu dinheiro não precisa ficar para ver o próximo.'],
  ['DECISÃO', 'Eles não mudaram a direção. Mude você.'],
  ['FAMÍLIA', 'Enquanto eles discutem, você protege a sua família.'],
  ['AJUSTE', 'Até R$ 450 bilhões de ajuste vêm aí. Seu patrimônio vai esperar sentado?'],
  ['RECORDE', 'Arrecadação recorde de R$ 2,9 trilhões. E o que voltou para você?'],
  ['ACORDE', 'Parece um pesadelo? Então acorde em outro país.'],
  ['QUEM PRODUZ', 'Quem trabalha e produz não precisa assistir parado.'],
  ['O BRASIL QUE TRABALHA', 'Está fazendo as malas. E você?'],
];

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + FILE);
  await page.evaluate(() => document.fonts.ready);
  await page.emulateMedia({ media: 'print' });
  const n = await page.evaluate(({ HOOKS, CROWD }) => {
    const MM = 96 / 25.4;
    let k = 0, filled = 0;
    const free = p => {
      const limit = p.querySelector('.footer').getBoundingClientRect().top - 6 * MM;
      let maxB = p.querySelector('.content').getBoundingClientRect().top;
      p.querySelectorAll('.content > *').forEach(el => { maxB = Math.max(maxB, el.getBoundingClientRect().bottom); });
      return (limit - maxB) / MM;
    };
    for (const p of document.querySelectorAll('.page')) {
      if (!p.querySelector('.footer') || p.classList.contains('nofill')) continue;
      const f = free(p);
      if (f < 24) continue;
      const [lbl, txt] = HOOKS[k++ % HOOKS.length];
      const box = document.createElement('div');
      box.className = 'filler';
      let html = `<div class="lower"><span class="lbl">${lbl}</span><span class="txt">${txt}</span></div>`;
      if (f >= 58) html = `<div class="crowdband">${CROWD}</div>` + html;
      box.innerHTML = html;
      const src = p.querySelector('.content > small.src:last-child');
      src ? p.querySelector('.content').insertBefore(box, src) : p.querySelector('.content').appendChild(box);
      // se ainda sobrar muito, empurra a chamada para o pé da página
      const rest = free(p);
      if (rest > 0) box.style.marginTop = `${Math.min(rest, 60) * 0.5}mm`;
      if (free(p) < 0) box.remove(); else filled++;
    }
    return filled;
  }, { HOOKS, CROWD });
  fs.writeFileSync(FILE, await page.content());
  await browser.close();
  console.log(`Chamadas inseridas: ${n}`);
})();
