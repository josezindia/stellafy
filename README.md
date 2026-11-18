# Show What You Know: Stellafy

*Small purchases. Brighter futures.*

People shop online every day. What if those purchases could also support education, protect the environment, or help local communities without costing customers anything extra?

In this project, you'll build **Stellafy**, a small shopping platform that connects everyday purchases with social impact.

You'll apply what you're learning in computer science, economics, and finance to a real-world business problem.

You don't need to know everything before starting. Learn as you build.

## Goals

By the end of this project, you'll be able to:

- Build and deploy a web application.
- Work with Python and databases.
- Apply financial calculations to a business problem.
- Analyze and visualize data.
- Collaborate using GitHub and Jira.

## Required Features

- Homepage and product catalogue.
- Shopping cart.
- Social cause selection.
- Simulated checkout and contribution calculator.
- Sales and social impact dashboard.

All transactions and contributions are simulated. No real payments are required.

## How Stellafy Works

Imagine a customer purchases a product for $100.

| Description | Amount |
|---|---:|
| Customer purchase | $100 |
| Merchant commission (10%) | $10 |
| Contribution to cause (60% of commission) | $6 |
| Stellafy revenue before expenses | $4 |

The customer pays nothing extra. Part of the commission supports their selected cause.

## Technology Stack

| Technology | Purpose |
|---|---|
| HTML & Tailwind CSS | Website design |
| HTMX & JavaScript | Website interaction |
| Python & Flask | Application logic |
| SQLite & SQLAlchemy | Database |
| Pandas & Chart.js | Data analysis and visualization |
| Pytest | Testing |
| uv | Dependency management |
| Git & GitHub | Version control |
| Jira | Project management |
| Figma | UI design |

## Environment Setup

### 1. Create your accounts

- [GitHub](https://github.com/)
- [GitHub Student Developer Pack](https://github.com/settings/education/benefits)
- [Figma](https://www.figma.com/)
- [Jira](https://afrotech.atlassian.net)

### 2. Install your development tools

- [Python](https://www.python.org/downloads/)
- [VS Code](https://code.visualstudio.com/)
- [Git](https://git-scm.com/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [DB Browser for SQLite (optional)](https://sqlitebrowser.org/)

### 3. Fork and clone the repository

1. Open the [Stellafy repository](https://github.com/josezindia/stellafy).
2. Click **Fork** in the top-right corner.
3. Click **Create fork** to create your own copy.

#### Clone using VS Code (Recommended)

1. Open Visual Studio Code.
2. Open the Command Palette:
   - Windows: `Ctrl + Shift + P`
   - macOS: `Cmd + Shift + P`
3. Search for `Git: Clone` and select it.
4. Enter your forked repository URL:

   https://github.com/YOUR-USERNAME/stellafy.git

5. Choose a folder on your computer.
6. Click **Open** when VS Code asks you to open the cloned repository.

#### Alternatively, clone using the terminal

```bash
git clone https://github.com/YOUR-USERNAME/stellafy.git
cd stellafy
code .
```

Replace `YOUR-USERNAME` with your GitHub username.

If `code .` doesn't work, open VS Code manually and select
**File → Open Folder → stellafy**.

### 4. Set up Python

In VS Code, open **Terminal → New Terminal**.

Once the project configuration (`pyproject.toml`) is available, run:

```bash
uv sync
```

This creates your Python environment and installs the required dependencies.

If `.env.example` is available, copy it to `.env` and follow
the configuration provided.

Never commit your `.env` file to GitHub.

### 5. Run the application

Once the application (`run.py`) is available, run:

```bash
uv run python run.py
```

Open http://127.0.0.1:5000 in your browser.

If the Stellafy homepage appears, your development environment
is ready.

To stop the application, press `Ctrl + C` in your terminal.


## Project Structure

Build toward this structure as you complete your milestones.

```text
stellafy/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── main.py
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── templates/
│       ├── base.html
│       ├── index.html
│       └── partials/
├── instance/
├── migrations/
├── tests/
├── .env.example
├── .gitignore
├── pyproject.toml
├── uv.lock
├── README.md
└── run.py
```

You do not need to create every file on the first day.

---

## Milestones

Complete these in order. Open only the milestone you are working on. Your mentor will assign individual tasks in Jira and GitHub Issues.

| Milestone | Deliverable |
|---|---|
| [1. Getting Started](milestones/01-getting-started/README.md) | Running Flask application |
| [2. Build the Storefront](milestones/02-storefront/README.md) | Working storefront |
| [3. Shopping and Social Impact](milestones/03-shopping-and-impact/README.md) | Simulated shopping and impact calculator |
| [4. Database and Analytics](milestones/04-database-and-analytics/README.md) | Saved orders and analytics dashboard |
| [5. Testing and Deployment](milestones/05-testing-and-deployment/README.md) | Tested, deployed application |

---

## Development Workflow

Your mentor will assign tasks through Jira and GitHub Issues.

For each assigned task:

1. Read the GitHub Issue.
2. Move the Jira task to In Progress.
3. Create a Git branch.
4. Implement and test your changes.
5. Commit and push your changes.
6. Open a pull request for review.
7. Address feedback and merge after approval.
8. Move the Jira task to Done.

## Stretch Features

Optional features to explore after completing the main project:

- User registration and login.
- Product search and filtering.
- Interactive charts.
- Financial scenario analysis.

## Final Submission

- GitHub repository URL.
- Live application URL.
- Application screenshots.
- Meaningful Git commits.
- A short demonstration video.
- A brief reflection on what you learned.

## Project Guidelines

- Build one feature at a time.
- Keep your code simple and readable.
- Commit your progress regularly.
- Never commit passwords, secret keys, or your `.env` file.
- Use AI as a learning assistant.
- Understand the code you write.
- Ask questions when you're stuck.

**Build small. Learn as you go. Keep improving.**
