# Commit History and Git Patch Changes for files (git diff):

```json
[
    {
        "hash": "c719ebf431077f5765aa36770391611d837dc0b9",
        "message": "ci: add pull request template",
        "author": "joe-stifler",
        "author_email": "joseribeiro1017@gmail.com",
        "timestamp": "2024-03-27T09:48:02+00:00",
        "parents": [
            "c25ee92a307948914d6c3c10da941e8db7170900"
        ],
        "all_file_changes": [
            {
                "file_path": ".github/pull_request_template.md",
                "deleted_file": true,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": false,
                "changes": ".github/pull_request_template.md\n=======================================================\nlhs: 100644 | 276e0b5088cb12ca603d36355c106fb52082eeca\nrhs: None\nfile deleted in rhs\n---@@ -1,7 +0,0 @@\n-## Why this PR and What changes?\n-<!-- Explain the need for this PR (Pull Request). -->\n- \n-<!-- Summarize changes made (Pull Request). -->\n- \n-## Tests added?\n-<!-- State test status and provide a brief description of the tests. -->\n\n---"
            }
        ]
    },
    {
        "hash": "5e5409b5cc7e828dc13cfadf33bab19f3c2fddf8",
        "message": "ci: add flake8 and pytest configuration files",
        "author": "joe-stifler",
        "author_email": "joseribeiro1017@gmail.com",
        "timestamp": "2024-03-27T09:53:41+00:00",
        "parents": [
            "c719ebf431077f5765aa36770391611d837dc0b9"
        ],
        "all_file_changes": [
            {
                "file_path": ".flake8",
                "deleted_file": true,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": false,
                "changes": ".flake8\n=======================================================\nlhs: 100644 | b68fdd05a15475089a5d041dbd8c40ccdfe4937f\nrhs: None\nfile deleted in rhs\n---@@ -1,2 +0,0 @@\n-[flake8]\n-max-line-length = 200\n\n---"
            },
            {
                "file_path": ".pytest.ini",
                "deleted_file": true,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": false,
                "changes": ".pytest.ini\n=======================================================\nlhs: 100644 | eea2c180278f7b2bc64449bc2dce8d07e3856af1\nrhs: None\nfile deleted in rhs\n---@@ -1 +0,0 @@\n-[pytest]\n\n---"
            }
        ]
    },
    {
        "hash": "af46b1345eecb6746d8d141896fad39cb8f1ad07",
        "message": "chore: add .gitignore file",
        "author": "joe-stifler",
        "author_email": "joseribeiro1017@gmail.com",
        "timestamp": "2024-03-27T12:48:57+00:00",
        "parents": [
            "5e5409b5cc7e828dc13cfadf33bab19f3c2fddf8"
        ],
        "all_file_changes": [
            {
                "file_path": ".gitignore",
                "deleted_file": true,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": false,
                "changes": ".gitignore\n=======================================================\nlhs: 100644 | e858ef266427ba2cf419edd4a78e4698690e09db\nrhs: None\nfile deleted in rhs\n---@@ -1,20 +0,0 @@\n-build/\n-*.egg-info\n-__pycache__\n-\n-.ipynb_checkpoints\n-__pycache__/\n-.pytest_cache/\n-.eggs/\n-*.egg-info\n-docs-build/\n-docs-files/\n-*.coverage\n-*.log\n-.vscode\n-*.xml\n-build/\n-*.DS_Store\n-*.csv\n-\n-output\n\n---"
            }
        ]
    },
    {
        "hash": "798319590cb9d97898c1568dac6cb35108cf84d3",
        "message": "docs: add contributing file",
        "author": "joe-stifler",
        "author_email": "joseribeiro1017@gmail.com",
        "timestamp": "2024-03-27T12:49:10+00:00",
        "parents": [
            "af46b1345eecb6746d8d141896fad39cb8f1ad07"
        ],
        "all_file_changes": [
            {
                "file_path": "CONTRIBUTING.md",
                "deleted_file": true,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": false,
                "changes": "CONTRIBUTING.md\n=======================================================\nlhs: 100644 | 014cd1f4ee5efba0fe1a722a62045ab5d38cfd5b\nrhs: None\nfile deleted in rhs\n---@@ -1,246 +0,0 @@\n-# Contributing Guidelines\n-\n-### Key Points to Note:\n-\n-- **Not Absolute Truths**: the information herein is not exhaustively curated and is subject to change.\n-\n-- **Reference Official Documentation**: In case of uncertainty, it's always better to consult the official documentation, relevant books, or content provided by our great professors.\n-\n-- **Open to Suggestions**: Your participation in this project is highly valued. So feel free to open an Issue or Pull Request to propose enhancements to this guide.\n-\n----\n-\n-## Main Software Engineering Book References\n-\n-One highly recommended resource is [Software Engineering at Google](https://abseil.io/resources/swe-book/), a treasure trove of best practices and insights from Google\u2019s software development experiences. While a detailed summary will be added later, we encourage all contributors to explore this book for a deeper understanding of collaborative software engineering.\n-\n----\n-\n-## Guidelines\n-\n-Adopting standards in software development is essential for consistency, readability, and collaboration. Standards simplify the complexity of collaborative projects and support automation processes such as [Semantic Versioning](https://semver.org/) and [Releases](https://github.com/semantic-release/semantic-release).\n-\n-### Git\n-\n-Understanding Git is crucial for our workflow. While the [VS Code extension for Git](https://code.visualstudio.com/docs/sourcecontrol/overview) is a time-saver, knowing how to use [Git CLI](https://git-scm.com/docs) is fundamental. For quick reference, consult the [Git Cheat Sheet](https://training.github.com/downloads/github-git-cheat-sheet.pdf).\n-\n-\n-<details>\n-<summary><b>Relevant Links:</b></summary>\n-\n-- [Official Git Documentation](https://git-scm.com/docs)\n-- [VS Code Git Extension](https://code.visualstudio.com/docs/sourcecontrol/overview)\n-- [Pro Git Book](https://git-scm.com/book/en/v2)\n-- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)\n-\n-</details>\n-\n-\n-### Branch Methodology\n-\n-We follow [GitHub Flow](https://githubflow.github.io/), a straightforward and effective branch-based workflow. GitHub Flow is a lightweight, branch-based workflow that emphasizes collaboration, review, and prompt integration. It involves creating branches for new features or fixes, implementing changes, opening PRs for review, revising, merging against main, and then deleting the feature branch upon completion. Ultimately, the `main` branch is the primary source of truth. For a more in-depth discussion, see [Software Engineering at Google book - Version Control and Branch Management Chapter](https://abseil.io/resources/swe-book/html/ch16.html).\n-\n-<details>\n-<summary><b>Relevant Links:</b></summary>\n-\n-- [GitHub Flow](https://githubflow.github.io/)\n-- [Critique of Git Flow](https://georgestocker.com/2020/03/04/please-stop-recommending-git-flow/)\n-- [Git Flow Model](https://nvie.com/posts/a-successful-git-branching-model/)\n-- [Chapter on Version Control and Branch Management](https://abseil.io/resources/swe-book/html/ch16.html)\n-</details>\n-\n-### Commit Message Convention\n-\n-We adhere to [Conventional Commits](https://www.conventionalcommits.org/) standards:\n-\n-```markdown\n-<type>: <short summary> ( #<pull-request-reference> )\n-  \u2502           \u2502                       |\n-  |           |                       \u2514\u2500\u2af8 The PR reference number.\n-  |           |\n-  \u2502           \u2514\u2500\u2af8 Summary in present tense. Not capitalized. No period at the end.\n-  \u2502\n-  \u2514\u2500\u2af8 Commit Type: feat|feat!|fix|fix!|perf|perf!|refactor|refactor!|test|bench|build|ci|docs|style|chore\n-```\n-\n-<details>\n-<summary><b>Commit Types:</b></summary>\n-\n-| Type       | Description                                          | Example                                                        |\n-|------------|------------------------------------------------------|----------------------------------------------------------------|\n-| feat       | add a new feature                                    | `feat: add linear algebra solver for Computational Mathematics module` |\n-| feat!      | a breaking change to a feature                       | `feat!: add linear algebra solver for Computational Mathematics module` |\n-| fix        | a bug fix                                            | `fix: correct data preprocessing bug in ML project`            |\n-| fix!       | a breaking change to a bug fix                       | `fix!: correct data preprocessing bug in ML project`           |\n-| perf       | a code change that improves performance              | `perf: optimize pipeline for reduced training time`            |\n-| perf!      | a breaking change to a performance improvement       | `perf!: optimize pipeline for reduced training time`           |\n-| refactor   | a code change that neither fixes a bug nor adds a feature | `refactor: optimize pipeline for reduced training time`        |\n-| refactor!  | a breaking change to a refactoring                  | `refactor!: optimize pipeline for reduced training time`       |\n-| test       | adding missing tests or correcting existing tests   | `test: add unit tests for data preprocessing pipeline`         |\n-| bench      | improvements to benchmarks                          | `bench: improve performance of data preprocessing pipeline`    |\n-| build      | changes to build system or external dependencies    | `build: update dependencies for Data Science module`           |\n-| ci         | changes to CI configuration files and scripts       | `ci: update CI configuration for Data Science module`          |\n-| docs       | documentation only changes                          | `docs: update README for Modern Programming Methods`           |\n-| style      | changes that do not affect the meaning of the code  | `style: update code formatting for Data Science module`        |\n-| chore      | changes to the build process or auxiliary tools and libraries | `chore: update dependencies for Data Science module`        |\n-</details>\n-\n-<details>\n-<summary><b>Commit Rules:</b></summary>\n-\n-1) Follow the commit naming convention.\n-2) Be concise and descriptive.\n-3) Use English.\n-4) Start with a verb in imperative mood.\n-5) Use present tense.\n-6) Avoid ending with a period.\n-</details>\n-\n-<details>\n-<summary><b>Relevant Links:</b></summary>\n-\n-- [Conventional Commits](https://www.conventionalcommits.org/)\n-- [Angular Commit Message Guidelines](https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#-commit-message-guidelines)\n-</details>\n-\n-### Branch Naming Convention\n-\n-Branch names should be descriptive, following this format:\n-\n-```markdown\n-<type>/<issue-reference>/<description>\n-  \u2502           \u2502                |\n-  |           |                \u2514\u2500\u2af8 A short description of the branch's purpose.\n-  |           |\n-  \u2502           \u2514\u2500\u2af8 The github issue/ticket number. Use `no-ref` if no issue.\n-  \u2502\n-  \u2514\u2500\u2af8 Branch Type: feat|feat!|fix|fix!|perf|perf!|refactor|refactor!|test|bench|build|ci|docs|style|chore\n-```\n-\n-<details>\n-<summary><b>Branch Name Examples:</b></summary>\n-\n-- `fix/no-ref/update-dependencies`\n-- `fix/issue-27/fix-data-sync-error`\n-- `test/no-ref/refactor-math-algorithms`\n-- `feature/issue-15/implement-regression-analysis`\n-</details>\n-\n-<details>\n-<summary><b>Relevant Links:</b></summary>\n-\n-- [Conventional Commits](https://www.conventionalcommits.org/)\n-- [Simplified Naming Convention](https://dev.to/varbsan/a-simplified-convention-for-naming-branches-and-commits-in-git-il4)\n-</details>\n-\n-### Pull Requests (PRs) and Code Reviews\n-\n-PRs are vital for proposing and reviewing changes. Reviewers ensure code quality, while contributors address feedback for merge-readiness. According to [Software Engineering at Google - Code Review Chapter](https://abseil.io/resources/swe-book/html/ch09.html), code reviews are key for knowledge sharing and documentation. PR titles should follow the same commit naming convention as before:\n-\n-```markdown\n-<type>: <short summary> ( #<pull-request-reference> )\n-  \u2502           \u2502                       |\n-  |           |                       \u2514\u2500\u2af8 The PR reference number.\n-  |           |\n-  \u2502           \u2514\u2500\u2af8 Summary in present tense. Not capitalized. No period at the end.\n-  \u2502\n-  \u2514\u2500\u2af8 Commit Type: feat|feat!|fix|fix!|perf|perf!|refactor|refactor!|test|bench|build|ci|docs|style|chore\n-```\n-\n-<details>\n-<summary><b>PR Description Template:</b></summary>\n-\n-```markdown\n-## Why this PR?\n-- Explain the need.\n-\n-## What Changes?\n-- Summarize changes.\n-\n-## Tests added?\n-- State test status.\n-\n-## Breaking changes created?\n-- Highlight any disruptions.\n-\n-## Additional context?\n-- Provide more information.\n-```\n-</details>\n-\n-<details>\n-<summary><b>PR Description Example:</b></summary>\n-\n-```markdown\n-## Why this PR?\n-- To address performance issues in our ML model training process.\n-\n-## What Changes?\n-- Enhanced the DataPreprocessing class in data_processing.py.\n-\n-## Tests added?\n-- Comprehensive unit tests were included.\n-\n-## Breaking changes created?\n-- None.\n-\n-## Additional context?\n-- Related to issue #1234 and reviewed by the data science team.\n-```\n-</details>\n-\n-<details>\n-<summary><b>PR Rules:</b></summary>\n-\n-- PR titles must follow the commit naming convention.\n-- PR descriptions should adhere to the template.\n-- Link PRs to relevant issues.\n-- Ensure PRs are reviewed by knowledgeable team members.\n-- Tag PRs appropriately.\n-- Assign PRs to responsible individuals.\n-- Link PRs to milestones and projects.\n-- PRs must pass automated checks.\n-- Use `Squash and Merge` for merging.\n-- PRs should be up-to-date with `main`.\n-\n-</details>\n-\n-<details>\n-<summary><b>Relevant Links:</b></summary>\n-\n-- [GitHub PRs Overview](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests)\n-- [PR Templates](https://docs.github.com/en/github/building-a-strong-community/creating-a-pull-request-template-for-your-repository)\n-- [PR Labels](https://docs.github.com/en/github/managing-your-work-on-github/applying-labels-to-issues-and-pull-requests)\n-- [Assigning PRs](https://docs.github.com/en/github/managing-your-work-on-github/assigning-issues-and-pull-requests-to-other-github-users)\n-- [PR Milestones](https://docs.github.com/en/github/managing-your-work-on-github/about-milestones)\n-- [PR Projects](https://docs.github.com/en/github/managing-your-work-on-github/about-project-boards)\n-- [PR Checks](https://docs.github.com/en/actions/guides/about-continuous-integration)\n-- [Merge Methods on GitHub](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github)\n-\n-</details>\n-\n-### Issues\n-TODO: Provide guidelines for effective issue management.\n-\n-### Code Style\n-TODO: Define code style guidelines.\n-\n-### Continuous Integration and Deployment\n-TODO: Detail our CI/CD practices.\n-\n-### Semantic Versioning and Releases\n-TODO: Explain versioning and release management.\n-\n-### Semantic Versioning and Releases\n-\n-TODO: Explain versioning and release management.\n-\n-### Collaboration and Communication\n-\n-TODO: Outline collaboration and communication protocols.\n-\n----\n-\n-## Code of Conduct\n-\n-This file was crafted with the assistance of ChatGPT.\n\n---"
            }
        ]
    },
    {
        "hash": "f07bd0f24f401d96462178f8ae4df3de82e5c3cf",
        "message": "build: add environment.yml, requirements.txt, and setup.py files",
        "author": "joe-stifler",
        "author_email": "joseribeiro1017@gmail.com",
        "timestamp": "2024-03-27T12:49:39+00:00",
        "parents": [
            "798319590cb9d97898c1568dac6cb35108cf84d3"
        ],
        "all_file_changes": [
            {
                "file_path": "environment.yml",
                "deleted_file": true,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": false,
                "changes": "environment.yml\n=======================================================\nlhs: 100644 | 63fe08845740710456aefac6a000cfc63caf040d\nrhs: None\nfile deleted in rhs\n---@@ -1,10 +0,0 @@\n-name: git-genie\n-channels:\n-  - conda-forge\n-dependencies:\n-  - python=3.10\n-  - pip\n-  - pip:\n-    - jupyter\n-    - ipykernel\n-    - -r requirements.txt\n\n---"
            },
            {
                "file_path": "requirements.txt",
                "deleted_file": true,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": false,
                "changes": "requirements.txt\n=======================================================\nlhs: 100644 | 19fb5587f8ca82007bc088a261235b365b814010\nrhs: None\nfile deleted in rhs\n---@@ -1,8 +0,0 @@\n-jupyter\n-ipykernel\n-pytest===7.4.3\n-coverage===7.4.4\n-flake8\n-black[jupyter]\n-GitPython\n-pyperclip\n\n---"
            },
            {
                "file_path": "setup.py",
                "deleted_file": true,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": false,
                "changes": "setup.py\n=======================================================\nlhs: 100644 | 872e0c609fcd4ad0bcadb909141b16371b020aa5\nrhs: None\nfile deleted in rhs\n---@@ -1,23 +0,0 @@\n-from setuptools import setup, find_packages\n-\n-setup(\n-    name=\"git_genie\",\n-    version=\"0.1.0\",\n-    author=\"Joe\",\n-    author_email=\"joseribeiro1017@gmail.com\",\n-    packages=find_packages(),\n-    install_requires=[],\n-    entry_points={\n-        \"console_scripts\": [\n-            \"git_genie=git_genie.__init__:main\"\n-        ]\n-    },\n-    classifiers=[\n-        \"Programming Language :: Python :: 3\",\n-        \"License :: OSI Approved :: MIT License\",\n-        \"Operating System :: OS Independent\",\n-    ],\n-    description=\"A simple crawler.\",\n-    long_description=open(\"README.md\").read(),\n-    long_description_content_type=\"text/markdown\",\n-)\n\n---"
            }
        ]
    },
    {
        "hash": "a4c62602a2a075894919c586f6c496cb1764ff70",
        "message": "docs: add MIT License",
        "author": "joe-stifler",
        "author_email": "joseribeiro1017@gmail.com",
        "timestamp": "2024-03-27T12:49:48+00:00",
        "parents": [
            "f07bd0f24f401d96462178f8ae4df3de82e5c3cf"
        ],
        "all_file_changes": [
            {
                "file_path": "LICENSE",
                "deleted_file": true,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": false,
                "changes": "LICENSE\n=======================================================\nlhs: 100644 | 7e75c18bd76a45213c6949b2eb63a15cd0e22890\nrhs: None\nfile deleted in rhs\n---@@ -1,21 +0,0 @@\n-MIT License\n-\n-Copyright (c) 2024 OTSU\n-\n-Permission is hereby granted, free of charge, to any person obtaining a copy\n-of this software and associated documentation files (the \"Software\"), to deal\n-in the Software without restriction, including without limitation the rights\n-to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n-copies of the Software, and to permit persons to whom the Software is\n-furnished to do so, subject to the following conditions:\n-\n-The above copyright notice and this permission notice shall be included in all\n-copies or substantial portions of the Software.\n-\n-THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n-IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n-FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n-AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n-LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n-OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n-SOFTWARE.\n\\ No newline at end of file\n\n---"
            }
        ]
    },
    {
        "hash": "308d45187d6dbba9fa9a71c1aae12f38bf9194c3",
        "message": "ci: add release workflow and package.json for semantic release",
        "author": "joe-stifler",
        "author_email": "joseribeiro1017@gmail.com",
        "timestamp": "2024-03-27T12:50:00+00:00",
        "parents": [
            "a4c62602a2a075894919c586f6c496cb1764ff70"
        ],
        "all_file_changes": [
            {
                "file_path": ".github/workflows/release.yml",
                "deleted_file": true,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": false,
                "changes": ".github/workflows/release.yml\n=======================================================\nlhs: 100644 | 8bb64670e83d12280f91d949b1ae7ad8a70eea35\nrhs: None\nfile deleted in rhs\n---@@ -1,52 +0,0 @@\n-name: Release\n-\n-on:\n-  push:\n-    branches:\n-      - main\n-\n-jobs:\n-  lint-test:\n-    uses: ./.github/workflows/lint-test.yml\n-\n-  release:\n-    name: Release Python Package\n-    runs-on: ubuntu-latest\n-    needs: lint-test\n-\n-    # TODO: remove unnecessary permissions\n-    permissions:\n-        contents: write\n-        actions: write\n-        checks: write\n-        issues: write\n-        discussions: write\n-        packages: write\n-        pull-requests: write\n-        repository-projects: write\n-        statuses: write\n-    steps:\n-      - name: Checkout code\n-        uses: actions/checkout@v3\n-\n-      - name: Set up Python 3.10\n-        uses: actions/setup-python@v4\n-        with:\n-          python-version: \"3.10\"\n-  \n-      - name: Install Dependencies\n-        run: |\n-          pip install -e .\n-          pip install -r requirements.txt\n-\n-      - name: Setup node\n-        uses: actions/setup-node@v3\n-        with:\n-          node-version: \"18.x\"\n-\n-      - name: Semantic relase\n-        run: |\n-          npm install semantic-release\n-          npx semantic-release\n-        env:\n-          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}\n\n---"
            },
            {
                "file_path": "package.json",
                "deleted_file": true,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": false,
                "changes": "package.json\n=======================================================\nlhs: 100644 | 26615978e682e367588e0b0016fbbc2b0e2d81ab\nrhs: None\nfile deleted in rhs\n---@@ -1,58 +0,0 @@\n-{\n-    \"name\": \"crawler\",\n-    \"version\": \"0.0.0-development\",\n-    \"devDependencies\": {\n-        \"conventional-changelog-conventionalcommits\": \"^5.0.0\",\n-        \"semantic-release\": \"^21.0.2\"\n-    },\n-    \"release\": {\n-        \"branches\": [\n-            \"main\"\n-        ],\n-        \"plugins\": [\n-            [\n-                \"@semantic-release/commit-analyzer\",\n-                {\n-                    \"preset\": \"conventionalCommits\",\n-                    \"releaseRules\": [\n-                        {\n-                            \"type\": \"build\",\n-                            \"release\": \"patch\"\n-                        },\n-                        {\n-                            \"type\": \"docs\",\n-                            \"release\": \"patch\"\n-                        }\n-                    ],\n-                    \"parserOpts\": {\n-                        \"noteKeywords\": [\n-                            \"BREAKING CHANGE\",\n-                            \"BREAKING CHANGES\",\n-                            \"BREAKING\"\n-                        ]\n-                    }\n-                }\n-            ],\n-            \"@semantic-release/release-notes-generator\",\n-            [\n-                \"@semantic-release/exec\",\n-                {\n-                    \"prepareCmd\": \"ls\"\n-                }\n-            ],\n-            [\n-                \"@semantic-release/github\",\n-                {\n-                    \"assets\": [\n-                        {\n-                            \"path\": \"*.tar.gz\"\n-                        }\n-                    ]\n-                }\n-            ]\n-        ]\n-    },\n-    \"dependencies\": {\n-        \"@semantic-release/exec\": \"^6.0.3\"\n-    }\n-}\n\n---"
            }
        ]
    },
    {
        "hash": "1085dad5c68aff460098f49690d88248de204802",
        "message": "ci: add conda, unit testing, linting, and coverage workflows",
        "author": "joe-stifler",
        "author_email": "joseribeiro1017@gmail.com",
        "timestamp": "2024-03-27T12:50:42+00:00",
        "parents": [
            "308d45187d6dbba9fa9a71c1aae12f38bf9194c3"
        ],
        "all_file_changes": [
            {
                "file_path": ".github/workflows/conda.yml",
                "deleted_file": true,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": false,
                "changes": ".github/workflows/conda.yml\n=======================================================\nlhs: 100644 | d57e7c3f19ce393b59a51cb9cb574d208a61198f\nrhs: None\nfile deleted in rhs\n---@@ -1,29 +0,0 @@\n-name: Conda\n-\n-on:\n-  push:\n-    branches:\n-      - main\n-\n-jobs:\n-  conda-check:\n-    name: Check Conda environment\n-    runs-on: ubuntu-latest\n-    steps:\n-      - name: Checkout code\n-        uses: actions/checkout@v3\n-\n-      - uses: conda-incubator/setup-miniconda@v2\n-        with:\n-          activate-environment: pietstormai\n-          environment-file: environment.yml\n-      - run: |\n-          pip install --upgrade pip\n-          pip install -e .\n-          pip install -r requirements.txt\n-      - run: |\n-          conda info --envs\n-      - run: |\n-          python3 --version\n-      - run: |\n-          python3 -m pytest\n\n---"
            },
            {
                "file_path": ".github/workflows/coverage.yml",
                "deleted_file": true,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": false,
                "changes": ".github/workflows/coverage.yml\n=======================================================\nlhs: 100644 | 75c4b243166c9e47378bbdb2bc2a6e05e18575ee\nrhs: None\nfile deleted in rhs\n---@@ -1,61 +0,0 @@\n-name: Coverage\n-\n-on:\n-  pull_request:\n-    types:\n-      - opened\n-      - synchronize\n-\n-jobs:\n-  lint-test:\n-    uses: ./.github/workflows/lint-test.yml\n-\n-  check-coverage:\n-    name: Python Code Coverage\n-    runs-on: ubuntu-latest\n-    needs: lint-test\n-    permissions:\n-      contents: read\n-      pull-requests: write\n-    env:\n-      # TODO: 5% of coverage is pretty low.\n-      # We should increase this value after Friday.\n-      COVERAGE_THRESHOLDS: '0 50'\n-    steps:\n-    - name: Download Coverage Report\n-      uses: actions/download-artifact@v3\n-      with:\n-        name: coverage-report\n-        path: .\n-\n-    - name: Code Coverage Summary Report\n-      uses: irongut/CodeCoverageSummary@v1.3.0\n-      with:\n-        badge: true\n-        output: 'both'\n-        format: 'markdown'\n-        hide_complexity: true\n-        hide_branch_rate: false\n-        filename: 'coverage.xml'\n-        thresholds: ${{ env.COVERAGE_THRESHOLDS }}\n-\n-    - name: Cat coverage.md file\n-      run: cat code-coverage-results.md\n-\n-    - name: Comment on Pull Request\n-      uses: marocchino/sticky-pull-request-comment@v2\n-      if: github.event_name == 'pull_request'\n-      with:\n-        recreate: true\n-        path: code-coverage-results.md\n-\n-    - name: Write to Job Summary\n-      run: cat code-coverage-results.md >> $GITHUB_STEP_SUMMARY\n-\n-    - name: Code Coverage Threshold Check\n-      uses: irongut/CodeCoverageSummary@v1.3.0\n-      with:\n-        fail_below_min: true\n-        filename: 'coverage.xml'\n-        hide_branch_rate: false\n-        thresholds: ${{ env.COVERAGE_THRESHOLDS }}\n\n---"
            },
            {
                "file_path": ".github/workflows/lint-test.yml",
                "deleted_file": true,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": false,
                "changes": ".github/workflows/lint-test.yml\n=======================================================\nlhs: 100644 | 9bd6350db2adf519761ecd480696c1fdaf0aa395\nrhs: None\nfile deleted in rhs\n---@@ -1,65 +0,0 @@\n-name: Lint and Test\n-\n-on:\n-  workflow_call:\n-\n-concurrency:\n-  group: ${{ github.workflow }}-${{ github.ref }}\n-  cancel-in-progress: true\n-\n-jobs:\n-  python-lint:\n-    name: Lint Python Code\n-    runs-on: ubuntu-latest\n-\n-    steps:\n-    - uses: actions/checkout@v3\n-\n-    - name: Set up Python 3.10\n-      uses: actions/setup-python@v4\n-      with:\n-        python-version: \"3.10\"\n-\n-    - name: Install dependencies\n-      run: |\n-        pip install -r requirements.txt\n-\n-    - name: Lint Code\n-      run: |\n-        flake8 .\n-\n-    # TODO: disabling for now\n-    # - name: Lint Docs\n-    #   run: |\n-    #     pydocstyle --convention=numpy .\n-\n-  python-unit-tests:\n-    name: Run Unit Python Tests\n-    runs-on: ubuntu-latest\n-\n-    steps:\n-    - name: Checkout Code\n-      uses: actions/checkout@v3\n-\n-    - name: Set up Python 3.10\n-      uses: actions/setup-python@v4\n-      with:\n-        python-version: \"3.10\"\n-\n-    - name: Install Dependencies\n-      run: |\n-        pip install --upgrade pip\n-        pip install -e .\n-        pip install -r requirements.txt\n-\n-    - name: Run Pytest\n-      run: |\n-        # Note: `pytest.ini` is used to enable specific pytest packages.\n-        coverage run --branch --source=crawler -m pytest\n-        coverage xml\n-\n-    - name: Upload Coverage Report\n-      uses: actions/upload-artifact@v3\n-      with:\n-        name: coverage-report\n-        path: coverage.xml\n\n---"
            }
        ]
    },
    {
        "hash": "31eeb64c885f0dfa7dde4da4ff1a815be980be07",
        "message": "ci: add pull request template",
        "author": "joe-stifler",
        "author_email": "joseribeiro1017@gmail.com",
        "timestamp": "2024-03-27T12:50:49+00:00",
        "parents": [
            "1085dad5c68aff460098f49690d88248de204802"
        ],
        "all_file_changes": [
            {
                "file_path": "PR_description.md",
                "deleted_file": true,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": false,
                "changes": "PR_description.md\n=======================================================\nlhs: 100644 | 46c80dd849c4e485cc0647d2539f84edbab4f7ed\nrhs: None\nfile deleted in rhs\n---@@ -1,24 +0,0 @@\n-# Commit History to be merged to main:\n-\n-- ci: add pull request template\n-- joe-stifler\n-- joseribeiro1017@gmail.com\n-- 2024-03-27 09:48:02\n-- \n-- Files Changed: 1\n-- Lines Added: 0\n-- Lines Removed: 1\n-- Commit SHA: c719ebf431077f5765aa36770391611d837dc0b9\n-\n-\n-# Pull Request Template:\n-\n-## Why this PR and What changes?\n-<!-- Explain the need for this PR (Pull Request). -->\n-<!-- Summarize changes made (Pull Request). -->\n-\n-## Tests added?\n-<!-- State test status and provide a brief description of the tests. -->\n-\n-# Pull Request Description Task:\n-Using the commit history above and the pull request template, create the pull request description for the current branch / pull request.\n\n---"
            }
        ]
    },
    {
        "hash": "b33bc88f1c70b9d28be5696bf6965bddf82628c1",
        "message": "ci: add pyproject.yml with black configuration",
        "author": "joe-stifler",
        "author_email": "joseribeiro1017@gmail.com",
        "timestamp": "2024-03-27T12:51:00+00:00",
        "parents": [
            "31eeb64c885f0dfa7dde4da4ff1a815be980be07"
        ],
        "all_file_changes": [
            {
                "file_path": "pyproject.yml",
                "deleted_file": true,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": false,
                "changes": "pyproject.yml\n=======================================================\nlhs: 100644 | 2e917d2f4ccf8b1e0f5e18ba09bf298c34fb003f\nrhs: None\nfile deleted in rhs\n---@@ -1,2 +0,0 @@\n-[tool.black]\n-line_length = 100\n\n---"
            }
        ]
    },
    {
        "hash": "67480ff19be4b7b7c6365fa7e94b3d33dc3669d4",
        "message": "feat: add file_aggregator.py and file_utils.py to git_genie/utils",
        "author": "joe-stifler",
        "author_email": "joseribeiro1017@gmail.com",
        "timestamp": "2024-03-27T12:51:23+00:00",
        "parents": [
            "b33bc88f1c70b9d28be5696bf6965bddf82628c1"
        ],
        "all_file_changes": [
            {
                "file_path": "git_genie/utils/file_aggregator.py",
                "deleted_file": true,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": false,
                "changes": "git_genie/utils/file_aggregator.py\n=======================================================\nlhs: 100644 | 7e4163550865b89a83ab8408e725059f148e9ecf\nrhs: None\nfile deleted in rhs\n---@@ -1,81 +0,0 @@\n-import glob\n-import os\n-import tempfile\n-\n-# Define the path where you want to start searching for files\n-start_path = \".\"  # Use '.' for current directory or specify your own path\n-\n-# Define the pattern to match .h and .cpp files\n-patterns = [\"*.py\"]\n-\n-# Define the output file where the content will be aggregated\n-output_file = \"all_headers_and_cpp_files_content_from_this_repository_in_one_file.txt\"\n-\n-# Define folders to ignore\n-ignored_folders = [\n-    \"third_party\",\n-    \".git\",\n-    \"scans\",\n-    \"build\",\n-    \".vscode\",\n-    \".github\",\n-    \"transformed_images\",\n-]\n-\n-# Get the absolute path of the start_path to ensure correct relative path\n-# calculation\n-start_path_abs = os.path.abspath(start_path)\n-\n-\n-# Function to get directory structure, excluding ignored folders\n-def get_directory_structure(startpath):\n-    structure = \"\"\n-    for root, dirs, files in os.walk(startpath, topdown=True):\n-        dirs[:] = [\n-            d\n-            for d in dirs\n-            if os.path.join(root, d)\n-            not in [os.path.join(startpath, f) for f in ignored_folders]\n-        ]  # Modify dirs in-place to ignore certain directories\n-        level = root.replace(startpath, \"\").count(os.sep)\n-        indent = \" \" * 4 * (level)\n-        structure += f\"{indent}{os.path.basename(root)}/\\n\"\n-        subindent = \" \" * 4 * (level + 1)\n-        for f in files:\n-            structure += f\"{subindent}{f}\\n\"\n-    return structure\n-\n-\n-# Write the aggregated content to a temporary file initially\n-with tempfile.NamedTemporaryFile(delete=False) as temp_outfile:\n-    temp_filename = temp_outfile.name\n-    with open(temp_filename, \"w\") as outfile:\n-        # Write directory structure first\n-        outfile.write(\"Directory Structure:\\n\")\n-        outfile.write(get_directory_structure(start_path_abs) + \"\\n\")\n-        outfile.write(\"Aggregated File Content:\\n\")\n-        # Then write the file contents as before\n-        for pattern in patterns:\n-            for filename in glob.glob(\n-                os.path.join(start_path, \"**\", pattern), recursive=True\n-            ):\n-                if any(\n-                    ignored_folder in filename for ignored_folder in ignored_folders\n-                ):\n-                    continue\n-                relative_path = os.path.relpath(filename, start_path_abs)\n-                outfile.write(\n-                    f\"/**\\n * Below follows the content associated with the file:\\n * {relative_path}\\n */\\n\"\n-                )\n-                with open(filename, \"r\") as infile:\n-                    content = infile.read()\n-                    outfile.write(content + \"\\n\\n\")\n-\n-# Now move the temporary file content to the original output file\n-# os.replace(temp_filename, output_file)\n-# mv the temporary file to the output file\n-os.system(f\"mv {temp_filename} {output_file}\")\n-\n-print(\n-    f\"All .h and .cpp files have been aggregated into {output_file}, ignoring specified folders, with directory structure prepended.\"\n-)\n\n---"
            },
            {
                "file_path": "git_genie/utils/file_utils.py",
                "deleted_file": true,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": false,
                "changes": "git_genie/utils/file_utils.py\n=======================================================\nlhs: 100644 | 784396513541fc3ba8f273788db7697e4fb507ba\nrhs: None\nfile deleted in rhs\n---@@ -1,89 +0,0 @@\n-import os\n-import re\n-\n-\n-def generate_filename_from_url(url):\n-    \"\"\"Generates a filesystem-safe filename from a URL.\n-\n-    This function removes the protocol part of the URL, replaces non-word characters with underscores,\n-    and truncates the filename to a maximum length of 255 characters to ensure compatibility with most filesystems.\n-    A '.md' extension is appended to the resulting filename.\n-\n-    Parameters\n-    ----------\n-    url : str\n-        The URL to be converted into a filename.\n-\n-    Returns\n-    -------\n-    str\n-        The generated safe filename ending with '.md'.\n-    \"\"\"\n-    # Protocol stripping and sanitization\n-    stripped_url = re.sub(r\"^https?://\", \"\", url)\n-    # Replace non-word characters with underscores\n-    safe_filename = re.sub(r\"\\W+\", \"_\", stripped_url)\n-    # Truncate to max filesystem filename length and append extension\n-    max_length = 255\n-    if len(safe_filename) > max_length:\n-        safe_filename = safe_filename[:max_length]\n-    safe_filename += \".md\"\n-    return safe_filename\n-\n-\n-def save_content_to_multiple_files(url_text_dict, directory=\"output\"):\n-    \"\"\"Saves content of each URL to its own Markdown file within the specified directory.\n-\n-    Each URL's content is saved in a separate Markdown file named after the URL itself. The function\n-    ensures the creation of the target directory if it does not already exist.\n-\n-    Parameters\n-    ----------\n-    url_text_dict : dict\n-        A dictionary where keys are URLs and values are their corresponding Markdown text content.\n-    directory : str, optional\n-        The directory path where files will be saved. Defaults to 'output'.\n-    \"\"\"\n-    # Ensure target directory exists\n-    if not os.path.exists(directory):\n-        os.makedirs(directory)\n-\n-    # Write each URL's content to a separate file\n-    for url, markdown_text in url_text_dict.items():\n-        filename = generate_filename_from_url(url)\n-        header = f\"# Source URL: {url}\\n\\n\"\n-        content = header + markdown_text\n-        with open(os.path.join(directory, filename), \"w\", encoding=\"utf-8\") as file:\n-            file.write(content)\n-\n-\n-def save_content_to_single_file(\n-    url_text_dict, directory=\"output\", filename=\"combined_output.md\"\n-):\n-    \"\"\"Saves content of all URLs into a single Markdown file within the specified directory.\n-\n-    Content from each URL is saved consecutively in the same file, separated by Markdown horizontal rules.\n-    The function ensures the creation of the target directory if it does not already exist.\n-\n-    Parameters\n-    ----------\n-    url_text_dict : dict\n-        A dictionary where keys are URLs and values are their corresponding Markdown text content.\n-    directory : str, optional\n-        The directory path where the combined file will be saved. Defaults to 'output'.\n-    filename : str, optional\n-        The name of the file to save the combined content. Defaults to 'combined_output.md'.\n-    \"\"\"\n-    # Ensure target directory exists\n-    if not os.path.exists(directory):\n-        os.makedirs(directory)\n-\n-    # Combine all content into a single string\n-    combined_content = \"\"\n-    for url, markdown_text in url_text_dict.items():\n-        header = f\"# Source URL: {url}\\n\\n\"\n-        combined_content += header + markdown_text + \"\\n\\n---\\n\\n\"\n-\n-    # Write combined content to the specified file\n-    with open(os.path.join(directory, filename), \"w\", encoding=\"utf-8\") as file:\n-        file.write(combined_content)\n\n---"
            }
        ]
    },
    {
        "hash": "d0a341b57e6e87d2dd9a4f34b6e5fa8cfcafc620",
        "message": "test: add tests for file_utils module",
        "author": "joe-stifler",
        "author_email": "joseribeiro1017@gmail.com",
        "timestamp": "2024-03-27T12:51:30+00:00",
        "parents": [
            "67480ff19be4b7b7c6365fa7e94b3d33dc3669d4"
        ],
        "all_file_changes": [
            {
                "file_path": "tests/test_file_utils.py",
                "deleted_file": true,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": false,
                "changes": "tests/test_file_utils.py\n=======================================================\nlhs: 100644 | 96926b3e35ef354010660938ddf69d45084c7c22\nrhs: None\nfile deleted in rhs\n---@@ -1,17 +0,0 @@\n-from crawler.utils.file_utils import (\n-    generate_filename_from_url,\n-    save_content_to_single_file,\n-)\n-\n-\n-def test_generate_filename_from_url():\n-    url = \"https://example.com/page?query=123\"\n-    filename = generate_filename_from_url(url)\n-    assert filename == \"example_com_page_query_123.md\"\n-\n-\n-def test_save_content_to_single_file(tmp_path):\n-    url_text_dict = {\"https://example.com\": \"# Example Content\"}\n-    save_content_to_single_file(url_text_dict, directory=tmp_path, filename=\"test.md\")\n-    saved_file = tmp_path / \"test.md\"\n-    assert saved_file.exists()\n\n---"
            }
        ]
    },
    {
        "hash": "f83e956042ce3f93e14cf5e6d009aff41046610f",
        "message": "feat: add MarkdownGenerator class to generate PR descriptions",
        "author": "joe-stifler",
        "author_email": "joseribeiro1017@gmail.com",
        "timestamp": "2024-03-27T12:51:36+00:00",
        "parents": [
            "d0a341b57e6e87d2dd9a4f34b6e5fa8cfcafc620"
        ],
        "all_file_changes": [
            {
                "file_path": "git_genie/markdown_generator.py",
                "deleted_file": true,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": false,
                "changes": "git_genie/markdown_generator.py\n=======================================================\nlhs: 100644 | e35d9bd9ce8eb4fb8c9833a1d8879aa45ba0b4c9\nrhs: None\nfile deleted in rhs\n---@@ -1,56 +0,0 @@\n-import sys\n-import json\n-import logging\n-\n-class MarkdownGenerator:\n-    \"\"\"\n-    A class to generate Markdown descriptions from commit history data.\n-\n-    Methods\n-    -------\n-    generate_pr_description(commit_history)\n-        Produces a Markdown string with a detailed description of each commit.\n-    \"\"\"\n-\n-    @staticmethod\n-    def generate_pr_description(commit_history, template_path):\n-        \"\"\"\n-        Generates a detailed Pull Request description in Markdown format \n-        from a list of commit information dictionaries.\n-\n-        Parameters\n-        ----------\n-        commit_history : list of dict\n-            The commit history as a list of dictionaries, with each dictionary\n-            containing details of a commit and associated changes.\n-        template_path : str\n-            The path to the Pull Request template file.\n-\n-        Returns\n-        -------\n-        str\n-            A string in Markdown format describing the commits.\n-\n-        \"\"\"\n-        markdown_content = '# Commit History and Git Patch Changes for files (git diff):\\n\\n```json\\n'\n-        markdown_content += json.dumps(commit_history, indent=4, sort_keys=False)\n-        markdown_content += '\\n```\\n'\n-        \n-        markdown_content  += '\\n# Pull Request Template:\\n\\n```markdown\\n'\n-\n-        try:\n-            with open(template_path, 'r', encoding=\"utf-8\") as f:\n-                markdown_content += f.read()\n-        except FileNotFoundError:\n-            logging.warning(\"Failed to read the Pull Request template file at: %s\", template_path)\n-            sys.exit(1)\n-\n-        markdown_content += '```\\n'\n-        \n-        markdown_content += '\\n# Now perform the following tasks:\\n\\n'\n-        markdown_content += '1. Review the changes in the commit history above.\\n'\n-        markdown_content += '2. Fill out the Pull Request Template.\\n'\n-        markdown_content += '4. Check which files are created, which ones are removed, and which ones are updated.\\n'\n-        markdown_content += '3. Then think step by step and ensure that your generated the correct PR description by checking the patch json content generated from git diff provided above.\\n'\n-\n-        return markdown_content\n\n---"
            }
        ]
    },
    {
        "hash": "6d00657a2a7ec770b09c28ed82d6a810443e1da2",
        "message": "feat: add GitRepo class to manage Git repositories",
        "author": "joe-stifler",
        "author_email": "joseribeiro1017@gmail.com",
        "timestamp": "2024-03-27T12:51:46+00:00",
        "parents": [
            "f83e956042ce3f93e14cf5e6d009aff41046610f"
        ],
        "all_file_changes": [
            {
                "file_path": "git_genie/git_repo.py",
                "deleted_file": true,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": false,
                "changes": "git_genie/git_repo.py\n=======================================================\nlhs: 100644 | 9916ad2fc4ac643182a14b566b23999e797f04a8\nrhs: None\nfile deleted in rhs\n---@@ -1,142 +0,0 @@\n-import logging\n-from git import Repo\n-\n-class GitRepo:\n-    \"\"\"\n-    Interface to a Git repository, providing access to the repository's commit history.\n-\n-    Parameters\n-    ----------\n-    path : str, optional\n-        The file system path to the Git repository. Defaults to the current directory.\n-\n-    Attributes\n-    ----------\n-    repo : git.Repo\n-        The GitPython Repo object.\n-\n-    Methods\n-    -------\n-    get_commit_history(branch_name, main_branch_name='main')\n-        Retrieves the commit history for a given branch not merged into the main branch.\n-    \"\"\"\n-\n-    def __init__(self, path='.'):\n-        \"\"\"\n-        Initialize a GitRepo object.\n-\n-        Parameters\n-        ----------\n-        path : str, optional\n-            The file system path to the Git repository. Defaults to the current directory.\n-        \"\"\"\n-        self.repo = Repo(path)\n-\n-    def get_commit_history(self, branch_name, main_branch_name='main', start_commit_hash=None):\n-        \"\"\"\n-        Retrieves a list of commits in the branch that are not in the main branch\n-        and are newer than the specified start_commit_hash.\n-\n-        Parameters\n-        ----------\n-        branch_name : str\n-            The name of the branch to retrieve the commit history for.\n-        main_branch_name : str, optional\n-            The name of the main branch to compare against. Defaults to 'main'.\n-        start_commit_hash : str, optional\n-            The hash of the commit to start the history from. If specified, only commits\n-            newer than this commit will be included. Defaults to None.\n-\n-        Returns\n-        -------\n-        list of dict\n-            A list of dictionaries, each representing a commit with its details\n-            and associated changes.\n-\n-        Examples\n-        --------\n-        >>> repo = GitRepo('/path/to/repo')\n-        >>> commit_history = repo.get_commit_history('feature-branch')\n-        >>> print(commit_history[0]['message'])\n-        Initial commit message\n-        \"\"\"\n-        commits = list(self.repo.iter_commits(f'{start_commit_hash}..'))\n-        commit_history = []\n-\n-        # If start_commit_hash is specified, filter out older commits\n-        # if start_commit_hash:\n-        #     try:\n-        #         start_commit = self.repo.commit(start_commit_hash)\n-        #         commits = [commit for commit in commits if commit.committed_date >= start_commit.committed_date or commit.hexsha == start_commit_hash]\n-        #     except ValueError:\n-        #         logging.warning(\"Warning: The provided commit hash %s could not be found. Ignoring the start commit hash.\", start_commit_hash)\n-        \n-        for commit in commits[::-1]:  # List from oldest to newest\n-            all_file_changes = self._get_commit_files(commit)\n-\n-            commit_info = {\n-                'hash': commit.hexsha,\n-                'message': commit.message.strip(),\n-                'author': commit.author.name,\n-                'author_email': commit.author.email,\n-                'timestamp': commit.committed_datetime.isoformat(),\n-                'parents': [parent.hexsha for parent in commit.parents],\n-                'all_file_changes': all_file_changes,\n-            }\n-            commit_history.append(commit_info)\n-\n-        return commit_history\n-\n-    def _get_commit_files(self, commit):\n-        \"\"\"\n-        Helper method to retrieve file changes for a specific commit.\n-\n-        Parameters\n-        ----------\n-        commit : git.Commit\n-            The commit object to retrieve file changes from.\n-\n-        Returns\n-        -------\n-        list of dict\n-            A list of dictionaries each representing a file's changes.\n-        \"\"\"\n-        files_added = []\n-        files_modified = []\n-        files_deleted = []\n-        all_file_changes = []\n-        for diff in commit.diff(commit.parents[0] if commit.parents else None, create_patch=True):\n-            file_change = {\n-                'file_path': diff.b_path if diff.new_file else diff.a_path,\n-                'deleted_file': diff.deleted_file,\n-                'new_file': diff.new_file,\n-                'copied_file': diff.copied_file,\n-                'rename_from': diff.rename_from,\n-                'rename_to': diff.rename_to,\n-                'updated_file': not (\n-                    diff.deleted_file or\n-                    diff.new_file or\n-                    diff.copied_file or\n-                    diff.rename_from or\n-                    diff.rename_to\n-                ),\n-                'changes': str(diff),\n-            }\n-            all_file_changes.append(file_change)\n-        return all_file_changes\n-\n-    def _get_diff_lines(self, diff):\n-        \"\"\"\n-        Helper method to parse the diff of a file.\n-\n-        Parameters\n-        ----------\n-        diff : git.Diff\n-            The diff object to parse changes from.\n-\n-        Returns\n-        -------\n-        str\n-            A string representing the diff of the file.\n-        \"\"\"\n-        return diff.diff.decode('utf-8')\n\n---"
            }
        ]
    },
    {
        "hash": "286c58aa21209310e1c80b392310efd03403b0e1",
        "message": "feat: add CLIHandler class for command-line interface operations",
        "author": "joe-stifler",
        "author_email": "joseribeiro1017@gmail.com",
        "timestamp": "2024-03-27T12:51:54+00:00",
        "parents": [
            "6d00657a2a7ec770b09c28ed82d6a810443e1da2"
        ],
        "all_file_changes": [
            {
                "file_path": "git_genie/cli_handler.py",
                "deleted_file": true,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": false,
                "changes": "git_genie/cli_handler.py\n=======================================================\nlhs: 100644 | 990564e8538a96c8532f13fb240a42d1f9d9f7da\nrhs: None\nfile deleted in rhs\n---@@ -1,88 +0,0 @@\n-import logging\n-import argparse\n-import pyperclip\n-\n-from .git_repo import GitRepo\n-from .markdown_generator import MarkdownGenerator\n-\n-class CLIHandler:\n-    \"\"\"\n-    A class to handle command-line interface operations for the GitGenie tool.\n-\n-    This class uses argparse to parse command-line arguments and execute the appropriate\n-    functionalities provided by GitRepo and MarkdownGenerator classes.\n-\n-    Methods\n-    -------\n-    run()\n-        Executes the CLI based on the parsed arguments.\n-    \"\"\"\n-\n-    def __init__(self):\n-        \"\"\"\n-        Initializes the CLIHandler with an argument parser.\n-        Sets up the expected command-line arguments.\n-        \"\"\"\n-        self.parser = argparse.ArgumentParser(description=\"GitGenie CLI\")\n-        self._setup_cli_arguments()\n-\n-    def _setup_cli_arguments(self):\n-        \"\"\"\n-        Internal method to setup CLI argument parsing.\n-        \"\"\"\n-        self.parser.add_argument(\n-            '-b', '--branch', \n-            default=None,  # No default value; will use the current branch if not provided\n-            help='The branch to generate PR description for. Defaults to the current branch if not specified.'\n-        )\n-        self.parser.add_argument(\n-            '-r', '--repo-path', \n-            default='.',\n-            help='Path to the local Git repository (default: current directory).'\n-        )\n-        self.parser.add_argument('-t', '--template-path', default='.github/pull_request_template.md',\n-                                 help='Path to the Pull Request template (default: .github/pull_request_template.md).')\n-        self.parser.add_argument('-o', '--output-file', default='',\n-                                 help='Path to the output file to write the markdown description (optional).')\n-        self.parser.add_argument('-v', '--verbose', default='INFO',\n-                            choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],\n-                            help='Set the logging level (default: INFO).')\n-        self.parser.add_argument('-c', '--start-commit',\n-                                 default=None,\n-                                 help='The commit hash to start the commit history from. Only commits newer than this will be included.')\n-        \n-        self.args = self.parser.parse_args()\n-        \n-        logging.basicConfig(level=self.args.verbose)\n-\n-    def run(self):\n-        \"\"\"\n-        Executes the CLI based on the parsed arguments. It retrieves the commit history\n-        from the specified branch and generates a Markdown-formatted PR description.\n-        \"\"\"\n-        git_repo = GitRepo(self.args.repo_path)\n-\n-        # If no branch is specified, use the current active branch\n-        branch_name = self.args.branch or git_repo.repo.active_branch.name\n-        \n-        commit_history = git_repo.get_commit_history(branch_name, start_commit_hash=self.args.start_commit)\n-\n-        if commit_history:\n-            markdown_description = MarkdownGenerator.generate_pr_description(commit_history, self.args.template_path)\n-            print(markdown_description)\n-            \n-            # Ask the user if they want to copy the output to the clipboard\n-            should_copy = input(\"Would you like to copy the markdown description to the clipboard? (y/n): \").strip().lower()\n-\n-            if should_copy == 'y':\n-                pyperclip.copy(markdown_description)\n-                logging.info(\"Markdown description has been copied to clipboard.\")\n-            elif should_copy == 'n' and self.args.output_file:\n-                with open(self.args.output_file, 'w', encoding='utf-8') as f:\n-                    f.write(markdown_description)\n-                    logging.info(\"Markdown description has been written to %s.\", self.args.output_file)\n-            else:\n-                logging.error(\"Markdown description has not been copied to clipboard or written to file.\")\n-                \n-        else:\n-            logging.warning(f\"No commit history found for the specified branch: {branch_name}\")\n\n---"
            }
        ]
    },
    {
        "hash": "675d10a3e1cc471bb2997631a8e9268bbc51225a",
        "message": "feat: add LLMIntegrator class for interacting with LLM API",
        "author": "joe-stifler",
        "author_email": "joseribeiro1017@gmail.com",
        "timestamp": "2024-03-27T12:52:07+00:00",
        "parents": [
            "286c58aa21209310e1c80b392310efd03403b0e1"
        ],
        "all_file_changes": [
            {
                "file_path": "git_genie/llm_integrator.py",
                "deleted_file": true,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": false,
                "changes": "git_genie/llm_integrator.py\n=======================================================\nlhs: 100644 | fbf01e5fe2c04879f250226657bf554114c6639c\nrhs: None\nfile deleted in rhs\n---@@ -1,73 +0,0 @@\n-import requests\n-\n-class LLMIntegrator:\n-    \"\"\"\n-    A class to interact with an external Large Language Model (LLM) API for text generation tasks.\n-\n-    Parameters\n-    ----------\n-    api_url : str\n-        The endpoint URL of the LLM API service.\n-\n-    Attributes\n-    ----------\n-    api_url : str\n-        The endpoint URL of the LLM API service.\n-    session : requests.Session\n-        A Requests session for making API calls.\n-\n-    Methods\n-    -------\n-    generate_text(input_text)\n-        Sends text to the LLM API and returns the generated text response.\n-    \"\"\"\n-\n-    def __init__(self, api_url):\n-        \"\"\"\n-        Initializes the LLMIntegrator with the provided API URL.\n-\n-        Parameters\n-        ----------\n-        api_url : str\n-            The endpoint URL of the LLM API service.\n-        \"\"\"\n-        self.api_url = api_url\n-        self.session = requests.Session()\n-\n-    def generate_text(self, input_text):\n-        \"\"\"\n-        Sends text to the LLM API and retrieves the generated text based on the input.\n-\n-        Parameters\n-        ----------\n-        input_text : str\n-            The input text for the LLM to process and generate output from.\n-\n-        Returns\n-        -------\n-        str\n-            The text generated by the LLM based on the input.\n-\n-        Examples\n-        --------\n-        >>> llm = LLMIntegrator('https://api.example.com/generate')\n-        >>> response = llm.generate_text('Hello world')\n-        >>> print(response)\n-        'Hello, world! How can I help you today?'\n-        \"\"\"\n-        # Replace the mock call below with actual API interaction\n-        payload = {'input': input_text}\n-        headers = {'Authorization': 'Bearer YOUR_API_KEY'}\n-\n-        # Uncomment and configure the following lines for the actual API call:\n-        # response = self.session.post(self.api_url, json=payload, headers=headers)\n-        # response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code\n-        # return response.json().get('generated_text')\n-\n-        # Mock response for demonstration:\n-        return f'Mock response based on input: {input_text}'\n-\n-# Example usage (should be outside this file in practice):\n-# if __name__ == '__main__':\n-#     llm_integrator = LLMIntegrator('https://api.llm-provider.com/generate')\n-#     print(llm_integrator.generate_text('Example input text for the LLM.'))\n\n---"
            }
        ]
    },
    {
        "hash": "e4d283f1a96514b6e809fade8761aa724ebb7d28",
        "message": "feat: add GitRepo, CLIHandler, MarkdownGenerator, and main to __init__.py",
        "author": "joe-stifler",
        "author_email": "joseribeiro1017@gmail.com",
        "timestamp": "2024-03-27T12:52:22+00:00",
        "parents": [
            "675d10a3e1cc471bb2997631a8e9268bbc51225a"
        ],
        "all_file_changes": [
            {
                "file_path": "git_genie/__init__.py",
                "deleted_file": true,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": false,
                "changes": "git_genie/__init__.py\n=======================================================\nlhs: 100644 | 832ccba1a7e9963619230dd292b1af16eb0e2621\nrhs: None\nfile deleted in rhs\n---@@ -1,6 +0,0 @@\n-from .git_repo import GitRepo\n-from .cli_handler import CLIHandler\n-from .markdown_generator import MarkdownGenerator\n-from .main import main\n-\n-__all__ = ['GitRepo', 'CLIHandler', 'MarkdownGenerator', 'main']\n\n---"
            },
            {
                "file_path": "git_genie/utils/__init__.py",
                "deleted_file": true,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": false,
                "changes": "git_genie/utils/__init__.py\n=======================================================\nlhs: 100644 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391\nrhs: None\nfile deleted in rhs"
            }
        ]
    },
    {
        "hash": "8fdd770082ef2b8d327d2eef566ea7134fa60f57",
        "message": "feat: add main.py file with CLIHandler and main function",
        "author": "joe-stifler",
        "author_email": "joseribeiro1017@gmail.com",
        "timestamp": "2024-03-27T12:52:28+00:00",
        "parents": [
            "e4d283f1a96514b6e809fade8761aa724ebb7d28"
        ],
        "all_file_changes": [
            {
                "file_path": "git_genie/main.py",
                "deleted_file": true,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": false,
                "changes": "git_genie/main.py\n=======================================================\nlhs: 100644 | f5a75aa468484b687beff23e8de2cf32924b3653\nrhs: None\nfile deleted in rhs\n---@@ -1,12 +0,0 @@\n-from .cli_handler import CLIHandler\n-\n-def main():\n-    \"\"\"\n-    Main function to execute the CLIHandler which processes command-line arguments and\n-    runs the GitGenie tool accordingly.\n-    \"\"\"\n-    cli_handler = CLIHandler()\n-    cli_handler.run()\n-\n-if __name__ == '__main__':\n-    main()\n\n---"
            }
        ]
    },
    {
        "hash": "c7824734a2c84791ee1cf1e0cecaea4af91ab22c",
        "message": "docs: update README",
        "author": "joe-stifler",
        "author_email": "joseribeiro1017@gmail.com",
        "timestamp": "2024-03-27T12:52:56+00:00",
        "parents": [
            "8fdd770082ef2b8d327d2eef566ea7134fa60f57"
        ],
        "all_file_changes": [
            {
                "file_path": "README.md",
                "deleted_file": false,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": true,
                "changes": "README.md\n=======================================================\nlhs: 100644 | 8ab223e5a3ebeeabecf7870fb3f19935c15c68a0\nrhs: 100644 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391\n---@@ -1,70 +0,0 @@\n-**GitGenie: Enhancing Git Workflow Quality**\n-\n-GitGenie is a Python-based command-line interface (CLI) tool designed to enhance the quality of Git commit histories and pull request descriptions. It automates the generation of meaningful commit messages and compiles detailed pull request summaries, streamlining the review process and improving project collaboration.\n-\n-### **Motivation**\n-\n-The creation of GitGenie stems from a desire to:\n-\n-1. Improve Collaboration: Facilitate clearer, more informative commit histories and pull request descriptions, enhancing team collaboration and code review efficiency.\n-2. Automate Repetitive Tasks: Reduce the manual effort involved in crafting commit messages and summarizing pull requests, allowing developers to focus on coding.\n-3. Enforce Best Practices: Encourage the use of semantic versioning and detailed documentation, leading to better version control and project management.\n-4. Leverage AI: Utilize the capabilities of large language models (LLMs) to analyze code changes and generate descriptive, semantic commit messages that adhere to Semantic Versioning 2.0.0.\n-\n-### **Features**\n-\n-- Automated Commit Message Generation: Creates commit messages based on staged changes, using LLMs to ensure they adhere to Semantic Versioning 2.0.0.\n-- Pull Request Inspection: Generates a comprehensive summary of commit history for branch reviews, formatted for immediate use in pull request descriptions.\n-- Intuitive CLI: Offers a simple and user-friendly command-line interface to inspect repositories and generate commit messages efficiently.\n-- Versatile Usage: Ideal for individual developers, teams, and projects of any size aiming to maintain high-quality Git practices.\n-\n-### **Requirements**\n-\n-No additional requirements are needed to run GitGenie. However, to use the clipboard functionality for copying commit messages, you may need to install xclip on Linux systems. You can do this by running the following command:\n-\n-```bash\n-sudo apt-get install xclip\n-```\n-\n-### **Installation**\n-\n-```bash\n-bashCopy code\n-pip install gitgenie\n-\n-```\n-\n-### **Usage**\n-\n-GitGenie simplifies your Git workflow. Here\u2019s how to use it:\n-\n-```bash\n-# Generate a commit message:\n-gitgenie generate -r /path/to/repo\n-\n-# Inspect a repository for a pull request:\n-gitgenie inspect -r /path/to/repo -b feature-branch -o PR_summary.md\n-```\n-\n-### **Roadmap**\n-\n-- [x] Implement commit message generation based on staged changes.\n-- [x] Add support for custom commit message templates.\n-- [ ] Integrate AI models for commit message generation.\n-- [ ] Enhance pull request inspection with additional metrics and insights, such as code complexity and test coverage.\n-\n-### **Contributing**\n-\n-We welcome contributions! Please see our CONTRIBUTING.md for guidelines on how to make contributions. This includes information on commit messages, branch naming conventions, pull requests, and more. Your input helps make GitGenie even better.\n-\n-### **License**\n-\n-GitGenie is released under the MIT License. See the LICENSE file for more details.\n-\n-### **AI Involvement in Content Generation**\n-\n-This project leverages AI to assist in generating content, specifically for commit message creation and pull request description generation.\n-\n-### **Acknowledgements**\n-\n-This project was crafted with insights from various resources, including [Software Engineering at Google](https://abseil.io/resources/swe-book/), to ensure adherence to best practices in software development.\n\n---"
            }
        ]
    },
    {
        "hash": "a04ef88323dfc80644555394b917378fa377b8e4",
        "message": "docs: add example jupyter notebook file to test the git_genie pull request creation",
        "author": "joe-stifler",
        "author_email": "joseribeiro1017@gmail.com",
        "timestamp": "2024-03-27T12:53:42+00:00",
        "parents": [
            "c7824734a2c84791ee1cf1e0cecaea4af91ab22c"
        ],
        "all_file_changes": [
            {
                "file_path": "examples/pull_request_llm_context.ipynb",
                "deleted_file": true,
                "new_file": false,
                "copied_file": false,
                "rename_from": null,
                "rename_to": null,
                "updated_file": false,
                "changes": "examples/pull_request_llm_context.ipynb\n=======================================================\nlhs: 100644 | cd2d59281120c55f03bcdf6f17234e8ca9a2bf7b\nrhs: None\nfile deleted in rhs\n---@@ -1,294 +0,0 @@\n-{\n- \"cells\": [\n-  {\n-   \"cell_type\": \"code\",\n-   \"execution_count\": 43,\n-   \"metadata\": {},\n-   \"outputs\": [\n-    {\n-     \"name\": \"stdout\",\n-     \"output_type\": \"stream\",\n-     \"text\": [\n-      \"The autoreload extension is already loaded. To reload it, use:\\n\",\n-      \"  %reload_ext autoreload\\n\"\n-     ]\n-    }\n-   ],\n-   \"source\": [\n-    \"%load_ext autoreload\\n\",\n-    \"%autoreload 2\"\n-   ]\n-  },\n-  {\n-   \"cell_type\": \"code\",\n-   \"execution_count\": 44,\n-   \"metadata\": {},\n-   \"outputs\": [\n-    {\n-     \"data\": {\n-      \"text/plain\": [\n-       \"'/home/joe/Documents/1-PROJECTS/AI-Projects/UTILITIES/git_genie'\"\n-      ]\n-     },\n-     \"execution_count\": 44,\n-     \"metadata\": {},\n-     \"output_type\": \"execute_result\"\n-    }\n-   ],\n-   \"source\": [\n-    \"%pwd\"\n-   ]\n-  },\n-  {\n-   \"cell_type\": \"code\",\n-   \"execution_count\": 45,\n-   \"metadata\": {},\n-   \"outputs\": [\n-    {\n-     \"name\": \"stdout\",\n-     \"output_type\": \"stream\",\n-     \"text\": [\n-      \"Already at the repository root.\\n\"\n-     ]\n-    }\n-   ],\n-   \"source\": [\n-    \"import os\\n\",\n-    \"\\n\",\n-    \"# print this notebook file name\\n\",\n-    \"if not os.path.exists(\\\".git\\\"):  # Assuming a Git repository\\n\",\n-    \"    %cd ../\\n\",\n-    \"else:\\n\",\n-    \"    print(\\\"Already at the repository root.\\\")\"\n-   ]\n-  },\n-  {\n-   \"cell_type\": \"code\",\n-   \"execution_count\": 46,\n-   \"metadata\": {},\n-   \"outputs\": [],\n-   \"source\": [\n-    \"from git_genie import *\"\n-   ]\n-  },\n-  {\n-   \"cell_type\": \"code\",\n-   \"execution_count\": 47,\n-   \"metadata\": {},\n-   \"outputs\": [],\n-   \"source\": [\n-    \"git_repo = GitRepo(\\\"./\\\")\"\n-   ]\n-  },\n-  {\n-   \"cell_type\": \"code\",\n-   \"execution_count\": 48,\n-   \"metadata\": {},\n-   \"outputs\": [],\n-   \"source\": [\n-    \"branch_name = \\\"feat/generate-pull-request-llm-context\\\"\"\n-   ]\n-  },\n-  {\n-   \"cell_type\": \"code\",\n-   \"execution_count\": 49,\n-   \"metadata\": {},\n-   \"outputs\": [],\n-   \"source\": [\n-    \"commit_history = git_repo.get_commit_history(branch_name)\"\n-   ]\n-  },\n-  {\n-   \"cell_type\": \"code\",\n-   \"execution_count\": 50,\n-   \"metadata\": {},\n-   \"outputs\": [\n-    {\n-     \"name\": \"stdout\",\n-     \"output_type\": \"stream\",\n-     \"text\": [\n-      \"[\\n\",\n-      \"    {\\n\",\n-      \"        \\\"hash\\\": \\\"c719ebf431077f5765aa36770391611d837dc0b9\\\",\\n\",\n-      \"        \\\"message\\\": \\\"ci: add pull request template\\\",\\n\",\n-      \"        \\\"author\\\": \\\"joe-stifler\\\",\\n\",\n-      \"        \\\"author_email\\\": \\\"joseribeiro1017@gmail.com\\\",\\n\",\n-      \"        \\\"timestamp\\\": \\\"2024-03-27T09:48:02+00:00\\\",\\n\",\n-      \"        \\\"files\\\": [\\n\",\n-      \"            {\\n\",\n-      \"                \\\"file_path\\\": \\\".github/pull_request_template.md\\\",\\n\",\n-      \"                \\\"changes\\\": \\\"@@ -1,7 +0,0 @@\\\\n-## Why this PR and What changes?\\\\n-<!-- Explain the need for this PR (Pull Request). -->\\\\n- \\\\n-<!-- Summarize changes made (Pull Request). -->\\\\n- \\\\n-## Tests added?\\\\n-<!-- State test status and provide a brief description of the tests. -->\\\\n\\\"\\n\",\n-      \"            }\\n\",\n-      \"        ]\\n\",\n-      \"    },\\n\",\n-      \"    {\\n\",\n-      \"        \\\"hash\\\": \\\"5e5409b5cc7e828dc13cfadf33bab19f3c2fddf8\\\",\\n\",\n-      \"        \\\"message\\\": \\\"ci: add flake8 and pytest configuration files\\\",\\n\",\n-      \"        \\\"author\\\": \\\"joe-stifler\\\",\\n\",\n-      \"        \\\"author_email\\\": \\\"joseribeiro1017@gmail.com\\\",\\n\",\n-      \"        \\\"timestamp\\\": \\\"2024-03-27T09:53:41+00:00\\\",\\n\",\n-      \"        \\\"files\\\": [\\n\",\n-      \"            {\\n\",\n-      \"                \\\"file_path\\\": \\\".flake8\\\",\\n\",\n-      \"                \\\"changes\\\": \\\"@@ -1,2 +0,0 @@\\\\n-[flake8]\\\\n-max-line-length = 200\\\\n\\\"\\n\",\n-      \"            },\\n\",\n-      \"            {\\n\",\n-      \"                \\\"file_path\\\": \\\".pytest.ini\\\",\\n\",\n-      \"                \\\"changes\\\": \\\"@@ -1 +0,0 @@\\\\n-[pytest]\\\\n\\\"\\n\",\n-      \"            }\\n\",\n-      \"        ]\\n\",\n-      \"    }\\n\",\n-      \"]\\n\"\n-     ]\n-    }\n-   ],\n-   \"source\": [\n-    \"import json\\n\",\n-    \"\\n\",\n-    \"pretty_json = json.dumps(commit_history, indent=4, sort_keys=False)\\n\",\n-    \"\\n\",\n-    \"print(pretty_json)\"\n-   ]\n-  },\n-  {\n-   \"cell_type\": \"code\",\n-   \"execution_count\": 51,\n-   \"metadata\": {},\n-   \"outputs\": [\n-    {\n-     \"ename\": \"TypeError\",\n-     \"evalue\": \"MarkdownGenerator.generate_pr_description() missing 1 required positional argument: 'template_path'\",\n-     \"output_type\": \"error\",\n-     \"traceback\": [\n-      \"\\u001b[0;31m---------------------------------------------------------------------------\\u001b[0m\",\n-      \"\\u001b[0;31mTypeError\\u001b[0m                                 Traceback (most recent call last)\",\n-      \"Cell \\u001b[0;32mIn[51], line 1\\u001b[0m\\n\\u001b[0;32m----> 1\\u001b[0m markdown_generator \\u001b[38;5;241m=\\u001b[39m \\u001b[43mMarkdownGenerator\\u001b[49m\\u001b[38;5;241;43m.\\u001b[39;49m\\u001b[43mgenerate_pr_description\\u001b[49m\\u001b[43m(\\u001b[49m\\u001b[43mcommit_history\\u001b[49m\\u001b[43m)\\u001b[49m\\n\",\n-      \"\\u001b[0;31mTypeError\\u001b[0m: MarkdownGenerator.generate_pr_description() missing 1 required positional argument: 'template_path'\"\n-     ]\n-    }\n-   ],\n-   \"source\": [\n-    \"markdown_generator = MarkdownGenerator.generate_pr_description(commit_history)\"\n-   ]\n-  },\n-  {\n-   \"cell_type\": \"code\",\n-   \"execution_count\": null,\n-   \"metadata\": {},\n-   \"outputs\": [\n-    {\n-     \"data\": {\n-      \"text/plain\": [\n-       \"'# Commit History:\\\\n\\\\n```json\\\\n[\\\\n    {\\\\n        \\\"author\\\": \\\"joe-stifler\\\",\\\\n        \\\"author_email\\\": \\\"joseribeiro1017@gmail.com\\\",\\\\n        \\\"files\\\": [\\\\n            {\\\\n                \\\"changes\\\": \\\"@@ -1,7 +0,0 @@\\\\\\\\n-## Why this PR and What changes?\\\\\\\\n-<!-- Explain the need for this PR (Pull Request). -->\\\\\\\\n- \\\\\\\\n-<!-- Summarize changes made (Pull Request). -->\\\\\\\\n- \\\\\\\\n-## Tests added?\\\\\\\\n-<!-- State test status and provide a brief description of the tests. -->\\\\\\\\n\\\",\\\\n                \\\"file_path\\\": \\\".github/pull_request_template.md\\\"\\\\n            }\\\\n        ],\\\\n        \\\"hash\\\": \\\"c719ebf431077f5765aa36770391611d837dc0b9\\\",\\\\n        \\\"message\\\": \\\"ci: add pull request template\\\",\\\\n        \\\"timestamp\\\": \\\"2024-03-27T09:48:02+00:00\\\"\\\\n    },\\\\n    {\\\\n        \\\"author\\\": \\\"joe-stifler\\\",\\\\n        \\\"author_email\\\": \\\"joseribeiro1017@gmail.com\\\",\\\\n        \\\"files\\\": [\\\\n            {\\\\n                \\\"changes\\\": \\\"@@ -1,2 +0,0 @@\\\\\\\\n-[flake8]\\\\\\\\n-max-line-length = 200\\\\\\\\n\\\",\\\\n                \\\"file_path\\\": \\\".flake8\\\"\\\\n            },\\\\n            {\\\\n                \\\"changes\\\": \\\"@@ -1 +0,0 @@\\\\\\\\n-[pytest]\\\\\\\\n\\\",\\\\n                \\\"file_path\\\": \\\".pytest.ini\\\"\\\\n            }\\\\n        ],\\\\n        \\\"hash\\\": \\\"5e5409b5cc7e828dc13cfadf33bab19f3c2fddf8\\\",\\\\n        \\\"message\\\": \\\"ci: add flake8 and pytest configuration files\\\",\\\\n        \\\"timestamp\\\": \\\"2024-03-27T09:53:41+00:00\\\"\\\\n    }\\\\n]\\\\n```\\\\n\\\\n# Pull Request Template:\\\\n\\\\n```markdown\\\\n## Why this PR and What changes?\\\\n<!-- Explain the need for this PR (Pull Request). -->\\\\n \\\\n<!-- Summarize changes made (Pull Request). -->\\\\n \\\\n## Tests added?\\\\n<!-- State test status and provide a brief description of the tests. -->\\\\n```\\\\n\\\\n# Your Task:\\\\n\\\\n1. Review the changes in the commit history above.\\\\n2. Fill out the Pull Request Template.\\\\n'\"\n-      ]\n-     },\n-     \"execution_count\": 38,\n-     \"metadata\": {},\n-     \"output_type\": \"execute_result\"\n-    }\n-   ],\n-   \"source\": [\n-    \"markdown_generator\"\n-   ]\n-  },\n-  {\n-   \"cell_type\": \"code\",\n-   \"execution_count\": null,\n-   \"metadata\": {},\n-   \"outputs\": [\n-    {\n-     \"data\": {\n-      \"text/markdown\": [\n-       \"# Commit History:\\n\",\n-       \"\\n\",\n-       \"```json\\n\",\n-       \"[\\n\",\n-       \"    {\\n\",\n-       \"        \\\"author\\\": \\\"joe-stifler\\\",\\n\",\n-       \"        \\\"author_email\\\": \\\"joseribeiro1017@gmail.com\\\",\\n\",\n-       \"        \\\"files\\\": [\\n\",\n-       \"            {\\n\",\n-       \"                \\\"changes\\\": \\\"@@ -1,7 +0,0 @@\\\\n-## Why this PR and What changes?\\\\n-<!-- Explain the need for this PR (Pull Request). -->\\\\n- \\\\n-<!-- Summarize changes made (Pull Request). -->\\\\n- \\\\n-## Tests added?\\\\n-<!-- State test status and provide a brief description of the tests. -->\\\\n\\\",\\n\",\n-       \"                \\\"file_path\\\": \\\".github/pull_request_template.md\\\"\\n\",\n-       \"            }\\n\",\n-       \"        ],\\n\",\n-       \"        \\\"hash\\\": \\\"c719ebf431077f5765aa36770391611d837dc0b9\\\",\\n\",\n-       \"        \\\"message\\\": \\\"ci: add pull request template\\\",\\n\",\n-       \"        \\\"timestamp\\\": \\\"2024-03-27T09:48:02+00:00\\\"\\n\",\n-       \"    },\\n\",\n-       \"    {\\n\",\n-       \"        \\\"author\\\": \\\"joe-stifler\\\",\\n\",\n-       \"        \\\"author_email\\\": \\\"joseribeiro1017@gmail.com\\\",\\n\",\n-       \"        \\\"files\\\": [\\n\",\n-       \"            {\\n\",\n-       \"                \\\"changes\\\": \\\"@@ -1,2 +0,0 @@\\\\n-[flake8]\\\\n-max-line-length = 200\\\\n\\\",\\n\",\n-       \"                \\\"file_path\\\": \\\".flake8\\\"\\n\",\n-       \"            },\\n\",\n-       \"            {\\n\",\n-       \"                \\\"changes\\\": \\\"@@ -1 +0,0 @@\\\\n-[pytest]\\\\n\\\",\\n\",\n-       \"                \\\"file_path\\\": \\\".pytest.ini\\\"\\n\",\n-       \"            }\\n\",\n-       \"        ],\\n\",\n-       \"        \\\"hash\\\": \\\"5e5409b5cc7e828dc13cfadf33bab19f3c2fddf8\\\",\\n\",\n-       \"        \\\"message\\\": \\\"ci: add flake8 and pytest configuration files\\\",\\n\",\n-       \"        \\\"timestamp\\\": \\\"2024-03-27T09:53:41+00:00\\\"\\n\",\n-       \"    }\\n\",\n-       \"]\\n\",\n-       \"```\\n\",\n-       \"\\n\",\n-       \"# Pull Request Template:\\n\",\n-       \"\\n\",\n-       \"```markdown\\n\",\n-       \"## Why this PR and What changes?\\n\",\n-       \"<!-- Explain the need for this PR (Pull Request). -->\\n\",\n-       \" \\n\",\n-       \"<!-- Summarize changes made (Pull Request). -->\\n\",\n-       \" \\n\",\n-       \"## Tests added?\\n\",\n-       \"<!-- State test status and provide a brief description of the tests. -->\\n\",\n-       \"```\\n\",\n-       \"\\n\",\n-       \"# Your Task:\\n\",\n-       \"\\n\",\n-       \"1. Review the changes in the commit history above.\\n\",\n-       \"2. Fill out the Pull Request Template.\\n\"\n-      ],\n-      \"text/plain\": [\n-       \"<IPython.core.display.Markdown object>\"\n-      ]\n-     },\n-     \"execution_count\": 39,\n-     \"metadata\": {},\n-     \"output_type\": \"execute_result\"\n-    }\n-   ],\n-   \"source\": [\n-    \"# import markdown from jupyter\\n\",\n-    \"from IPython.display import Markdown\\n\",\n-    \"\\n\",\n-    \"Markdown(markdown_generator)\"\n-   ]\n-  }\n- ],\n- \"metadata\": {\n-  \"kernelspec\": {\n-   \"display_name\": \"git-genie\",\n-   \"language\": \"python\",\n-   \"name\": \"python3\"\n-  },\n-  \"language_info\": {\n-   \"codemirror_mode\": {\n-    \"name\": \"ipython\",\n-    \"version\": 3\n-   },\n-   \"file_extension\": \".py\",\n-   \"mimetype\": \"text/x-python\",\n-   \"name\": \"python\",\n-   \"nbconvert_exporter\": \"python\",\n-   \"pygments_lexer\": \"ipython3\",\n-   \"version\": \"3.10.14\"\n-  }\n- },\n- \"nbformat\": 4,\n- \"nbformat_minor\": 2\n-}\n\n---"
            }
        ]
    }
]
```

# Pull Request Template:

```markdown
## Why this PR and What changes?
<!-- Explain the need for this PR (Pull Request). -->
 
<!-- Summarize changes made (Pull Request). -->
 
## Tests added?
<!-- State test status and provide a brief description of the tests. -->
```

# Now perform the following tasks:

1. Review the changes in the commit history above.
2. Fill out the Pull Request Template.
3. Check which files are created, which ones are removed, and which ones are updated.
4. Then think step by step and ensure that your generated the correct PR description by checking the patch json content generated from git diff provided above.
5. Finally, create a pull request title that follows the semantic versioning standards.
