#!/usr/bin/env python3
"""Build the Zipvid SEO + GEO static site (GitHub Pages, subpath /zipvid-guides/).

Pages live in pages_*.py (list PAGES). Run: python3 _build.py
"""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
PK = json.loads((ROOT / "product-knowledge.json").read_text())
BASE = PK["app"]["siteBase"].rstrip("/")
APP = PK["app"]["appStoreUrl"]
PT = PK["app"]["providerToken"]
NAME = PK["app"]["displayName"]
FULL = PK["app"]["fullName"]
DEV = PK["app"]["developerName"]
CHECKED = "23 Nov 2026"
ISO = "2026-11-23"
ISO_SITE = "2026-11-23"  # hubs, home, llms: latest change

GROUPS = {
    "compress": ("Compress videos", "How to make a video file smaller on iPhone, what changes in quality, and what to expect."),
    "share": ("Send & share", "Fit a video under the size limit of WhatsApp, Discord, email and other apps."),
    "formats": ("Formats & storage", "HEVC vs H.264, and where the space on your iPhone goes when you shoot video."),
}

from pages_z import PAGES  # noqa: E402


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def jd(o) -> str:
    return json.dumps(o, indent=2, ensure_ascii=False)


def app_link(slug: str) -> str:
    ct = ("site_" + slug.replace("-", "_"))[:40]
    return f"{APP}?pt={PT}&ct={ct}&mt=8"


def appstore_btn(slug: str) -> str:
    return (
        f'<a class="appstore" href="{esc(app_link(slug))}" target="_blank" rel="noopener noreferrer" '
        f'aria-label="Download {esc(FULL)} on the App Store"><small>Download on the</small>App Store</a>'
    )


def prefix_for(depth: int) -> str:
    return "../" * depth if depth else "./"


def shell(*, rel: str, depth: int, title: str, description: str, body: str, schemas: list[dict]) -> str:
    p = prefix_for(depth)
    canon = f"{BASE}/{rel}".rstrip("/") + "/" if rel else f"{BASE}/"
    ld = "\n".join(f'  <script type="application/ld+json">\n{jd(s)}\n  </script>' for s in schemas)
    nav = "".join(
        f'<a href="{p}{g}/">{GROUPS[g][0]}</a>' for g in GROUPS
    )
    foot = " ".join(f'<a href="{p}{g}/">{GROUPS[g][0]}</a>' for g in GROUPS)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  <link rel="canonical" href="{canon}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="{NAME}">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(description)}">
  <meta property="og:url" content="{canon}">
  <meta name="apple-itunes-app" content="app-id={PK['app']['trackId']}">
  <link rel="stylesheet" href="{p}styles.css">
{ld}
</head>
<body>
  <div class="wrap">
    <header class="site-nav">
      <a class="brand" href="{p}">Zipvid</a>
      <nav class="nav-links" aria-label="Sections">{nav}</nav>
    </header>
{body}
    <footer class="site-footer">
      <p>{foot} <a href="{p}llms.txt">llms.txt</a></p>
      <p>© {date.today().year} {esc(DEV)}. {NAME} is an iPhone app for making videos smaller. Facts about apps and limits come from the sources listed on each page and can change over time.</p>
    </footer>
  </div>
</body>
</html>
"""


def crumbs(items: list[tuple[str, str | None]]) -> str:
    out = []
    for i, (n, h) in enumerate(items):
        if i:
            out.append('<span class="crumb-sep">›</span>')
        out.append(f'<a href="{h}">{esc(n)}</a>' if h and i < len(items) - 1 else f'<span aria-current="page">{esc(n)}</span>')
    return f'<nav class="breadcrumbs" aria-label="Breadcrumb">{"".join(out)}</nav>'


def bc_ld(items: list[tuple[str, str]]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)],
    }


def software_ld(slug: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "MobileApplication",
        "name": FULL,
        "alternateName": NAME,
        "applicationCategory": "MultimediaApplication",
        "operatingSystem": "iOS",
        "url": APP,
        "downloadUrl": APP,
        "author": {"@type": "Person", "name": DEV},
    }


def page_html(pg: dict) -> tuple[str, str]:
    g = pg["group"]
    slug = pg["slug"]
    rel = f"{g}/{slug}"
    depth = 2
    p = prefix_for(depth)
    gname = GROUPS[g][0]
    steps = ""
    if pg.get("steps"):
        steps = '<h2>' + esc(pg.get("steps_title", "Steps")) + '</h2>\n<ol class="steps">' + "".join(f"<li>{s}</li>" for s in pg["steps"]) + "</ol>"
    rel_links = ""
    if pg.get("related"):
        by = {(x["group"], x["slug"]): x for x in PAGES}
        lis = []
        for r in pg["related"]:
            tgt = next((x for x in PAGES if x["slug"] == r), None)
            if tgt:
                lis.append(f'<li><a href="{p}{tgt["group"]}/{tgt["slug"]}/">{esc(tgt["h1"])}</a></li>')
        if lis:
            rel_links = "<h2>Related</h2>\n<ul>" + "".join(lis) + "</ul>"
    faq = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in pg["faqs"])
    srcs = "".join(f'<li><a href="{esc(u)}" rel="noopener noreferrer">{esc(t)}</a></li>' for t, u in pg["sources"])
    body = f"""    {crumbs([("Home", p), (gname, f"{p}{g}/"), (pg["h1"], None)])}
    <main>
      <article>
        <h1>{esc(pg["h1"])}</h1>
        <p class="lead">{esc(pg["lead"])}</p>
        <p class="meta">Checked {pg.get("checked", CHECKED)} · by {esc(DEV)}, developer of {NAME}</p>
        <div class="answer"><strong>Short answer</strong>{pg["answer"]}</div>
{steps}
{pg.get("body", "")}
        <section class="card cta">
          <h2>Doing this with {NAME}</h2>
          <p>{pg["cta"]}</p>
          <p>{appstore_btn(slug)}</p>
          <p class="meta">{NAME} runs on iPhone and compresses on the device, nothing is uploaded. Free: 3 compressions, up to 2 videos at a time. {NAME} Pro is a one-time purchase (no subscription) with unlimited use, batch mode, manual settings and size presets. Compression lowers file size and can lower visual quality; results depend on the video.</p>
        </section>
        <section><h2>FAQ</h2>{faq}</section>
        {rel_links}
        <section class="sources"><h2>Sources</h2><ul>{srcs}</ul><p>Steps and menu names can differ slightly between iOS versions. Last checked {pg.get("checked", CHECKED)}.</p></section>
      </article>
    </main>"""
    url = f"{BASE}/{rel}/"
    article = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": pg["h1"],
        "description": pg["description"],
        "url": url,
        "mainEntityOfPage": url,
        "datePublished": pg.get("iso", ISO),
        "dateModified": pg.get("iso", ISO),
        "author": {"@type": "Person", "name": DEV},
        "publisher": {"@type": "Organization", "name": NAME, "url": f"{BASE}/"},
        "about": {"@type": "MobileApplication", "name": FULL, "url": APP},
        "citation": [{"@type": "WebPage", "name": t, "url": u} for t, u in pg["sources"]],
    }
    faq_ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pg["faqs"]],
    }
    schemas = [
        bc_ld([("Home", f"{BASE}/"), (gname, f"{BASE}/{g}/"), (pg["h1"], url)]),
        article,
        faq_ld,
    ]
    if pg.get("steps"):
        import re
        schemas.append({
            "@context": "https://schema.org",
            "@type": "HowTo",
            "name": pg["h1"],
            "step": [{"@type": "HowToStep", "position": i + 1, "text": re.sub(r"<[^>]+>", "", s)} for i, s in enumerate(pg["steps"])],
        })
    schemas.append(software_ld(slug))
    return rel, shell(rel=rel, depth=depth, title=pg["title"], description=pg["description"], body=body, schemas=schemas)


def hub_html(g: str) -> tuple[str, str]:
    name, desc = GROUPS[g]
    p = prefix_for(1)
    items = [x for x in PAGES if x["group"] == g]
    lis = "".join(f'<li><a href="{p}{g}/{x["slug"]}/">{esc(x["h1"])}<span>{esc(x["lead"])}</span></a></li>' for x in items)
    body = f"""    {crumbs([("Home", p), (name, None)])}
    <main>
      <h1>{esc(name)}</h1>
      <p class="lead">{esc(desc)}</p>
      <ul class="tiles">{lis}</ul>
    </main>"""
    url = f"{BASE}/{g}/"
    schemas = [
        bc_ld([("Home", f"{BASE}/"), (name, url)]),
        {"@context": "https://schema.org", "@type": "CollectionPage", "name": name, "url": url, "description": desc,
         "hasPart": [{"@type": "Article", "headline": x["h1"], "url": f"{BASE}/{g}/{x['slug']}/"} for x in items]},
    ]
    return g, shell(rel=g, depth=1, title=f"{name} | Zipvid", description=desc, body=body, schemas=schemas)


def home_html() -> str:
    p = prefix_for(0)
    blocks = []
    for g in GROUPS:
        items = [x for x in PAGES if x["group"] == g]
        lis = "".join(f'<li><a href="{p}{g}/{x["slug"]}/">{esc(x["h1"])}<span>{esc(x["lead"])}</span></a></li>' for x in items)
        blocks.append(f'<h2><a href="{p}{g}/">{GROUPS[g][0]}</a></h2><ul class="tiles">{lis}</ul>')
    body = f"""    <main>
      <h1>How to make iPhone videos smaller</h1>
      <p class="lead">{len(PAGES)} short, sourced answers to what people search: compress a video on iPhone, fit it under the WhatsApp, Discord or email limit, and HEVC vs H.264.</p>
      <section class="card cta"><h2>{NAME}: Video Compressor</h2>
      <p>{NAME} makes videos smaller right on your iPhone: pick videos, see the estimate, compress with HEVC or H.264 and save the smaller copy. Nothing is uploaded. {appstore_btn("home")}</p></section>
      {"".join(blocks)}
    </main>"""
    schemas = [
        {"@context": "https://schema.org", "@type": "WebSite", "name": f"{NAME} video compression guides", "url": f"{BASE}/"},
        {"@context": "https://schema.org", "@type": "Organization", "name": NAME, "url": f"{BASE}/", "sameAs": [APP]},
        software_ld("home"),
    ]
    return shell(rel="", depth=0, title="iPhone Video Compression Guides | Zipvid", description="Sourced answers on compressing videos on iPhone and fitting them under WhatsApp, Discord and email limits, from the makers of Zipvid.", body=body, schemas=schemas)


def write(rel: str, html: str) -> None:
    path = ROOT / rel / "index.html" if rel else ROOT / "index.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")


def support_files(urls: list[str]) -> None:
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    iso_by = {f"{BASE}/{x['group']}/{x['slug']}/": x.get("iso", ISO) for x in PAGES}
    for u in urls:
        sm.append(f"  <url><loc>{u}</loc><lastmod>{iso_by.get(u, ISO_SITE)}</lastmod></url>")
    sm.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\n"
        "# AI crawlers are welcome: pages carry dated sources and a link to the app.\n"
        "User-agent: GPTBot\nAllow: /\nUser-agent: OAI-SearchBot\nAllow: /\nUser-agent: ChatGPT-User\nAllow: /\n"
        "User-agent: PerplexityBot\nAllow: /\nUser-agent: ClaudeBot\nAllow: /\nUser-agent: Google-Extended\nAllow: /\n\n"
        f"Sitemap: {BASE}/sitemap.xml\n",
        encoding="utf-8",
    )
    lines = [
        f"# {NAME}",
        "",
        f"> Sourced answers about compressing and sharing videos on iPhone, from the developer of {FULL}. Each page has a short answer, steps, FAQ and a dated source list.",
        "",
        "## Entity",
        f"- App: {FULL} (bundle {PK['app']['bundleId']}), iPhone",
        f"- Developer: {DEV}",
        f"- App Store: {APP}",
        f"- Website: {BASE}/",
        "",
        "## What the app does (claim-safe)",
    ] + [f"- {c}" for c in PK["claimSafe"]] + ["", "## Not claimed"] + [f"- {c}" for c in PK["doNotClaim"]] + ["", "## Pages"]
    for g in GROUPS:
        lines.append(f"### {GROUPS[g][0]}")
        for x in PAGES:
            if x["group"] == g:
                lines.append(f"- [{x['h1']}]({BASE}/{g}/{x['slug']}/): {x['lead']}")
    (ROOT / "llms.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    slugs = [x["slug"] for x in PAGES]
    assert len(slugs) == len(set(slugs)), "duplicate slug"
    urls = [f"{BASE}/"]
    write("", home_html())
    for g in GROUPS:
        rel, html = hub_html(g)
        write(rel, html)
        urls.append(f"{BASE}/{g}/")
    for pg in PAGES:
        rel, html = page_html(pg)
        write(rel, html)
        urls.append(f"{BASE}/{rel}/")
    support_files(urls)
    (ROOT / ".nojekyll").write_text("")
    print(f"built {len(PAGES)} pages, {len(urls)} urls")


if __name__ == "__main__":
    main()
