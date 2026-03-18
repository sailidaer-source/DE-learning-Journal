# DATABRICKS SERIES

## WHAT IS DATABRICKS

Databricks is a **unified analytics and data engineering platform** that lets you process and analyze all kinds of data in one place. It's built on top of Apache Spark but adds many enterprise features, including:

- **Collaborative workspaces** for data engineers, data scientists, and analysts
- **Support for data lakes, data warehouses, and machine learning**
- **Delta Lake technology** for reliability, governance, and speed

## What is Apache Spark?

Apache Spark is:

- An open-source distributed computing engine for processing large datasets.
- Very fast compared to older frameworks like Hadoop MapReduce.
- Can run batch, streaming, SQL, ML, and graph workloads.
- Requires you to manage clusters, storage, integrations, and scaling manually.

## Why Databricks is Different from Just Using Spark

**Spark alone** = fast distributed processing, but you must manage clusters, storage, and integrations manually.

**Databricks** = adds a friendly UI, auto-cluster management, collaborative notebooks, optimized connectors, governance tools, ML lifecycle support, and Delta Lake for reliable data.

It's like the difference between owning a powerful engine vs. a fully built sports car — same power, but one is ready to drive.

## 1. Setup & Infrastructure

**Spark Alone** → You install, configure, and manage your own clusters (on-premise or cloud).

**Databricks** → Fully managed — just click to create clusters, no manual setup.

## 2. Cluster Management

**Spark Alone** → You must manually scale up/down, monitor, and shut down clusters.

**Databricks** → Auto-scaling clusters that start/stop based on workload to save cost. Cluster pools and autoscaling simplify resource management.

## 3. Data Storage

**Spark Alone** → Reads/writes from external storage (S3, HDFS, Azure Blob) but no built-in transactional layer.

**Databricks** → Uses Delta Lake for ACID transactions, schema enforcement, and time travel (versioned data).

## 4. Data Governance & Security

**Spark Alone** → You handle permissions manually at the file system or storage level.

**Databricks** → Unity Catalog (or account-level governance) provides centralized data access control, auditing, and compliance features.

## 5. Collaboration

**Spark Alone** → No built-in multi-user interface — sharing requires exporting scripts or files.

**Databricks** → Collaborative notebooks where multiple users can work together, comment, and share results.

## 6. Workflow Automation

**Spark Alone** → Requires external schedulers (Airflow, cron) for automation.

**Databricks** → Built-in Jobs scheduler with monitoring, retry policies, alerts, and integrations.

## 7. Machine Learning

**Spark Alone** → MLlib for basic ML, but no built-in experiment tracking or deployment tooling.

**Databricks** → MLflow integration for ML lifecycle management (tracking, model registry, deployment).

## 8. Optimization

**Spark Alone** → You manually tune Spark configurations for performance.

**Databricks** → Auto-optimizations (e.g., Photon engine for faster SQL, automatic caching, and query optimizations).

## 9. Integrations

**Spark Alone** → You set up JDBC/ODBC drivers manually for BI tools.

**Databricks** → Native connectors to Power BI, Tableau, Looker, Snowflake, and cloud services make integrations smoother.

## 10. Summary

Databricks packages Spark with enterprise features — collaboration, automation, governance, and optimizations — so teams can move faster with less operational overhead.

---

## What is the Databricks Lakehouse?

The Lakehouse is Databricks' data architecture that combines the best parts of a Data Lake and a Data Warehouse in a single system.

- Data Lake strength → Store all kinds of data (structured, semi-structured, unstructured) cheaply in cloud object storage.
- Data Warehouse strength → Provide fast queries, governance, and reliability.

Databricks Lakehouse merges these into one unified platform using Delta Lake (the "secret sauce").

### Problems It Solves

1. Data Silos

Traditionally, companies needed a Data Lake for raw data + a Data Warehouse for analytics. That meant two systems, constant ETL pipelines, and duplicate data.

- Lakehouse = one platform, no silos.

2. Reliability Issues in Data Lakes

Normal data lakes (S3, ADLS, GCS) don't support:

- ACID transactions
- Schema enforcement
- Version control

This caused corrupted tables and inconsistent data.

- Lakehouse (via Delta Lake) adds ACID transactions + schema validation + time travel.

3. Scalability & Cost

Data warehouses are fast but expensive and limited to structured data. Data lakes are cheap and scalable but can be slow and unreliable.

- Lakehouse keeps data in cheap cloud storage (like a lake) but allows fast SQL queries (like a warehouse).

### How It Works Internally

**Data Storage**

Data is stored in cloud object storage (S3, ADLS, GCS) in open formats (Parquet, JSON, Avro, ORC).

**Delta Lake Layer (the magic)**

- Adds a transaction log (_delta_log) on top of files.
- Tracks every write/update/delete.
- Ensures ACID transactions (no partial writes).
- Provides schema enforcement and schema evolution.
- Enables time travel (query old versions of data).

**Query & Compute Layer**

- Use Spark, SQL, Python, R, Scala, or Java to process data.
- Optimized with Photon engine for faster SQL queries.
- Supports batch, streaming, ML, and BI workloads.
- Governance & Security via Unity Catalog: manages data access, metadata, and lineage.

### Advantages of the Databricks Lakehouse

- ✅ Unified Platform — No need for both a lake + warehouse; everything is in one place.
- ✅ Open Data Format — Data stays in open formats (Parquet/Delta), avoiding vendor lock-in.
- ✅ ACID Transactions — Reliable data like a database.
- ✅ Time Travel — Query historical data versions.
- ✅ Performance — Indexing, caching, and Photon engine make queries super fast.
- ✅ Cost-Efficient — Store on cheap cloud object storage but query like a warehouse.
- ✅ Supports All Workloads — BI dashboards, ML training, real-time streaming, batch ETL.
- ✅ Scalable & Elastic — Auto-scales with cloud compute.


# Azure Cluster Study Notes

## 1. What is a Cluster?
- **Cluster**: A group of nodes (computing units) working together to process tasks in parallel.
- **Node**: A single computing unit (VM or container).
- **Driver / Control Plane**: The “leader” that schedules and manages tasks
- **Worker Node**: Executes the actual computations.

👉 Analogy: If you have 100 assignments, you form a team of 10 people.  
- The team = Cluster  
- Each person = Node  
- The leader who distributes tasks = Driver/Control Plane  

---

## 2. Why Compute = Cluster
- In **Azure Databricks**, the term **Compute** refers to the computing resources used to run workloads.
- These resources are organized as a **Cluster** (Driver + Workers).
- Therefore, **Compute and Cluster are often interchangeable terms** in Databricks.

---

## 3. Classic Compute vs. Serverless Compute

### Classic Compute
- You create and manage the cluster manually.
- You decide the number of nodes, their type, and scaling rules.
- You must start and stop the cluster yourself.
- Best for long-running jobs or when you need fine-grained control.

👉 Analogy: You personally recruit 10 classmates, assign them tasks, and dismiss them afterward.

### Serverless Compute
- Azure automatically provisions and manages the cluster for you.
- You only submit the job; the system handles the rest.
- Ideal for quick experiments or temporary workloads.
- Saves time and reduces management overhead.

👉 Analogy: You simply say “I have 100 assignments,” and the system automatically finds people, distributes tasks, and collects results.

---

## 4. Key Takeaways
- **Cluster = Team**, **Node = Member**.
- **Compute = Cluster**, since compute resources are delivered as clusters.
- **Classic vs. Serverless**: The difference lies in **who manages the team** (you vs. the system).

---

## 5. Glossary (English–Chinese)
| English Term       | Chinese Term       | Meaning |
|--------------------|--------------------|---------|
| Cluster            | 集群               | Group of nodes working together |
| Node               | 节点               | Single computing unit |
| Compute            | 计算资源           | Resources used to run workloads |
| Classic Compute    | 传统计算           | User-managed cluster |
| Serverless Compute | 无服务器计算       | System-managed cluster |

---

## 6. Suggested Learning Path
1. Understand the basic structure of a cluster (Driver + Workers).
2. Learn why Compute = Cluster in Databricks.
3. Compare Classic vs. Serverless Compute and their use cases.
4. Practice by creating a small Classic Cluster in Databricks, then try Serverless Compute.



(End of Databricks Day 1 continuation).
