<p align="center">
  <img src="assets/banner.svg" alt="Gabriel de Moura Pereira — interfaces, software e automação" width="100%" />
</p>

<h1 align="center">Gabriel de Moura Pereira</h1>
<p align="center"><em>Interfaces web, automação e ferramentas — do fluxo ao código.</em></p>

<p align="center">
  <a href="#projetos">Projetos</a> ·
  <a href="#repositórios-públicos">Repositórios</a> ·
  <a href="#como-trabalho-com-ia">Como uso IA</a> ·
  <a href="#vamos-conversar">Contato</a>
</p>

---

Construo interfaces e sistemas que conectam **UX/UI, desenvolvimento web, automação e inteligência artificial**. Meu foco é transformar uma ideia em experiência clara: organizar o fluxo, desenhar a interface e implementar o que acontece por trás dela.

Trabalho principalmente com **HTML, CSS, JavaScript, React, Python e FastAPI**, e há algum tempo com **Kotlin/Compose** e **MicroPython** nos projetos de automação. Gosto de escopo pequeno, critério de aceite objetivo e código que outra pessoa consegue ler depois.

> Este perfil é um retrato honesto do que existe hoje. Projetos privados aparecem descritos, não publicados; estudos aparecem como estudos. Não há métricas de conversão, depoimentos ou clientes inventados.

## Como sugerir código

Você pode propor uma melhoria de conteúdo, acessibilidade ou código abrindo uma [issue de melhoria](../../issues/new?template=feature_request.yml). A ideia deve apontar o arquivo ou seção afetada e explicar como validar o resultado.

## Estudos interativos

- [morada — protótipo imobiliário](https://tufenor.github.io/portfolio/demos/prototipo-imobiliario/): estudo responsivo com compra e aluguel filtrados separadamente, busca por cidade/bairro, filtros de tipo/preço/quartos, favoritos locais, mapa ilustrativo e detalhes em modal. Marca, imóveis e valores fictícios; sem backend ou envio real. [Código editável](https://github.com/tufenor/portfolio/tree/main/demos/prototipo-imobiliario/).

- [Volta — landing page de elétrica e automação](https://tufenor.github.io/portfolio/demos/voltaria-eletrica/): estudo responsivo com interações locais e conteúdo demonstrativo; sem envio de formulário, WhatsApp ou rastreamento.

- [Auréa — estudo de UX para loja de joias](https://tufenor.github.io/portfolio/demos/atelier-aurora/): catálogo responsivo com busca, filtros, sacola demonstrativa e conteúdo editável. Marca e produtos fictícios; fotografia licenciada; sem checkout, integração Nuvemshop ou resultados de CRO.

- [Catálogo Studio — protótipo de catálogo e-commerce](https://tufenor.github.io/portfolio/demos/catalog-flow/): importação CSV local, edição e revisão de conteúdo e exportação JSON. Marca e dados fictícios; sugestão simulada, sem chamadas de IA ou integração com marketplace.

- [ELOVINZE — estudo de apresentação para moda atacadista](https://tufenor.github.io/portfolio/demos/elovinze-presentation/): conceito independente responsivo, com imagens de referência identificadas, conteúdo editável via `content.js` e cartão digital demonstrativo. Não é site oficial nem projeto contratado; links de produtos/atendimento são locais e não enviam dados. [Código editável](https://github.com/tufenor/portfolio/tree/main/demos/elovinze-presentation/).

## Projetos

### J.A.R.V.I.S. — assistente pessoal para Windows

![JARVIS — esquema conceitual de uma interface conectada a voz, computador e dispositivos](assets/jarvis.svg)

Assistente pessoal em desenvolvimento, com foco em **processamento local**, voz em português e automação controlada do computador. O sistema conecta uma interface de controle, ferramentas do próprio PC, um microcontrolador **ESP32** e um aplicativo companion em **Android**.

| | |
|---|---|
| **Meu trabalho** | Experiência de interação, painel de controle, integrações e diagnóstico |
| **Tecnologias** | Python, FastAPI, Kotlin/Compose, MicroPython |
| **Código** | [tufenor/jarvis](https://github.com/tufenor/jarvis) — núcleo, firmware e app Android |
| **Estágio** | Em desenvolvimento; configuração e credenciais ficam fora do repositório |

O aprendizado que carrego dele: automação de verdade precisa de **limites explícitos**, confirmação antes de ações destrutivas e logs que expliquem o que falhou.

### MoneyIA — mesa de oportunidades e agentes

![MoneyIA — fila de oportunidades, aprovações e evidências](assets/moneyia.svg)

Uma central local para organizar oportunidades, demos, aprovações, agentes e
pendências humanas. O [snapshot público sanitizado do Control Center](moneyia-control-center/)
mostra a arquitetura da fila, o fallback entre provedores e o pacote de
publicação remota com HTTPS. Dados comerciais, e-mails, tokens e estados
financeiros permanecem fora do portfólio.

| | |
|---|---|
| **Meu trabalho** | Orquestração de fila, UX da Mesa, evidência e publicação segura |
| **Tecnologias** | Node.js, HTML/CSS/JavaScript, FastAPI/JARVIS, Caddy |
| **Case** | [Ponte MoneyIA + JARVIS](https://tufenor.github.io/portfolio/case/moneyia-jarvis-bridge-2026-11-26.html) |
| **Estágio** | Mesa local e deploy remoto protegido verificados; envio externo depende de evidência da plataforma |

### Frequency — gestão de academia

![Frequency — esquema conceitual de navegação entre painel, alunos e acessos](assets/frequency.svg)

Sistema de gestão de academia em desenvolvimento, com **API FastAPI**, **PostgreSQL** e interface web em português. Os fluxos cobertos são os de alunos, presenças, planos e administração.

| | |
|---|---|
| **Meu trabalho** | Modelagem de dados, fluxos de gestão e coerência entre telas e API |
| **Tecnologias** | Python, FastAPI, PostgreSQL, HTML/CSS/JavaScript |
| **Código** | [tufenor/frequency](https://github.com/tufenor/frequency) — API, frontend e manual do cliente |
| **Estágio** | Em desenvolvimento; dados de academia e backups ficam fora do repositório |
| **Foco de produto** | Tornar tarefas administrativas compreensíveis na interface, não só funcionais |

Cada funcionalidade tem seu próprio estágio de validação — a apresentação aqui descreve o projeto em construção, não um produto lançado.

### Web — páginas, apresentação e experiência

![Web — esquema conceitual de uma página organizada para computador e celular](assets/web.svg)

Páginas estáticas e estudos de frontend. É onde testei composição, tipografia, responsividade e acessibilidade em projetos pequenos e verificáveis:

| Projeto | O que é | Código |
|---|---|---|
| **MYD-Site** | Site de apresentação para marketing digital, em HTML e CSS | [tufenor/MYD-Site](https://github.com/tufenor/MYD-Site) |
| **Site-Apresentacao** | Site de apresentação com foco mobile, em HTML, CSS e JavaScript | [tufenor/Site-Apresentacao](https://github.com/tufenor/Site-Apresentacao) |
| **Alura-Plus** | Estudo de frontend | [tufenor/Alura-Plus](https://github.com/tufenor/Alura-Plus) |

As ilustrações desta página são **diagramas conceituais**, não capturas das interfaces dos produtos.

Também publiquei um **case do processo**: como montei uma operação de prospecção e entrega com agentes de IA, o que funcionou, o que falhou e o que deliberadamente não automatizei. [Ler o case](https://tufenor.github.io/portfolio/projeto/).

O **Radar global MoneyIA** é um recorte público e sanitizado da etapa de descoberta: normalização de oportunidades, ranking, fila de revisão visual e retomada de verificações humanas. [Ler o case do Radar](https://tufenor.github.io/portfolio/case/moneyia-radar.html). Os números são da execução local em modo sombra; não representam clientes, contratos ou receita.

Também publiquei um recorte da ponte de continuidade entre a Mesa e o JARVIS: fila local, fallback opcional e exigência de evidência antes de marcar um envio como confirmado. [Ler o case da ponte JARVIS](https://tufenor.github.io/portfolio/case/moneyia-jarvis-bridge-2026-11-26.html). O runtime e as credenciais pessoais não fazem parte do case público.

## Repositórios públicos

| Repositório | Linguagem | O que você encontra |
|---|---|---|
| [MYD-Site](https://github.com/tufenor/MYD-Site) | HTML | Site de apresentação para marketing digital |
| [Site-Apresentacao](https://github.com/tufenor/Site-Apresentacao) | JavaScript | Site de apresentação com foco mobile |
| [Alura-Plus](https://github.com/tufenor/Alura-Plus) | HTML | Estudo de frontend |
| [Exercicios-de-treino-js](https://github.com/tufenor/Exercicios-de-treino-js) | HTML | Exercícios de prática em JavaScript |
| [jarvis](https://github.com/tufenor/jarvis) | Python | Núcleo do assistente, firmware ESP32 e app Android |
| [frequency](https://github.com/tufenor/frequency) | Python | Gestão de academia: API FastAPI, frontend React e manual |
| [portfolio](https://github.com/tufenor/portfolio) | HTML | Vitrine e demonstração de correção de responsividade |
| [openclaw-server](https://github.com/tufenor/openclaw-server) | — | Repositório de experimentação; README mínimo |
| [rea](https://github.com/tufenor/rea) | — | Exploração de engenharia reversa com agentes. O projeto original é [REA, de morluto](https://github.com/morluto/rea); consulte a documentação e a autoria de lá |

Os dois projetos têm repositório público com o código-fonte. O que fica de fora é o que não pode ser público: banco de dados, backups, credenciais, configuração de máquina e dados de academia.

## Como trabalho com IA

Uso IA na pesquisa e na implementação, com revisão do resultado. Na prática isso significa:

- leio e testo o que a ferramenta gera, em vez de aceitar a saída como entrega;
- declaro o uso de IA quando o cliente ou a plataforma exige;
- não invento experiência, autoria, depoimento ou resultado de negócio;
- não publico código privado, dados de cliente ou credenciais para "provar" capacidade.

Isso não é modéstia: é o que permite assumir responsabilidade técnica pelo que está no ar.

## O que posso entregar

- **Correção mobile/UX** — uma página, até cinco defeitos acordados, antes/depois e verificação em larguras reais.
- **Landing page de uma oferta** — até seis seções, versão mobile, CTA e código documentado.
- **Automação pontual** — uma entrada, uma transformação e uma saída, com tratamento de falhas e guia de uso.
- **Diagnóstico de instalação** — reproduzir um defeito, corrigir o que está no código e entregar um checklist de instalação limpa.

Trabalho bem com **escopo fechado e critério de aceite escrito**. Projetos maiores entram depois, com marcos separados.

## Vamos conversar

Envie o objetivo do projeto, uma referência e o prazo desejado. A partir disso, organizamos uma primeira entrega com escopo definido.

[LinkedIn](https://linkedin.com/in/tufenor) · [Instagram](https://instagram.com/tufenor) · [TikTok](https://tiktok.com/@tufenor) · [GitHub](https://github.com/tufenor)

---

<details>
<summary><strong>EN — short version</strong></summary>

I build web interfaces and work on automation and AI projects. Most of my work is in HTML/CSS/JavaScript, React, Python and FastAPI, with Kotlin/Compose and MicroPython on the automation side.

I use AI for research and implementation, then review the output. I do not publish private code or client data to build a portfolio, and I do not claim clients, metrics or results that did not happen. The private projects (a Windows personal assistant and an academy management system) are described here, not open-sourced.

Open to small, clearly scoped projects with reviewable deliverables. Please share your goal, references and timeline.

</details>

<details>
<summary><strong>ES — versión corta</strong></summary>

Desarrollo interfaces web y trabajo en proyectos de automatización e IA. Mi stack principal es HTML/CSS/JavaScript, React, Python y FastAPI, con Kotlin/Compose y MicroPython en la parte de automatización.

Uso IA para investigación e implementación, y reviso el resultado. No publico código privado ni datos de clientes para armar el portfolio, y no invento clientes, métricas ni resultados. Los proyectos privados (un asistente personal para Windows y un sistema de gestión de gimnasio) están descritos, no publicados.

Disponible para proyectos pequeños, con alcance y criterios de aceptación claros. Comparte el objetivo, las referencias y el plazo.

</details>
