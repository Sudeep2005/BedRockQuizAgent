# 🧠 Bedrock QuizRunner Agent

> **Serverless RAG-powered Quiz Generator** built using **AWS Bedrock Agents**, **Astra DB**, and **AWS Lambda (Python 3.13)** — no-code/low-code approach.

![Architecture](./screenshots/architecture-diagram.png)

---

## 🚀 Overview

**Bedrock QuizRunner Agent** is an intelligent quiz-generation system powered by **Amazon Bedrock Agents** and **Astra DB** vector store.
It uses **RAG (Retrieval-Augmented Generation)** to dynamically create MCQs from your proprietary data, enabling adaptive learning or knowledge assessment apps — all within the AWS ecosystem.

This project demonstrates:

* Creating **Bedrock Agents** using the *no-code console interface*.
* Extending Bedrock Agents using **AWS Lambda functions**.
* Integrating with **Astra DB** for external RAG data retrieval.
* A fully serverless architecture — no backend servers needed.

---

## 🧩 Architecture

```
User
 │
 ▼
Bedrock Agent  ─────────────┐
 │                         │
 │                         ▼
 │                    AWS Lambda  (Python 3.13)
 │                         │
 ▼                         ▼
LLM (Claude 3.5 Sonnet) ← Astra DB Vector Store
```

Key Features:

* ⚡ **Low-code** agent creation with AWS Bedrock Agent Builder.
* 🧠 **Custom knowledge integration** using Astra DB via Lambda.
* 🧩 **Action Groups** connecting external APIs.
* 🔒 **IAM Guardrails** & environment-secure credentials.
* 🧾 **Dynamic RAG** using vector search retrieval.

---

## 🧰 Tech Stack

| Component      | Technology                           |
| -------------- | ------------------------------------ |
| Agent Platform | **Amazon Bedrock**                   |
| Language Model | Claude 3.5 Sonnet (Anthropic)        |
| Vector Store   | **Astra DB**                         |
| Runtime        | **AWS Lambda (Python 3.13)**         |
| Infrastructure | AWS Console (no-code setup)          |
| Storage        | Amazon S3 (Knowledge Base)           |
| Auth & Access  | IAM Roles, Bedrock Agent Permissions |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone this Repository

```bash
git clone https://github.com/Sudeep2005/bedrock-quizrunner-agent.git
cd bedrock-quizrunner-agent
```

### 2️⃣ Project Structure

```
BedRockQuizAgent/
│
├── lambda/
│   ├── handler.py
│   ├── utils/
│   │   └── astra_client.py
│   └── tests/
│       └── test_lambda.py
│
├── agent/
│   ├── config/
│   │   └── agent_instructions.yaml
│   └── schemas/
│       └── openapi.yaml
│
├── infrastructure/
│   ├── permissions.json
│   ├── policy-template.yaml
│   └── deployment-guide.md
│
├── screenshots/
│   ├── architecture-diagram.png
│   ├── bedrock-agent-ui.png
│   └── lambda-config.png
│
└── README.md
```

### 3️⃣ AWS Bedrock Agent Setup (No Code)

1. Open **Amazon Bedrock Console** → Agents → **Create Agent**.
2. Select **Claude 3.5 Sonnet v2** model.
3. Paste custom **agent instructions**:

   ```text
   You are an AI Quiz Generator. Based on given context, create MCQs with 4 options.
   Each question should be contextually relevant and answerable from provided data.
   ```
4. Prepare and test your agent.

### 4️⃣ Create AWS Lambda Function

* Runtime: `Python 3.13`
* Handler: `lambda_function.lambda_handler`
* Attach the following environment variables:

  ```
  ASTRA_ENDPOINT=https://<astra-db-endpoint>
  ASTRA_TOKEN=<astra-db-token>
  ASTRA_KEYSPACE=quiz_keyspace
  ASTRA_COLLECTION=quiz_context
  ```

Deploy your code:

```bash
zip -r function.zip .
aws lambda update-function-code --function-name quiz-runner --zip-file fileb://function.zip
```

### 5️⃣ Attach Lambda to Bedrock Agent

* In **Bedrock Agent Console → Action Groups → Add Action Group**
* Choose **Existing Lambda function**.
* Upload **OpenAPI schema** (from `agent/schemas/openapi.yaml`).
* Save and **Prepare Agent** again.

### 6️⃣ Grant Permissions

Use the Agent ARN to grant Bedrock invoke permissions:

```bash
aws lambda add-permission \
  --function-name quiz-runner \
  --principal bedrock.amazonaws.com \
  --statement-id AllowBedrockInvoke \
  --action lambda:InvokeFunction \
  --source-arn arn:aws:bedrock:region:account-id:agent/agent-id
```

---

## 🧪 Testing

1. Go to **Bedrock Agent “Test” tab**.
2. Query:

   ```
   Generate 5 MCQs on “AI Ethics” from available knowledge.
   ```
3. The agent will:

   * Fetch context from Astra DB via Lambda.
   * Generate high-quality MCQs using Claude 3.5 Sonnet.
   * Return JSON/markdown output.

---

## 🧱 Infrastructure (Optional: IaC)

To automate setup, use the provided **CloudFormation Template** in `infrastructure/policy-template.yaml` to deploy:

* IAM roles
* Lambda environment
* Permissions for Bedrock Agent

---

## 📸 Screenshots

| Step                  | Screenshot                                              |
| --------------------- | ------------------------------------------------------- |
| Architecture Overview | ![Architecture](./screenshots/architecture-diagram.png) |
| Bedrock Agent Builder | ![Agent Builder](./screenshots/bedrock-agent-ui.png)    |
| Lambda Setup          | ![Lambda Config](./screenshots/lambda-config.png)       |

---

## 🧭 Future Enhancements

* [ ] Bedrock Knowledge Base Integration
* [ ] Support for OpenSearch Vector Store
* [ ] Add Multi-Agent Collaboration
* [ ] Stream responses via Bedrock Agent Runtime SDK

---

## 🧑‍💻 Author

**Sumita’s AI Lab**
📧 Contact: [[your.email@example.com](mailto:your.email@example.com)]
🌐 GitHub: [github.com/your-username](https://github.com/your-username)
💬 LinkedIn: [linkedin.com/in/your-profile](https://linkedin.com/in/your-profile)

---

## 🪪 License

MIT License © 2025 Sumita’s AI Lab
See [`LICENSE`](./LICENSE) for details.

---

Would you like me to:

1. 🧾 Auto-generate this `README.md` file inside your local `C:\Projects\BedRockQuizAgent` folder (PowerShell command version)?
2. Or 📁 include placeholder sample screenshots & the folder setup command too (for direct copy-paste into VS Code)?
