# READM_Agent

간단한 설명
- READM_Agent는 지정된 GitHub 레포지토리를 분석하여 자동으로 README 초안을 생성하고 PR로 제출하는 에이전트 기반 툴입니다. 여러 역할의 에이전트(`RepoManager`, `Analyst`, `TechExpert`, `Writer`)가 협업하여 코드베이스 구조·기능·기술 스택을 파악하고 문서를 작성합니다.

주요 기능
- 레포지토리 파일 트리 및 핵심 파일 수집
- 프로젝트 구조·목적 분석
- 기술 스택 및 아키텍처 요약 생성
- README 마크다운 초안 작성 및 깃허브에 PR 생성

빠른 시작
1. 의존성 설치

```bash
pip install -r requirements.txt
or
conda install --file requirements.txt
```

2. 환경 변수 설정
- 루트에 `.env` 파일을 만들고 다음 값을 설정하세요:
  - `MY_GITHUB_TOKEN` — GitHub API 토큰
  - `GEMINI_API_KEY` — 생성형 모델(예: Gemini) API 키

3. 실행

```bash
python main.py
```

기본 설정으로 `main.py` 내부의 `TARGET_REPO` 값을 분석 대상으로 사용합니다. 필요 시 해당 값을 수정하세요.

프로젝트 구조 (주요 파일)
- [main.py](main.py) — 실행 엔트리포인트
- [requirements.txt](requirements.txt) — 필요한 패키지
- [agents/repo_manager.py](agents/repo_manager.py) — 깃허브 추출/게시 담당 에이전트
- [agents/analyst.py](agents/analyst.py) — 프로젝트 분석 에이전트
- [agents/tech_expert.py](agents/tech_expert.py) — 기술 스택/아키텍처 분석
- [agents/writers.py](agents/writers.py) — README 작성 에이전트
- [tools/doc_gen.py](tools/doc_gen.py) — 문서 생성 보조 유틸리티

작동 흐름
1. `RepoManager`가 대상 레포지토리의 파일 트리를 수집하고 핵심 파일 내용을 가져옵니다.
2. `Analyst`가 코드·구조·목적을 분석하여 요약을 만듭니다.
3. `TechExpert`가 기술 스택과 아키텍처 관점에서 보완 분석을 수행합니다
4. `Writer`가 분석 결과를 바탕으로 README 마크다운을 생성합니다.
5. 최종 산출물을 `RepoManager`가 깃허브에 PR로 제출합니다.

환경 변수 및 보안
- API 토큰 및 키는 `.env`에 보관하고 절대 레포지토리에 커밋하지 마세요.

기여
- 이 프로젝트에 기여하고 싶다면 이슈를 열거나 PR을 보내주세요.

라이선스
- MIT
