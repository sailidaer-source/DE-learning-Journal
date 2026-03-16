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
