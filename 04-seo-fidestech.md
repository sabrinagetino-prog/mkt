# SEO — fidestech.com.ar

> **Stack confirmado:** WordPress + Google Site Kit (Search Console + GA4 + PageSpeed + Tag Manager conectados). El sitio devolvió 403 al fetch automatizado — no es un problema (es una protección anti-bot estándar) salvo que también esté bloqueando Googlebot, lo cual chequeamos en el paso 0.
>
> **Datos reales que ya están disponibles vía Site Kit y que pido para afinar este plan:**
> 1. Search Console → Performance → exportar últimos 90 días (queries, pages, CTR, posición).
> 2. Search Console → Coverage → cuántas páginas indexadas vs descubiertas/excluidas.
> 3. GA4 → Acquisition → Organic Search → top landing pages + conversiones.
> 4. PageSpeed Insights → score mobile y desktop de la home + página de Concierge.
> 5. Plugins SEO instalados (Yoast / Rank Math / SEOPress / ninguno).

---

## 1. Keywords objetivo (prioridad alta → baja)

### Concierge (B2B + B2C edificios)
| Keyword | Intención | Volumen estimado | Dificultad |
|---------|-----------|------------------|------------|
| concierge virtual edificio | comercial | medio | media |
| seguridad para edificios argentina | comercial | alto | alta |
| portero virtual edificio | informacional/comercial | medio | media |
| reemplazar encargado edificio | comercial | bajo | baja ⭐ |
| sistema de seguridad para consorcios | comercial | medio | media |
| central de monitoreo edificios | comercial | medio | alta |
| control de accesos edificio CABA | comercial | bajo | baja ⭐ |
| reconocimiento facial edificio | informacional | bajo | media |
| cuanto cuesta encargado vs concierge | comercial | bajo | baja ⭐ |

### Kit Adultos Mayores
| Keyword | Intención | Volumen estimado | Dificultad |
|---------|-----------|------------------|------------|
| cuidar adulto mayor a distancia | informacional | alto | media |
| cerradura inteligente argentina | comercial | alto | alta |
| botón de pánico adultos mayores | comercial | medio | media |
| como cuidar a mis padres que viven lejos | informacional | medio | baja ⭐ |
| tecnología para cuidar adultos mayores | informacional | medio | baja ⭐ |
| cerradura con huella digital casa | comercial | medio | media |
| app para cuidar a mi mama | informacional | bajo | baja ⭐ |

⭐ = oportunidades de quick win (volumen razonable, dificultad baja).

---

## 2. Arquitectura de páginas recomendada

```
/ (home)
├── /concierge
│   ├── /concierge/plan-silver
│   ├── /concierge/plan-gold
│   ├── /concierge/para-administradores
│   ├── /concierge/para-consorcios
│   └── /concierge/cotizar (form)
├── /kit-adultos-mayores
│   ├── /kit-adultos-mayores/como-funciona
│   ├── /kit-adultos-mayores/cerradura-inteligente
│   ├── /kit-adultos-mayores/boton-de-panico
│   └── /kit-adultos-mayores/comprar (form)
├── /casos-de-exito
│   └── /casos/[nombre-edificio]
├── /blog
│   └── /blog/[slug]
├── /sobre-fides
└── /contacto
```

**Por qué:** cada plan (Silver/Gold) y cada componente del kit (cerradura, botón) merece su URL — así apuntás a keywords de cola larga sin pelearte con la home.

---

## 3. On-page — checklist por URL

Para cada página nueva o existente:

- [ ] **Title** (50-60 chars) con keyword principal + marca. Ej: *"Concierge Virtual para Edificios | Fides Tech"*
- [ ] **Meta description** (140-160 chars) con beneficio + CTA. Ej: *"Reemplazá el encargado por un servicio 24/7 que cuida, controla accesos y gestiona tu edificio. Pedí cotización."*
- [ ] **H1 único** que matchee con la intención de la URL (no repetir el title)
- [ ] **H2-H3** estructurados, con variantes de la keyword (LSI)
- [ ] **Slug corto y en castellano** (`/concierge/plan-gold`, no `/services?id=2`)
- [ ] **Alt text en todas las imágenes** (no decorativas) describiendo lo que muestra + contexto
- [ ] **Lazy loading** en imágenes below the fold
- [ ] **Schema.org markup:**
  - `Organization` en home (con sameAs a IG, LinkedIn)
  - `Service` en páginas de plan
  - `Product` en página del kit
  - `FAQPage` en las páginas con preguntas frecuentes
  - `LocalBusiness` si hay oficina física

---

## 4. Técnico — auditoría prioritaria

| Ítem | Cómo verificarlo | Por qué importa |
|------|------------------|-----------------|
| Core Web Vitals (LCP, INP, CLS) | PageSpeed Insights | Factor de ranking confirmado por Google |
| HTTPS y certificado válido | navegador | Confianza + ranking |
| Sitemap XML enviado a Search Console | `/sitemap.xml` | Indexación |
| robots.txt no bloqueando recursos críticos | `/robots.txt` | Crawlability |
| Versión móvil responsive y rápida | PageSpeed Mobile | Mobile-first indexing |
| Hreflang si hay versión en otro idioma | inspector | Multi-idioma |
| 404 customizado con sugerencias | navegar a URL falsa | UX + SEO |
| Redirecciones 301 de URLs viejas (si hubo rediseño) | Screaming Frog | No perder authority |
| Imágenes en WebP/AVIF | DevTools | Velocidad |
| Cache headers correctos | DevTools | Velocidad |
| Bloqueo de bots por WAF | el 403 que vi | Puede estar bloqueando Googlebot también ⚠️ |

⚠️ **Atención prioridad 1:** validar en Search Console que Googlebot no esté siendo bloqueado por el WAF. El 403 que recibí podría estar pasándole a Google también.

---

## 5. Contenidos — calendario de blog (3 meses)

Para apuntar a las keywords informacionales y construir autoridad:

### Mes 1 — Pilares
1. **"¿Concierge virtual o encargado tradicional? Comparativa real para tu edificio"** (apunta a *reemplazar encargado*)
2. **"Cómo cuidar a mis padres que viven en otra ciudad (sin que sientan que los vigilo)"** (apunta a *cuidar adulto mayor a distancia*)
3. **"Cuánto sale poner seguridad en un edificio en CABA en 2026"** (long tail comercial)

### Mes 2 — Educación
4. **"7 cosas que pasan en un edificio y nadie te cuenta"**
5. **"Cerradura inteligente: 5 mitos que tu mamá te va a decir (y cómo responderle)"**
6. **"Reconocimiento facial en edificios: privacidad, ley argentina y cómo lo manejamos"**

### Mes 3 — Casos y autoridad
7. **Caso de éxito: [edificio real, con permiso]**
8. **"Protocolos invisibles: qué hace Concierge cuando vos no te enterás"**
9. **"Guía para administradores: cómo presentarle Concierge a tu consorcio"**

Cada post: 1.200-1.800 palabras, 1 imagen propia mínimo, CTA al form correspondiente, links internos a las páginas de producto.

---

## 6. Off-page — link building viable

1. **Notas en medios del sector:** Reporte Inmobiliario, Real Estate Data, La Nación Propiedades. Pitch: "PropTech argentina que reemplaza al encargado".
2. **Asociaciones:** AIERH (administradores), CAPHI (propietarios). Pedir aparecer como proveedor recomendado.
3. **Partnerships:** Ayres ya está. Buscar 2-3 desarrolladoras más para casos cruzados con backlinks.
4. **Google Business Profile** verificado y optimizado (oficina física, fotos, reseñas).
5. **Directorios verticales:** Cuponstar, Páginas Amarillas, Buenos Negocios, etc. (de bajo valor pero piso necesario).

---

## 7. Stack WordPress recomendado

| Función | Plugin recomendado | Por qué |
|---------|--------------------|---------|
| SEO on-page | **Rank Math** (gratis) o Yoast SEO | Rank Math tiene más features en su versión gratis (schema avanzado, redirecciones, 404 monitor). Si ya usás Yoast, no migres. |
| Cache + performance | **WP Rocket** (paga, ~50 USD/año) o LiteSpeed Cache (gratis si el hosting es LiteSpeed) | Mejora directa de Core Web Vitals. |
| Imágenes | **ShortPixel** o Smush | Conversión automática a WebP, lazy load. |
| Schema avanzado | viene en Rank Math; si usás Yoast, sumar **Schema Pro** | Para Service, Product, FAQPage, LocalBusiness. |
| Redirecciones 301 | **Redirection** (gratis) o el módulo de Rank Math | Cuando reorganices URLs. |
| Backups | **UpdraftPlus** | Antes de tocar nada estructural. |

⚠️ **Antes de instalar nada nuevo:** chequear qué plugins SEO ya están activos. Tener Yoast + Rank Math al mismo tiempo rompe todo.

## 8. Roadmap sugerido — 90 días (revisado con Site Kit)

| Semana | Acción | Herramienta |
|--------|--------|-------------|
| 0 | **Paso cero:** en Search Console → URL Inspection → probar `https://www.fidestech.com.ar/` y confirmar "URL is on Google". Si no, el 403 está afectando a Googlebot y hay que liberar el user-agent en el WAF/hosting. | Site Kit / Search Console |
| 1 | Exportar de Search Console las 50 queries top + 20 páginas top de los últimos 90 días. Análisis de gaps vs keywords objetivo de este doc. | Site Kit |
| 1-2 | Auditoría técnica: PageSpeed (mobile/desktop), Coverage en Search Console, sitemap activo. Instalar/configurar Rank Math si no hay SEO plugin. | Site Kit + Rank Math |
| 3-4 | Reescribir titles, meta descriptions y H1 de páginas existentes (con Rank Math editor). Implementar schema Organization + Service + Product. | Rank Math |
| 5-8 | Crear URLs de plan Silver, plan Gold y subpáginas del kit (templates WP). Redireccionar URLs viejas con plugin Redirection. | WP + Redirection |
| 9-12 | Publicar los primeros 6 posts del blog (CPT "post" estándar). Setear Google Business Profile y primeros directorios. | WP + GBP |
| 13+ | Medir en Site Kit semanal: posición media + clicks orgánicos + conversiones GA4. Iterar contenidos según queries que ya rankean en posición 8-15 (los "quick wins"). | Site Kit |

## 9. Quick wins específicos de Site Kit

Una vez tengamos los datos:

1. **Queries en posición 8-20** = oportunidad inmediata. Optimizar la página existente (mejorar title, sumar contenido, conseguir 1-2 backlinks internos) puede saltarlas al top 5 sin trabajo de cero.
2. **Páginas con CTR <2% y posición top 10** = problema de title/meta description, no de contenido. Reescribir y medir en 30 días.
3. **Páginas con alto bounce en GA4 viniendo de orgánico** = mismatch de intención. Revisar el copy del primer scroll.
4. **Core Web Vitals en rojo en PageSpeed** = arreglar antes que cualquier contenido nuevo. Lo más común en WP: imágenes sin optimizar + tema pesado + falta de cache.

---

## 10. Métricas a trackear (dashboard mensual en Site Kit)

- **Tráfico orgánico mensual** (Search Console + GA4) — meta realista mes 6: 3x vs hoy.
- **Posición media de keywords objetivo** — meta: 5 keywords top 10 en mes 6.
- **CTR en SERP** — meta: >3% promedio.
- **Conversiones del orgánico al form** — meta: >2% del tráfico orgánico llena form. Configurar evento de conversión en GA4 sobre el submit del form.
- **Páginas indexadas** vs creadas — gap = problema técnico.
- **Core Web Vitals** (LCP < 2.5s, INP < 200ms, CLS < 0.1) — Site Kit los muestra directo.
