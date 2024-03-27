import logging
import argparse
import pyperclip

from .git_repo import GitRepo
from .markdown_generator import MarkdownGenerator


class CLIHandler:
    """
    A class to handle command-line interface operations for the GitGenie tool.

    This class uses argparse to parse command-line arguments and execute the appropriate
    functionalities provided by GitRepo and MarkdownGenerator classes.

    Methods
    -------
    run()
        Executes the CLI based on the parsed arguments.
    """

    def __init__(self):
        """
        Initializes the CLIHandler with an argument parser.
        Sets up the expected command-line arguments.
        """
        self.parser = argparse.ArgumentParser(description="GitGenie CLI")
        self._setup_cli_arguments()

    def _setup_cli_arguments(self):
        """
        Internal method to setup CLI argument parsing.
        """
        self.parser.add_argument(
            "-b",
            "--branch",
            default=None,  # No default value; will use the current branch if not provided
            help="The branch to generate PR description for. Defaults to the current branch if not specified.",
        )
        self.parser.add_argument(
            "-r",
            "--repo-path",
            default=".",
            help="Path to the local Git repository (default: current directory).",
        )
        self.parser.add_argument(
            "-t",
            "--template-path",
            default=".github/pull_request_template.md",
            help="Path to the Pull Request template (default: .github/pull_request_template.md).",
        )
        self.parser.add_argument(
            "-o",
            "--output-file",
            default="",
            help="Path to the output file to write the markdown description (optional).",
        )
        self.parser.add_argument(
            "-v",
            "--verbose",
            default="INFO",
            choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
            help="Set the logging level (default: INFO).",
        )
        self.parser.add_argument(
            "-c",
            "--start-commit",
            default=None,
            help="The commit hash to start the commit history from. Only commits newer than this will be included.",
        )

        self.args = self.parser.parse_args()

        logging.basicConfig(level=self.args.verbose)

    def run(self):
        """
        Executes the CLI based on the parsed arguments. It retrieves the commit history
        from the specified branch and generates a Markdown-formatted PR description.
        """
        git_repo = GitRepo(self.args.repo_path)

        # If no branch is specified, use the current active branch
        branch_name = self.args.branch or git_repo.repo.active_branch.name

        commit_history = git_repo.get_commit_history(
            branch_name, start_commit_hash=self.args.start_commit
        )

        if commit_history:
            markdown_description = MarkdownGenerator.generate_pr_description(
                commit_history, self.args.template_path
            )
            print(markdown_description)

            # Ask the user if they want to copy the output to the clipboard
            should_copy = (
                input(
                    "Would you like to copy the markdown description to the clipboard? (y/n): "
                )
                .strip()
                .lower()
            )

            if should_copy == "y":
                pyperclip.copy(markdown_description)
                logging.info("Markdown description has been copied to clipboard.")
            elif should_copy == "n" and self.args.output_file:
                with open(self.args.output_file, "w", encoding="utf-8") as f:
                    f.write(markdown_description)
                    logging.info(
                        "Markdown description has been written to %s.",
                        self.args.output_file,
                    )
            else:
                logging.error(
                    "Markdown description has not been copied to clipboard or written to file."
                )

        else:
            logging.warning(
                f"No commit history found for the specified branch: {branch_name}"
            )
