import requests

# 上游两个 m3u 文件
urls = [
    "https://raw.githubusercontent.com/mursor1985/LIVE/refs/heads/main/iptv.m3u",
    "https://raw.githubusercontent.com/mursor1985/LIVE/refs/heads/main/bililive.m3u",
]

merged = ["#EXTM3U"]

for url in urls:
    print(f"Fetching {url} ...")
    r = requests.get(url)
    r.raise_for_status()
    lines = r.text.strip().splitlines()
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        if line.startswith("#EXTM3U"):
            continue
        # 跳过 bililive.m3u 的“更新时间频道”
        if "列表更新时间" in line or "time.mp4" in line:
            continue
        merged.append(line)

with open("all.m3u", "w", encoding="utf-8") as f:
    f.write("\n".join(merged))

print("✅ all.m3u generated with", len(merged), "lines")
