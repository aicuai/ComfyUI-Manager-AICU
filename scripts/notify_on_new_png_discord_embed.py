# notify_on_new_png_discord_embed.py
import time
import os
import requests
import urllib.parse

WATCH_DIR = "/home/user/opt/ComfyUI/output"
DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")
BASE_URL = "https://comfyui.aicu.jp/api/view"

def build_image_url(filename):
    params = {
        "filename": filename,
        "subfolder": "",
        "type": "output",
        "rand": str(time.time())  # キャッシュバイパス用
    }
    return f"{BASE_URL}?{urllib.parse.urlencode(params)}"

def notify_discord(filename):
    image_url = build_image_url(filename)
    payload = {
        "embeds": [
            {
                "title": "🖼️ 新しい画像が生成されました",
                "description": f"`{filename}`",
                "image": {"url": image_url},
                "url": image_url
            }
        ]
    }
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        response.raise_for_status()
        print(f"✅ 通知送信: {filename}")
    except Exception as e:
        print(f"❌ Discord通知に失敗: {e}")

def main():
    print(f"📂 {WATCH_DIR} を監視中（Discord通知）...")
    seen_files = set(os.listdir(WATCH_DIR))

    while True:
        time.sleep(5)
        current_files = set(os.listdir(WATCH_DIR))
        new_files = [f for f in current_files - seen_files if f.endswith(".png")]
        for f in sorted(new_files):  # ソートして順番を維持
            notify_discord(f)
        seen_files = current_files

if __name__ == "__main__":
    main()
