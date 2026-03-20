
# 📘 Accessing Azure Data Lake Storage Gen2 — Overview (Study Notes)

## 1. Why Authentication Is Needed
Databricks cannot directly access Azure Data Lake Storage Gen2 (ADLS Gen2).
To read or write data, Databricks must **authenticate** itself to Azure.

Every access method is essentially answering the question:

> **“Who are you, and do you have permission to access this storage?”** 

---

## 2. Authentication Methods in Databricks

Azure Databricks supports **five major authentication patterns** for accessing ADLS Gen2.

### 2.1 Access Key
- Each storage account has a **primary access key**.
- Works like a “master password” for the entire storage account.
- Simple but **not secure**.
- Suitable only for learning or testing.

---

### 2.2 SAS Token (Shared Access Signature)
- A **temporary** and **more granular** access token.
- Can limit:
  - Permissions (read/write/list)
  - Expiration time
  - Specific containers or paths
- More secure than Access Key, but still not ideal for production.

---

### 2.3 Service Principal (SP)
- A **dedicated application identity** created in Azure AD.
- You assign permissions to this identity using **IAM roles**.
- Databricks uses the SP’s credentials to access ADLS.
- **Most common method in enterprise production environments.**

---

### 2.4 AAD Passthrough Authentication
- Databricks uses the **user’s own Azure AD identity**.
- Access is granted only if the user has permissions in ADLS IAM.
- Ensures fine‑grained, user‑level security.
- **Only available in Premium Databricks workspaces.**

---

### 2.5 Unity Catalog (Newest Method)
- Databricks’ centralized governance and permission system.
- Access is controlled through **Unity Catalog permissions**, not Azure IAM.
- Databricks checks the user’s UC privileges before accessing ADLS.
- Also requires Premium workspace.
- Becoming the **modern standard** for data governance.

---

## 3. Session Scoped vs Cluster Scoped Authentication

Authentication can be applied at two different scopes:

### 3.1 Session Scoped Authentication
- Credentials are set **inside a notebook**.
- Valid only while the notebook is attached to a cluster.
- Ends when the session ends.
- Good for:
  - Learning
  - Testing
  - Temporary access

Example:
```python
spark.conf.set("fs.azure.account.key.<storage>.dfs.core.windows.net", "<key>")
```

---

### 3.2 Cluster Scoped Authentication
- Credentials are configured **on the cluster itself**.
- Authentication happens when the cluster starts.
- All notebooks attached to the cluster inherit the access.
- Good for:
  - Production workloads
  - Shared clusters
  - Scheduled jobs

---

## 4. What You Will Learn in This Course Section

The course will walk through each authentication method:

1. **Access Key** (session scoped)
2. **SAS Token** (session scoped)
3. **Service Principal** (session scoped)
4. **Service Principal** (cluster scoped)
5. **AAD Passthrough** (Premium only)
6. **Recommended method** based on your subscription type

Unity Catalog is mentioned but not covered in detail, because:
- It requires Premium workspace
- It is usually configured by administrators

---

## 5. Key Takeaways

- Databricks needs authentication to access ADLS Gen2.
- There are **five** main authentication patterns.
- **Session scoped** = set in notebook, temporary.  
- **Cluster scoped** = set in cluster, persistent.
- **Service Principal** and **Unity Catalog** are the most common in real companies.
- Student subscriptions may not support Service Principals.

---

