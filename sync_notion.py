from notion_client import Client
import os

notion = Client(auth=os.environ["NOTION_TOKEN"])
DATABASE_ID = "3271bea0bf2f80e491a2cee8f861025e"

items = notion.databases.query(database_id=DATABASE_ID)["results"]

print("========== Notion 字段结构 ==========")
props = items[0]["properties"]
for key, value in props.items():
    print(f"\n字段名: {key}")
    print("结构:", value)
print("====================================")

exit()
