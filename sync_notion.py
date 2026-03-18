from notion_client import Client
import os

# 初始化 Notion 客户端
notion = Client(auth=os.environ["NOTION_TOKEN"])

DATABASE_ID = "3271bea0bf2f80e491a2cee8f861025e"

# 调试：打印字段名
items = notion.databases.query(database_id=DATABASE_ID)["results"]

print("========== Notion 字段名列表 ==========")
print(items[0]["properties"].keys())
print("=======================================")

# 退出，不执行后续逻辑
exit()
