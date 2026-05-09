고정된 리스트/데이터 상수화: tools/doc_gen.py 안의 validate_sections 함수의 required_sections나, doc_gen_prompt.py에 있는 tone 딕셔너리 같은 검증용/매핑용 데이터는 프로젝트가 커지면 관리가 힘들어집니다. 이를 constants.py라는 새로운 파일을 만들어서 관리하면 나중에 템플릿의 섹션이 변경되었을 때 한 곳에서만 변경하면 됩니다.

프롬프트 템플릿의 분리: agents/prompts 디렉토리에 잘 나누어 놓으셨으나, 프롬프트 내부의 규칙(예: classDef 규칙, JSON 구조 응답 지시어 등)이 여러 프롬프트에 중복될 여지가 보인다면 그 부분만 별도의 텍스트 상수로 분리하여 파이썬의 f-string 템플릿에 주입하는 식으로 재사용성을 높일 수 있습니다.
