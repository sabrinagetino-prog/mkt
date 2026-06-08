# Agente de Análisis de Instagram — Propuesta

## Realidad técnica primero

**Lo que NO puedo hacer desde acá:**
- Conectarme en vivo a la cuenta @fides_tech en este momento (no tengo credenciales ni token de Meta).
- Scrapear el feed público sin riesgo: Instagram bloquea scrapers y viola los ToS — no es un camino sostenible.

**Lo que SÍ es viable:** armarte el agente con la API oficial de Meta (Instagram Graph API), que es gratuita para cuentas de empresa/creator vinculadas a una página de Facebook. Te dejo el diseño completo abajo.

---

## Arquitectura propuesta

```
┌──────────────────────────────────────────────────────────────┐
│  Agente IG Fides                                              │
├──────────────────────────────────────────────────────────────┤
│  1. CONECTOR                                                  │
│     Instagram Graph API (oficial)                             │
│     - Long-lived access token (60 días, renovable)            │
│     - Permisos: instagram_basic, instagram_manage_insights    │
│                                                                │
│  2. INGESTA (cron diaria)                                     │
│     - GET /me/media → últimos 100 posts                       │
│     - GET /{media-id}/insights → reach, impressions, saves,   │
│       shares, comments, plays (reels), avg watch time         │
│     - Almacenar en SQLite o Postgres local                    │
│                                                                │
│  3. ANÁLISIS (semanal)                                        │
│     a. Ranking por engagement rate real                       │
│     b. Clustering por pilar (Concierge / Kit / Embajador)     │
│     c. Detección de hora/día óptimo de publicación            │
│     d. Detección de hashtags con mejor performance            │
│     e. Análisis de copy: largo, tono, presencia de CTA        │
│                                                                │
│  4. TENDENCIAS (semanal)                                      │
│     - Scraping ético: trending audios IG (vía API de terceros │
│       tipo Inflact, Iconosquare, o manual)                    │
│     - Filtro por relevancia a marca (lista de keywords + LLM) │
│                                                                │
│  5. REPORTE (semanal)                                         │
│     - Markdown / PDF con:                                      │
│       · Top 3 posts de la semana y por qué funcionaron        │
│       · Bottom 3 y qué pivotear                                │
│       · 3-5 tendencias activas a las que Fides puede sumarse  │
│       · Recomendaciones de copy y hora para la próxima semana │
└──────────────────────────────────────────────────────────────┘
```

---

## Pasos concretos para ponerlo en marcha

### Paso 1 — Habilitar la cuenta
1. Confirmar que @fides_tech está configurada como **cuenta de empresa** (no personal).
2. Vincularla a una **página de Facebook** (requisito de la API).
3. Crear una app en developers.facebook.com → tipo "Business".
4. Pedir permisos: `instagram_basic`, `instagram_manage_insights`, `pages_show_list`, `pages_read_engagement`.
5. Generar **long-lived token** (60 días) y guardarlo en un `.env`.

### Paso 2 — Decidir hosting
Opciones de menor a mayor esfuerzo:
- **A) Notebook + cron en una laptop:** gratis, frágil. Sirve para arrancar.
- **B) Script en Railway / Render / Fly.io:** ~USD 5/mes, automático.
- **C) Cloud Function (GCP) o Lambda (AWS):** gratis dentro del free tier, más profesional.

Recomendado: **opción B** para arrancar.

### Paso 3 — Stack mínimo
- **Lenguaje:** Python (mejor ecosistema para esto).
- **Librerías:** `requests`, `pandas`, `sqlite3`, `anthropic` (Claude API) o `openai` para el análisis de copy/clustering.
- **Almacenamiento:** SQLite local al principio, migrar a Postgres si crece.
- **Reporte:** Markdown → mandar por email con `resend` o Telegram bot.

### Paso 4 — MVP en 4 archivos
```
agent/
├── ingest.py        # baja datos de IG cada 24hs
├── analyze.py       # corre semanalmente, genera insights
├── report.py        # arma el markdown y lo manda
└── prompts/         # prompts de Claude para clustering y análisis de copy
```

### Paso 5 — Loop semanal de mejora
- Cada lunes: reporte llega al mail.
- Sabrina revisa, marca 1-2 posts que el agente leyó mal.
- Esas correcciones se vuelven few-shot examples para el siguiente análisis.

---

## Qué puedo hacer YA, sin esperar todo eso

Si me pasás:
- **Capturas o exports manuales** de los insights de los últimos 30 posts (alcance, engagement, guardados, compartidos), o
- **Acceso lectura** a la cuenta vía agencia (Meta Business Suite con rol "Analista"), o
- **Lista de posts top y flop** del último trimestre,

…puedo en una conversación armarte:
1. Análisis de qué pilar/formato/copy te está funcionando mejor.
2. Lista de tendencias activas en Argentina que matchean con tu línea editorial.
3. Recalibración del calendario de contenido en base a datos reales.

---

## Tendencias actuales que vale la pena evaluar (junio 2026)

Sin haber visto tus métricas todavía, estas son tendencias de feed argentino que matchean con tu tono "cercano pero profesional":

1. **"POV: el momento en que..."** — formato narrativo en primera persona, funciona muy bien para Concierge (el del portero, la visita, el merodeo).
2. **"Lo que no se ve":** content que muestra el detrás (central de monitoreo, instalación, equipo) — performa fuerte en B2B.
3. **Voice notes / WhatsApp aesthetic:** stories y reels que simulan un audio de mamá/hija. Encajan perfecto en el Kit.
4. **Listas tipo "5 cosas que..."** — sigue funcionando en carruseles, especialmente en LinkedIn/IG para administradores.
5. **Split screen "antes vs después"** — útil para mostrar transición Silver → Gold o vida antes/después del Kit.

Lo que **NO** sumaría a Fides aunque esté trending: bailes virales, audios de comedia stand-up, trends de inseguridad explícita ("entraron a robar y..."), formatos de provocación.

---

## Pregunta para vos

Para avanzar sin que esto quede como una propuesta abstracta, necesito que me digas cuál de estos caminos preferís:

- **(a)** Te armo el repo del agente listo para correr y vos / tu dev pone el token y lo deploya.
- **(b)** Hacemos el análisis "manual asistido" — me pasás los datos exportados y trabajo sobre eso ya mismo.
- **(c)** Solo querías la propuesta para evaluarlo internamente. Lo dejamos acá.
