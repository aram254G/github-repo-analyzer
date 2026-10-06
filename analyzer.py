
import requests
import pandas as pd


def get_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"

    page = 1
    all_repos = []

    while True:
        params = {
            "per_page": 100,
            "page": page
        }

        response = requests.get(url, params=params)
        response.raise_for_status()

        page_repos = response.json()

        if not page_repos:
            break

        all_repos.extend(page_repos)

        page += 1

    return all_repos


def analyze_repositories(repos):
    analyzed = []

    for repo in repos:
        description = repo.get("description") or "No description"

        analyzed.append({
            "name": repo.get("name"),
            "language": repo.get("language"),
            "stars": repo.get("stargazers_count"),
            "description": description,
            "url": repo.get("html_url"),
            "forks": repo.get("forks_count")
        })

    return analyzed


def save_to_csv(repos):
    df = pd.DataFrame(repos)

    df.to_csv("repositories.csv", index=False)

    print("Saved to repositories.csv")


def main():
    username = "aram254G"

    repos = get_repositories(username)

    analyzed_repos = analyze_repositories(repos)

    save_to_csv(analyzed_repos)


if __name__ == "__main__":
    main()
