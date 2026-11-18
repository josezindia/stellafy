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
- [Jira](https://afrotech.atlassian.net))

### 2. Install your development tools

- [Python](https://www.python.org/downloads/)
- [VS Code](https://code.visualstudio.com/)
- [Git](https://git-scm.com/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [DB Browser for SQLite (optional)](https://sqlitebrowser.org/)

### 3. Fork and clone the repository

Fork this repository to your GitHub account and clone your copy.

```bash
git clone https://github.com/YOUR-USERNAME/stellafy.git
cd stellafy
```

### 4. Set up Python

Once the starter configuration is available:

```bash
uv sync
```

Copy `.env.example` to `.env` and follow the configuration provided.

### 5. Run the application

Once the starter application is available:

```bash
uv run python run.py
```

Open http://127.0.0.1:5000 in your browser.

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

## Milestone 1: Getting Started

- Set up your development environment.
- Understand the Stellafy business model.
- Explore and run your first Flask application.
- Make your first GitHub commit.

**Deliverable:** A working Flask application.

## Milestone 2: Build the Storefront

- Design a simple website using Figma.
- Build the homepage and navigation.
- Display at least six products.
- Display three social causes.

**Deliverable:** A working storefront.

## Milestone 3: Shopping and Social Impact

- Build a shopping cart.
- Calculate purchase totals.
- Allow customers to select a cause.
- Calculate commissions and contributions.

**Deliverable:** A working simulated shopping experience.

## Milestone 4: Database and Analytics

- Create a SQLite database.
- Store products and simulated transactions.
- Calculate sales, revenue, and contributions.
- Build a simple analytics dashboard.

**Deliverable:** A working database and dashboard.

## Milestone 5: Test and Deploy

- Test the application.
- Fix identified bugs.
- Document your work.
- Deploy the application online.

**Deliverable:** A publicly accessible application.

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
