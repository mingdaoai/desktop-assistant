#!/usr/bin/env python

import os
import subprocess

def read_anthropic_key():
    try:
        with open(os.path.expanduser('~/.mingdaoai/anthropic.key'), 'r') as file:
            key = file.read().strip()
            return key
    except FileNotFoundError:
        print("Anthropic key file not found. Please create an API key from https://console.anthropic.com/settings/keys and save it to ~/.mingdaoai/anthropic.key.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the key: {e}")
        return None


def start_desktop():
    api_key = read_anthropic_key()
    if not api_key:
        print("Cannot start desktop without a valid API key.")
        return

    # Set the environment variable for the API key
    os.environ['ANTHROPIC_API_KEY'] = api_key

    # Run the docker command
    try:
        command = [
            'docker', 'run',
            '-e', f'ANTHROPIC_API_KEY={os.environ["ANTHROPIC_API_KEY"]}',
            '-v', f'{os.path.expanduser("~")}/.anthropic:/home/computeruse/.anthropic',
            '-p', '5900:5900',
            '-p', '8501:8501',
            '-p', '6080:6080',
            '-p', '8080:8080',
            '-it', 'ghcr.io/anthropics/anthropic-quickstarts:computer-use-demo-latest'
        ]
        print("Running command:", ' '.join(command))
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the docker command: {e}")


if __name__ == "__main__":
    start_desktop()
