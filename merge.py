import requests

# 上游两个 m3u 文件
urls = [
    "https://raw.githubusercontent.com/mursor1985/LIVE/refs/heads/main/iptv.m3u",
    "https://raw.githubusercontent.com/mursor1985/LIVE/refs/heads/main/bililive.m3u",
    "https://raw.githubusercontent.com/mursor1985/LIVE/refs/heads/main/douyuyqk.m3u",
    "https://raw.githubusercontent.com/mursor1985/LIVE/refs/heads/main/huyayqk.m3u",
    "https://raw.githubusercontent.com/mursor1985/LIVE/refs/heads/main/yylunbo.m3u",
]

merged = ["#EXTM3U"]

for url in urls:
    print(f"Fetching {url} ...")
    r = requests.get(url)
    r.raise_for_status()
    lines = r.text.strip().splitlines()
    print(f"Fetched {len(lines)} lines from {url}")
    for line in lines:
        if not line.strip():
            continue
        if line.startswith("#EXTM3U"):
            continue
        # 跳过 bililive.m3u 的“列表更新时间”频道
        if "列表更新时间" in line or "time.mp4" in line:
            continue
        merged.append(line)

output_file = "all.m3u8"
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(merged))

print(f"✅ {output_file} generated with {len(merged)} lines")
