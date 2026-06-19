import json
import sys
from datetime import datetime

SITE_DATA = {
    "title": "华体会体育资讯",
    "url": "https://panel-cn-hth.com",
    "keywords": ["华体会", "体育竞猜", "赛事推荐", "实时比分"],
    "tags": ["体育", "娱乐", "资讯"],
    "description": "提供华体会平台最新体育赛事动态、即时比分与竞猜推荐服务。",
    "last_updated": "2025-03-15"
}

def format_summary(data: dict) -> str:
    lines = []
    lines.append(f"站点名称: {data['title']}")
    lines.append(f"访问地址: {data['url']}")
    lines.append(f"核心关键词: {', '.join(data['keywords'])}")
    lines.append(f"内容标签: {', '.join(data['tags'])}")
    lines.append(f"简要说明: {data['description']}")
    lines.append(f"最后更新: {data['last_updated']}")
    return "\n".join(lines)

def build_structured_dict(data: dict) -> dict:
    return {
        "meta": {
            "source": data["url"],
            "generated_at": datetime.now().isoformat(timespec="seconds")
        },
        "content": {
            "name": data["title"],
            "keywords": data["keywords"],
            "tags": data["tags"],
            "description": data["description"]
        }
    }

def output_json(data: dict) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=2))

def output_plain(data: dict) -> None:
    print(format_summary(data))

def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1] == "--json":
        structured = build_structured_dict(SITE_DATA)
        output_json(structured)
    else:
        output_plain(SITE_DATA)

if __name__ == "__main__":
    main()