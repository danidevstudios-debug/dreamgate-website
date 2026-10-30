#!/usr/bin/env python3
"""Build the DreamGate developer site from apps.json.

Usage: python3 build.py
Reads apps.json + template.html, writes index.html (fully self-contained:
the app data is embedded, so the page works from any static host and as a
single-file demo). Re-run after every apps.json change, then redeploy.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).parent
data = json.loads((HERE / "apps.json").read_text())
template = (HERE / "template.html").read_text()
assert "__APPS_JSON__" in template, "template placeholder missing"
out = template.replace("__APPS_JSON__", json.dumps(data))
(HERE / "index.html").write_text(out)
print(f"Built index.html with {len(data['apps'])} apps.")
