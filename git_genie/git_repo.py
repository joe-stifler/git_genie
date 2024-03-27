from git import Repo


class GitRepo:
    """
    Interface to a Git repository, providing access to the repository's commit history.

    Parameters
    ----------
    path : str, optional
        The file system path to the Git repository. Defaults to the current directory.

    Attributes
    ----------
    repo : git.Repo
        The GitPython Repo object.

    Methods
    -------
    get_commit_history(branch_name, main_branch_name='main')
        Retrieves the commit history for a given branch not merged into the main branch.
    """

    def __init__(self, path="."):
        """
        Initialize a GitRepo object.

        Parameters
        ----------
        path : str, optional
            The file system path to the Git repository. Defaults to the current directory.
        """
        self.repo = Repo(path)

    def get_commit_history(
        self, branch_name, main_branch_name="main", start_commit_hash=None
    ):
        """
        Retrieves a list of commits in the branch that are not in the main branch
        and are newer than the specified start_commit_hash.

        Parameters
        ----------
        branch_name : str
            The name of the branch to retrieve the commit history for.
        main_branch_name : str, optional
            The name of the main branch to compare against. Defaults to 'main'.
        start_commit_hash : str, optional
            The hash of the commit to start the history from. If specified, only commits
            newer than this commit will be included. Defaults to None.

        Returns
        -------
        list of dict
            A list of dictionaries, each representing a commit with its details
            and associated changes.

        Examples
        --------
        >>> repo = GitRepo('/path/to/repo')
        >>> commit_history = repo.get_commit_history('feature-branch')
        >>> print(commit_history[0]['message'])
        Initial commit message
        """
        if start_commit_hash:
            commits = list(self.repo.iter_commits(f"{start_commit_hash}.."))
        else:
            commits = list(self.repo.iter_commits(f"{main_branch_name}..{branch_name}"))

        commit_history = []

        for commit in commits[::-1]:  # List from oldest to newest
            all_file_changes = self._get_commit_files(commit)

            commit_info = {
                "hash": commit.hexsha,
                "message": commit.message.strip(),
                "author": commit.author.name,
                "author_email": commit.author.email,
                "timestamp": commit.committed_datetime.isoformat(),
                "parents": [parent.hexsha for parent in commit.parents],
                "all_file_changes": all_file_changes,
            }
            commit_history.append(commit_info)

        return commit_history

    def _get_commit_files(self, commit):
        """
        Helper method to retrieve file changes for a specific commit.

        Parameters
        ----------
        commit : git.Commit
            The commit object to retrieve file changes from.

        Returns
        -------
        list of dict
            A list of dictionaries each representing a file's changes.
        """
        all_file_changes = []
        for diff in commit.diff(
            commit.parents[0] if commit.parents else None, create_patch=True
        ):
            file_change = {
                "file_path": diff.b_path if diff.new_file else diff.a_path,
                "deleted_file": diff.deleted_file,
                "new_file": diff.new_file,
                "copied_file": diff.copied_file,
                "rename_from": diff.rename_from,
                "rename_to": diff.rename_to,
                "updated_file": not (
                    diff.deleted_file
                    or diff.new_file
                    or diff.copied_file
                    or diff.rename_from
                    or diff.rename_to
                ),
                "changes": str(diff),
            }
            all_file_changes.append(file_change)
        return all_file_changes

    def _get_diff_lines(self, diff):
        """
        Helper method to parse the diff of a file.

        Parameters
        ----------
        diff : git.Diff
            The diff object to parse changes from.

        Returns
        -------
        str
            A string representing the diff of the file.
        """
        return diff.diff.decode("utf-8")
