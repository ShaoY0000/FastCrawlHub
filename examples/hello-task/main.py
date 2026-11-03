from pathlib import Path


def main() -> None:
    """输出可观察日志，并生成一个可由 FastCrawlHub 收集的示例构件。"""
    print("hello from FastCrawlHub")
    output = Path("output")
    output.mkdir(exist_ok=True)
    (output / "result.txt").write_text("task completed\n", encoding="utf-8")
    print("artifact created: output/result.txt")


if __name__ == "__main__":
    main()

