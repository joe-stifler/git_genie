**GitGenie: Enhancing Git Workflow Quality**

GitGenie is a Python-based command-line interface (CLI) tool designed to enhance the quality of Git commit histories and pull request descriptions. It automates the generation of meaningful commit messages and compiles detailed pull request summaries, streamlining the review process and improving project collaboration.

### **Motivation**

The creation of GitGenie stems from a desire to:

1. Improve Collaboration: Facilitate clearer, more informative commit histories and pull request descriptions, enhancing team collaboration and code review efficiency.
2. Automate Repetitive Tasks: Reduce the manual effort involved in crafting commit messages and summarizing pull requests, allowing developers to focus on coding.
3. Enforce Best Practices: Encourage the use of semantic versioning and detailed documentation, leading to better version control and project management.
4. Leverage AI: Utilize the capabilities of large language models (LLMs) to analyze code changes and generate descriptive, semantic commit messages that adhere to Semantic Versioning 2.0.0.

### **Features**

- Automated Commit Message Generation: Creates commit messages based on staged changes, using LLMs to ensure they adhere to Semantic Versioning 2.0.0.
- Pull Request Inspection: Generates a comprehensive summary of commit history for branch reviews, formatted for immediate use in pull request descriptions.
- Intuitive CLI: Offers a simple and user-friendly command-line interface to inspect repositories and generate commit messages efficiently.
- Versatile Usage: Ideal for individual developers, teams, and projects of any size aiming to maintain high-quality Git practices.

### **Requirements**

No additional requirements are needed to run GitGenie. However, to use the clipboard functionality for copying commit messages, you may need to install xclip on Linux systems. You can do this by running the following command:

```bash
sudo apt-get install xclip
```

### **Installation**

```bash
bashCopy code
pip install gitgenie

```

### **Usage**

GitGenie simplifies your Git workflow. Here’s how to use it:

```bash
# Generate a commit message:
gitgenie generate -r /path/to/repo

# Inspect a repository for a pull request:
gitgenie inspect -r /path/to/repo -b feature-branch -o PR_summary.md
```

### **Roadmap**

- [x] Implement commit message generation based on staged changes.
- [x] Add support for custom commit message templates.
- [ ] Integrate AI models for commit message generation.
- [ ] Enhance pull request inspection with additional metrics and insights, such as code complexity and test coverage.

### **Contributing**

We welcome contributions! Please see our CONTRIBUTING.md for guidelines on how to make contributions. This includes information on commit messages, branch naming conventions, pull requests, and more. Your input helps make GitGenie even better.

### **License**

GitGenie is released under the MIT License. See the LICENSE file for more details.

### **AI Involvement in Content Generation**

This project leverages AI to assist in generating content, specifically for commit message creation and pull request description generation.

### **Acknowledgements**

This project was crafted with insights from various resources, including [Software Engineering at Google](https://abseil.io/resources/swe-book/), to ensure adherence to best practices in software development.
