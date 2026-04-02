Here is the revised Markdown note. I have balanced the content so that core concepts and technical details are in **English**, while the summaries and key warnings are in **Chinese**.

---

# Note: Azure ADLS Gen2 Shared Access Signature (SAS)

## 1. Overview (概览)
A **Shared Access Signature (SAS)** is a signed URI that points to one or more storage resources.
* **核心作用**: 它是 Azure 提供的一种受限访问凭证。允许你在不泄露主密钥（Account Key）的前提下，授权客户端在特定时间内访问特定资源。
* **Mechanism**: It includes a token that contains a set of query parameters defining the constraints of the access.

---

## 2. Three Types of SAS (三种主要类型)
| Type | Description | Use Case |
| :--- | :--- | :--- |
| **User Delegation SAS** | Secured with **Microsoft Entra ID** credentials. | **最推荐使用**。符合企业安全审计要求。 |
| **Service SAS** | Secured with the **Storage Account Key**. | 仅用于单一服务（如 Blob 或 File）。 |
| **Account SAS** | Delegates access to resources in one or more storage services. | 用于跨服务或管理级别的操作。 |

---

## 3. Key Token Parameters (核心参数)
* **`sp` (Permissions)**: Specific actions allowed (e.g., `r` for Read, `w` for Write).
* **`st` & `se` (Validity)**: The **Start** and **Expiry** time for the token.
    * **提示**: 建议遵循“过期即失效”原则，将有效时间设为业务所需的最小值。
* **`spr` (Protocol)**: Restricts access to HTTPS only.
* **`sig` (Signature)**: Used to authenticate the SAS request.



---

## 4. ADLS Gen2 & POSIX ACLs (特殊权限逻辑)
Unlike standard Blob storage, ADLS Gen2 has a hierarchical namespace.
* **Dual Check**: When using a **User Delegation SAS**, Azure checks both the **SAS Token permissions** and the **underlying ACLs** (Access Control Lists) on the folders.
* **中文提醒**: 如果你的 SAS 权限正确但依然报错 403，请检查该目录的 Linux 风格 ACL 权限是否已授予该用户。

---

## 5. Security Best Practices (安全最佳实践)
1. **Never use HTTP**: Always enforce HTTPS to prevent credential interception.
2. **Prefer User Delegation**: 尽量避免使用基于 Account Key 的 SAS，以防止密钥泄露导致全库被黑。
3. **Short-lived Expiry**: Use short expiration times and renew tokens as needed.
4. **IP Restrictions**: Use the `sip` parameter to limit access to known client IP addresses.

---

## 6. Code Snippet (Python Example)
```python
# Create a read-only SAS for a specific file
from azure.storage.filedatalake import generate_file_sas, FileSasPermissions

sas_token = generate_file_sas(
    account_name="mystorage",
    file_system_name="mycontainer",
    file_name="report.pdf",
    account_key="secret_key",
    permission=FileSasPermissions(read=True),
    expiry=datetime.utcnow() + timedelta(hours=2) # 2小时后过期
)
```