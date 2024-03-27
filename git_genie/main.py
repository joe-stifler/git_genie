from .cli_handler import CLIHandler

def main():
    """
    Main function to execute the CLIHandler which processes command-line arguments and
    runs the GitGenie tool accordingly.
    """
    cli_handler = CLIHandler()
    cli_handler.run()

if __name__ == '__main__':
    main()
