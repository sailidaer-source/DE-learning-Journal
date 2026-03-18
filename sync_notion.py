from notion_client import Client
import os
import re

notion = Client(auth=os.environ["NOTION_TOKEN"])
DATABASE_ID = "3271bea0bf2f80e491a2cee8f861025e"

def clean_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "_", name)

def fetch_database_items():
    results = []
    next_cursor = None
    while True:
        response = notion.databases.query(
            database_id=DATABASE_ID,
            start_cursor=next_cursor
        )
        results.extend(response["results"])
        next_cursor = response.get("next_cursor")
        if not next_cursor:
            break
    return results

def get_text(prop):
    if "title" in prop:
        return "".join([t["plain_text"] for t in prop["title"]])
    if "rich_text" in prop:
        return "".join([t["plain_text"] for t in prop["rich_text"]])
    return ""

def safe_get(props, key, kind=None):
    """安全获取字段，避免 KeyError"""
    if key not in props:
        return ""
    if kind == "multi_select":
        return ", ".join([t["name"] for t in props[key]["multi_select"]])
    if kind == "select":
        return props[key]["select"]["name"] if props[key]["select"] else ""
    if kind == "status":
        return props[key]["status"]["name"] if props[key]["status"] else ""
    if kind == "date":
        return props[key]["date"]["start"] if props[key]["date"] else ""
    return get_text(props[key])

def generate_markdown(item):
    props = item["properties"]

    title = safe_get(props, "笔记链接")
    main_cat = safe_get(props, "主类别", "multi_select")
    sub_cat = safe_get(props, "子类别", "multi_select")
    status = safe_get(props, "学习状态", "status")
    priority = safe_get(props, "优先级", "select")
    date = safe_get(props, "学习日期", "date")

    md = f"# {title}\n\n"
    md += f"**主类别:** {main_cat}\n\n"
    md += f"**子类别:** {sub_cat}\n\n"
    md += f"**学习状态:** {status}\n\n"
    md += f"**优先级:** {priority}\n\n"
    md += f"**学习日期:** {date}\n\n"

    return title, md

items = fetch_database_items()
output_dir = "notion_export"
os.makedirs(output_dir, exist_ok=True)

for item in items:
    title, md = generate_markdown(item)
    filename = clean_filename(title) + ".md"
    with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
        f.write(md)

print("Notion database exported successfully!")
