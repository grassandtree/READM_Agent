from constants import JSON_OUTPUT_INSTRUCTION, MERMAID_CLASSDEF_RULES


TECH_EXPERT_PROMPT_TEMPLATE = """
너는 숙련된 시스템 아키텍트이자 기술 면접관이야. 
analyst 에이전트가 정리한 아래의 [REPOSITORY CONTEXT]를 분석해서 기술 스택 분류와 시스템 아키텍처를 정리해줘.

[REPOSITORY CONTEXT]
{analysis_context}

[요구사항]
1. 기술 스택 분류: Frontend, Backend, Database, DevOps/Infra 등으로 나누어 정리해.
2. 기술 선택 이점: 각 기술 옆에 "이 기술을 사용해서 얻은 이점"을 초보 개발자의 포트폴리오용으로 한 문장씩 덧붙여줘.

3. 아키텍처 도식화 (Mermaid.js 필수 규칙):
""" + MERMAID_CLASSDEF_RULES + """

4. 주요 라이브러리 버전: 설정 파일에 명시된 버전이 있다면 함께 적어줘.

[출력 형식]
""" + JSON_OUTPUT_INSTRUCTION + """
{{
  "tech_summary": {{
    "tech_stack": {{
      "Frontend": ["기술 (이점)", ...],
      "Backend": ["기술 (이점)", ...],
      "DevOps": ["기술 (이점)", ...]
    }},
    "architecture_summary": "전체 구조 요약",
    "mermaid_code": "graph TD\\n    classDef... (여기에 위 규칙을 준수한 코드 작성)",
    "key_points": ["포인트 1", "2"]
  }}
}}
"""