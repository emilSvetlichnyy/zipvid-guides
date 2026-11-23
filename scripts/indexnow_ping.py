#!/usr/bin/env python3
"""Ping IndexNow (Bing, Yandex, etc.) with every URL from sitemap.xml."""
import json, re, urllib.request, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOST = "emilsvetlichnyy.app"
BASE = f"https://{HOST}/zipvid-guides"
KEY = (ROOT / "indexnow-key.txt").read_text().strip()
urls = re.findall(r"<loc>(.*?)</loc>", (ROOT / "sitemap.xml").read_text())
payload = {"host": HOST, "key": KEY, "keyLocation": f"{BASE}/{KEY}.txt", "urlList": urls}
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=json.dumps(payload).encode(),
                             headers={"Content-Type": "application/json; charset=utf-8"}, method="POST")
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        print(f"IndexNow HTTP {r.status} ({len(urls)} URLs)")
except urllib.error.HTTPError as e:
    print(f"IndexNow HTTPError {e.code}: {e.read()[:300]}"); raise SystemExit(1)
