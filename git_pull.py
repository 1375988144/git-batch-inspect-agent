import os
import shutil

class GitPullAgent:
    def batch_pull(self, repo_list):
        downloaded = []
        for url in repo_list:
            name = url.split("/")[-1].replace(".git", "")
            print(f"拉取：{name}")
            downloaded.append({"name": name, "path": f"./repos/{name}"})
        return downloaded