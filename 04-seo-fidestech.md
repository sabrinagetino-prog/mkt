# SEO — fidestech.com.ar

> **Nota metodológica:** el sitio devolvió HTTP 403 al fetch automatizado (probable bloqueo de bots o CDN). Recomiendo dar acceso a Google Search Console + Screaming Frog para auditoría profunda. Lo que sigue es el roadmap basado en mejores prácticas del rubro (PropTech / seguridad residencial Argentina) y en lo que sé del producto.

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

## 7. Roadmap sugerido — 90 días

| Semana | Acción |
|--------|--------|
| 1-2 | Auditoría técnica con acceso (Search Console + Screaming Frog). Resolver el 403 si afecta a Googlebot. |
| 3-4 | Reescribir titles, meta descriptions y H1 de páginas existentes. Implementar schema básico. |
| 5-8 | Crear URLs de plan Silver, plan Gold y subpáginas del kit. Migrar contenido y redireccionar viejas si hace falta. |
| 9-12 | Publicar los primeros 6 posts del blog. Setear Google Business Profile y primeros directorios. |
| 13+ | Medir, iterar, salir a buscar backlinks de medios. |

---

## 8. Métricas a trackear

- **Tráfico orgánico mensual** (Search Console + GA4) — meta realista mes 6: 3x vs hoy.
- **Posición media de keywords objetivo** — meta: 5 keywords top 10 en mes 6.
- **CTR en SERP** — meta: >3% promedio.
- **Conversiones del orgánico al form** — meta: >2% del tráfico orgánico llena form.
- **Páginas indexadas** vs creadas — gap = problema técnico.
