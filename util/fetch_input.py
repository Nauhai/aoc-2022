import sys
import requests
import os
import dotenv


dotenv.load_dotenv()


def fetch_input(day, session_cookie):
    if day < 1 or 25 < day:
        raise ValueError("Day must be between 1 and 25")

    url = f"https://adventofcode.com/2022/day/{day}/input"
    headers = {"Cookie": f"session={session_cookie}"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise RuntimeError(f"Cannot fetch input ({response.status_code}): {response.content}")

    input_path = f"src/input/day{day:02}.txt"
    with open(input_path, 'w') as file:
        file.write(response.content.decode("utf-8"))


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("No input to retrieve. Goodbye!")
        sys.exit()

    day = int(sys.argv[1])

    if not "SESSION_COOKIE" in os.environ:
        raise KeyError("Session cookie not set.")

    session_cookie = os.environ["SESSION_COOKIE"]
    fetch_input(day, session_cookie)

    print(f"Successfully fetched input for day {day:02}!")
