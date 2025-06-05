
# 🤝 LinkUp: Peer & Mentor Matching Using Agno AI Agents

**LinkUp** is an AI-powered command-line application that connects students with:

- 🔗 Peers sharing similar academic **interests**, **goals**, or **struggles**
- 🧑‍🏫 Suitable **senior mentors** from the same or related branches

It uses the [Agno Agent Framework](https://docs.agno.com/introduction) to build modular, reusable agents and the `typer` library for a seamless CLI experience.

---

## 📚 What is Agno?

> **Agno** is a Python-based framework that helps you create composable, intelligent agents for different applications such as CLI tools, APIs, and web apps.

Each agent is just a class with a `run()` method — simple, clean, and powerful.

📖 **Docs**: [Agno Docs](https://docs.agno.com/introduction)

---

## ✨ Features

- 🔍 Match students with similar **academic interests** or **mental health concerns**
- 🧑‍🏫 Suggest suitable **senior mentors** based on branch, year, and academic goals
- 💡 Easily extensible: Add more agents or enhance behavior
- ⚙️ Built with Agno agents and Typer CLI

---

## 🏗️ Project Structure

```

LinkUp/
├── agents/
│   ├── match\_finder\_agent.py           # Agent for peer matching
│   ├── mentor\_suggester\_agent.py       # Agent for mentor suggestion
│   └── mental\_health\_agent.py          # (Optional) Mental health agent
│
├── knowledge\_base/
│   └── student\_profiles.csv            # Student profiles data
│
├── main.py                             # CLI entry point using Typer
├── requirements.txt                    # Python dependencies
└── README.md                           # Project documentation

````

### 📄 Sample CSV File

> You can use **your own CSV file** with student data or use the **`student_profiles.csv`** already included in the `knowledge_base/` folder of this project.

Make sure your CSV includes columns like:

* `name`
* `year`
* `branch`
* `interests`
* `goals`
* `struggles`

📂 **Location**: `knowledge_base/student_profiles.csv`

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/linkup.git
cd linkup
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the CLI

### 🔍 Match Peers by Interests or Struggles

```bash
python main.py match "AI"
```

### 🧑‍🏫 Find Mentors Based on Academic Goals

```bash
python main.py mentor "AI Research"
```

---

## 🧠 How the Agents Work

### 🔹 `MatchFinderAgent`

* Loads data from the CSV.
* Filters students whose **interests** or **struggles** match the input (case-insensitive).
* Returns a list of names, years, and branches.

### 🔹 `MentorSuggesterAgent`

* Filters **3rd and 4th year students**.
* Suggests mentors based on matching **goals**.

---

## 📦 Requirements

**`requirements.txt`**

```txt
typer==0.9.0
pandas
agno
```

Generate it manually with:

```bash
pip freeze > requirements.txt
```

---

## 🛠️ Technologies Used

* [Python 3.8+](https://www.python.org/)
* [Agno](https://docs.agno.com/introduction) – AI agent framework
* [Typer](https://typer.tiangolo.com/) – CLI interface
* [Pandas](https://pandas.pydata.org/) – For CSV reading & filtering

---

## 🙋‍♀️ Contribution

Want to add a mental health chatbot, frontend, or multilingual support?

* 🍴 Fork this repo
* 📦 Create your branch
* ✅ Commit your changes
* 🔁 Open a pull request!

---

## 📜 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Dhruvi Mahale**
🔗 GitHub:https://github.com/Dhruvimahale08

