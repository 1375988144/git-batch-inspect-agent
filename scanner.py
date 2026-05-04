class CodeScanAgent:
    def scan_repos(self, repos):
        result = []
        for repo in repos:
            print(f"扫描仓库：{repo['name']}")
            # 高Token消耗：全量AST解析、文件扫描
            result.append({
                "repo": repo["name"],
                "files": 320,
                "code_smells": 18,
                "security_risks": 3,
                "unused_codes": 12,
                "format_errors": 41
            })
        return result