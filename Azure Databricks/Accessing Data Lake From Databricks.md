# Accessing Azure Data Lake with Access Keys

## Concept
- Each Azure Storage Account has **two access keys** (primary and secondary).
- These keys act like a **password** to authenticate requests.
- In Databricks, you configure Spark with the key before accessing data.

## Steps

1. **Get the Access Key**
   - Go to **Azure Portal → Storage Account → Security + Networking → Access keys**.
   - Copy either the primary or secondary key.

2. **Set Spark Configuration**
   - In your Databricks notebook, run:
   ```python
   spark.conf.set(
       "fs.azure.account.key.<storage-account>.dfs.core.windows.net",
       "<your-access-key>"
   )
