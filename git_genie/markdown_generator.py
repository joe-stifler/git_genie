import sys
import json
import logging

class MarkdownGenerator:
    """
    A class to generate Markdown descriptions from commit history data.

    Methods
    -------
    generate_pr_description(commit_history)
        Produces a Markdown string with a detailed description of each commit.
    """

    @staticmethod
    def generate_pr_description(commit_history, template_path):
        """
        Generates a detailed Pull Request description in Markdown format 
        from a list of commit information dictionaries.

        Parameters
        ----------
        commit_history : list of dict
            The commit history as a list of dictionaries, with each dictionary
            containing details of a commit and associated changes.
        template_path : str
            The path to the Pull Request template file.

        Returns
        -------
        str
            A string in Markdown format describing the commits.

        """
        markdown_content = '# Commit History and Git Patch Changes for files (git diff):\n\n```json\n'
        markdown_content += json.dumps(commit_history, indent=4, sort_keys=False)
        markdown_content += '\n```\n'
        
        markdown_content  += '\n# Pull Request Template:\n\n```markdown\n'

        try:
            with open(template_path, 'r', encoding="utf-8") as f:
                markdown_content += f.read()
        except FileNotFoundError:
            logging.warning("Failed to read the Pull Request template file at: %s", template_path)
            sys.exit(1)

        markdown_content += '```\n'
        
        markdown_content += '\n# Now perform the following tasks:\n\n'
        markdown_content += '1. Review the changes in the commit history above.\n'
        markdown_content += '2. Fill out the Pull Request Template.\n'
        markdown_content += '4. Check which files are created, which ones are removed, and which ones are updated.\n'
        markdown_content += '3. Then think step by step and ensure that your generated the correct PR description by checking the patch json content generated from git diff provided above.\n'

        return markdown_content
