import os
import re
import requests

# ==================== 配置 ====================
NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DATABASE_ID = "3271bea0bf2f80e491a2cee8f861025e"
OUTPUT_DIR = "notion_export"
NOTION_VERSION = "2022-06-28"   # 官方稳定版本

HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": NOTION_VERSION,
    "Content-Type": "application/json"
}

def clean_filename(name: str) -> str:
    name = re.sub(r'[\\/*?:"<>|]', "_", name.strip())
    return name if name else "untitled"

def fetch_all_pages():
    """使用官方 REST API 查询（彻底解决 AttributeError）"""
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    pages = []
    cursor = None
    while True:
        payload = {"start_cursor": cursor} if cursor else {}
        resp = requests.post(url, headers=HEADERS, json=payload)
        resp.raise_for_status()
        data = resp.json()
        pages.extend(data["results"])
        if not data.get("has_more"):
            break
        cursor = data.get("next_cursor")
    return pages

def safe_get(props: dict, key: str, kind: str = None):
    if key not in props:
        return ""
    prop = props[key]
    if kind == "multi_select":
        return ", ".join([t["name"] for t in prop.get("multi_select", [])])
    if kind == "select":
        return prop.get("select", {}).get("name", "")
    if kind == "status":
        return prop.get("status", {}).get("name", "")
    if kind == "date":
        return prop.get("date", {}).get("start", "")
    if prop.get("title"):
        return "".join([t.get("plain_text", "") for t in prop["title"]])
    return ""

def main():
    print("🚀 开始同步 Notion 数据库（使用官方 API）...")
    items = fetch_all_pages()
    print(f"📊 共获取 {len(items)} 条记录")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for f in os.listdir(OUTPUT_DIR):
        if f.endswith(".md"):
            os.remove(os.path.join(OUTPUT_DIR, f))

    for item in items:
        props = item["properties"]
        title = safe_get(props, "笔记标题")
        main_cat = safe_get(props, "主类别", "multi_select")
        sub_cat = safe_get(props, "子类别", "multi_select")
        status = safe_get(props, "学习状态", "status")
        priority = safe_get(props, "优先级", "select")
        date = safe_get(props, "学习日期", "date")

        md = f"# {title}\n\n"
        md += f"**主类别:** {main_cat}\n\n"
        md += f"**子类别:**
