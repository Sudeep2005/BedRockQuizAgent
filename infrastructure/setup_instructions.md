# 🧠 Bedrock QuizRunner Agent — Setup Instructions

This document provides step-by-step instructions to set up and deploy the **AWS Bedrock QuizRunner Agent** using **Python 3.13** and **Astra DB** for RAG (Retrieval-Augmented Generation).  
The system generates intelligent multiple-choice quizzes from contextual documents stored in Astra DB.

---

## 🚀 1. Prerequisites

Before you begin, make sure you have the following installed and configured:

| Tool | Description | Link |
|------|--------------|------|
| 🐍 Python 3.13 | Required runtime for the Lambda function | [Download](https://www.python.org/downloads/) |
| 💻 AWS CLI | Used for deployment to Lambda | [AWS CLI Setup Guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) |
| 🧰 Git | Version control for repository setup | [Install Git](https://git-scm.com/downloads) |
| 🧱 Astra DB Account | Database for RAG context | [Datastax Astra DB](https://www.datastax.com/astra-db) |
| ☁️ AWS Account with Bedrock Access | For deploying the agent and Lambda function | — |

---

## 📂 2. Clone the Repository

```bash
git clone https://github.com/Sudeep2005/bedrock-quizrunner-agent.git
cd bedrock-quizrunner-agent
