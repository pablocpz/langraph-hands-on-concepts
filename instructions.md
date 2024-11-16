### Setting up Python, `agents_env` and `env` file

---

Ensure you install Python `3.11.9`
https://www.python.org/downloads/release/python-3119/


#### **Step 1: Navigate to the Root Directory**
1. Open your terminal or command prompt.
2. Navigate to the root directory where you want to clone the repo:
   ```bash
   git clone https://github.com/pablocpz/langraph-hands-on-concepts.git

   cd langraph-hands-on-concepts
   ```

---

#### **Step 2: Create or Update the `.env` File**

Create a `.env` file inside the root dir to store the API keys

Then, store these variables:
```bash
OPENAI_API_KEY='<key goes here>'
TAVILY_API_KEY="<key goes here>"
```

---

#### **Step 3: Activate `agents_env`**
To load the `.env` variables into your environment:

- **Windows (Cmd)**:
  ```bash
  .\agents_env\Scripts\Activate

  ```

- **Mac/Linux**:
  ```bash
  source ./agents_env/bin/activate
  ```


In order to deactive the environment, simply run `deactivate`
---
