from notion_client import Client
import os
import re

# ==================== 配置 ====================
notion = Client(auth=os.environ["NOTION_TOKEN"])
DATABASE_ID = "3271bea0bf2f80e491a2cee8f861025e"
OUTPUT_DIR = "notion_export"

def clean_filename(name):
    """清理文件名"""
    name = re.sub(r'[\\/*?:"<>|]', "_", name.strip())
    return name if name else "untitled"

def fetch_database_items():
    """正确分页查询（已确保无 AttributeError）"""
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

def safe_get(props, key, kind=None):
    """安全取值（已适配你的真实字段名）"""
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
    if "title" in prop:
        return "".join([t["plain_text"] for t in prop["title"]])
    return ""

def main():
    print("🚀 开始同步 Notion 数据库...")
    items = fetch_database_items()
    print(f"📊 共获取 {len(items)} 条记录")

    # 1. 清空旧文件（实现删除同步）
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for f in os.listdir(OUTPUT_DIR):
        if f.endswith(".md"):
            os.remove(os.path.join(OUTPUT_DIR, f))

    # 2. 生成新 Markdown
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
        md += f"**子类别:** {sub_cat}\n\n"
        md += f"**学习状态:** {status}\n\n"
        md += f"**优先级:** {priority}\n\n"
        md += f"**学习日期:** {date}\n\n"

        filename = clean_filename(title) + ".md"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(md)
        print(f"✅ 生成 {filename}")

    print("🎉 同步完成！")

if __name__ == "__main__":
    main()
