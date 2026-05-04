
from core.git_pull import GitPullAgent
from core.scanner import CodeScanAgent
from core.analyzer import AnalyzeAgent
from core.reporter import ReportAgent
import config

def main():
    print("=" * 60)
    print(" Git 仓库批量智能巡检工具 ")
    print(" 日均Token消耗：约 600万 ")
    print("=" * 60)

    # 1. 批量拉取代码
    print("\n[步骤1] 批量拉取Git仓库...")
    git_agent = GitPullAgent()
    repos = git_agent.batch_pull(config.REPO_LIST)

    # 2. 代码扫描
    print("\n[步骤2] 代码深度扫描（高Token消耗）...")
    scan_agent = CodeScanAgent()
    scan_results = scan_agent.scan_repos(repos)

    # 3. AI智能分析（长链推理）
    print("\n[步骤3] AI长链分析问题...")
    analyze_agent = AnalyzeAgent()
    analyze_result = analyze_agent.analyze(scan_results)

    # 4. 生成报告
    print("\n[步骤4] 生成巡检报告...")
    report_agent = ReportAgent()
    report_agent.generate(analyze_result)

    print("\n✅ 全部仓库巡检完成！")

if __name__ == "__main__":
    main()