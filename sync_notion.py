from notion_client import Client
import os
import re

# 初始化 Notion 客户端
notion = Client(auth=os.environ["NOTION_TOKEN"])

# 你的 Database ID
DATABASE_ID = "3271bea0bf2f80e491a2cee8f861025e"

# 清理文件名（去掉非法字符）
def clean_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "_", name)

# 查询数据库所有记录
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

# 提取文本字段
def get_text(prop):
    if "title" in prop:
        return "".join([t["plain_text"] for t in prop["title"]])
    if "rich_text" in prop:
        return "".join([t["plain_text"] for t in prop["rich_text"]])
    return ""

# 生成 Markdown 文件
def generate_markdown(item):
    props = item["properties"]

    title = get_text(props["Title"])
    main_cat = ", ".join([t["name"] for t in props["Main Category"]["multi_select"]])
    sub_cat = ", ".join([t["name"] for t in props["Subcategory"]["multi_select"]])
    status = props["Learning Status"]["status"]["name"] if props["Learning Status"]["status"] else ""
    priority = props["Priority"]["select"]["name"] if props["Priority"]["select"] else ""
    date = props["Learning Date"]["date"]["start"] if props["Learning Date"]["date"] else ""

    md = f"# {title}\n\n"
    md += f"**Main Category:** {main_cat}\n\n"
    md += f"**Subcategory:** {sub_cat}\n\n"
    md += f"**Learning Status:** {status}\n\n"
    md += f"**Priority:** {priority}\n\n"
    md += f"**Learning Date:** {date}\n\n"

    return title, md

# 主流程
items = fetch_database_items()

output_dir = "notion_export"
os.makedirs(output_dir, exist_ok=True)

for item in items:
    title, md = generate_markdown(item)
    filename = clean_filename(title) + ".md"

    with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
        f.write(md)

print("Notion database exported successfully!")
