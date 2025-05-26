import sys
import time
import subprocess
from colorama import init, Fore, Style

init(autoreset=True)

def print_error(message: str):
    print(f"\n{Fore.RED}[ERROR]{Style.RESET_ALL} {message}")

def print_time(label: str, seconds: float):
    print(f"\n{Fore.GREEN}{label:<15}:{Style.RESET_ALL} {seconds:.6f} sec")

def main():
    if len(sys.argv) < 2:
        print_error("Usage: wtime <command>")
        sys.exit(1)

    command = sys.argv[1:]

    try:
        start = time.perf_counter()
        result = subprocess.run(command, shell=True)
        end = time.perf_counter()

        elapsed = end - start
        print_time("Real Time", elapsed)
        sys.exit(result.returncode)

    except FileNotFoundError:
        print_error(f"Command not found: {command[0]}")
        sys.exit(127)
    except Exception as e:
        print_error(f"Failed to execute command: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
