import subprocess
import sys

STEPS = [
    "export_likes.py",
    "filter_beats.py",
    "create_playlist.py",
    "add_beats_to_playlist.py",
]


def main():
    for step in STEPS:
        print(f"\n=== Running {step} ===")

        result = subprocess.run([sys.executable, step])

        if result.returncode != 0:
            print(f"\n{step} failed, stopping pipeline.")
            sys.exit(result.returncode)

    print("\nPipeline complete.")


if __name__ == "__main__":
    main()
