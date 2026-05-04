class ReportAgent:
    def generate(self, data):
        print("生成团队级巡检报告...")
        print(f"扫描仓库：{data['total_repos']}")
        print(f"总文件数：{data['total_files']}")
        print(f"总问题数：{data['total_issues']}")
        print(f"高风险：{data['high_risk']}")
        print(f"本次消耗Token：{data['token_used']}")
        print("报告已保存：report.md")