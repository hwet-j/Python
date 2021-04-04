# 말뭉치 : 자연어 연구를목적으로 수집된 샘플 dataset
# 형태소 (단어로서 의미를 가지는 최소 단위) 분석 (한글) - 어근, 접두사, 접미사, 품사 형태로 분리한 데이터로 분석작업

from konlpy.tag import Kkma

kkma = Kkma()
print(kkma.sentences("국민의힘 주호영 원내대표는 이날 당 비상대책위원회 회의에서 문 대통령의 부산 방문을 “노골적인 선거행보”라고 평가하며 “4차, 5차 재난지원금 공세에도 마음이 안 놓였는지 ‘가덕도 신공항’과 ‘동남권 메가시티’로 더불어민주당을 지원하는 선거운동에 나선 것”이라고 일갈했다."))
print(kkma.nouns("국민의힘 주호영 원내대표는 이날 당 비상대책위원회 회의에서 문 대통령의 부산 방문을 “노골적인 선거행보”라고 평가하며 “4차, 5차 재난지원금 공세에도 마음이 안 놓였는지 ‘가덕도 신공항’과 ‘동남권 메가시티’로 더불어민주당을 지원하는 선거운동에 나선 것”이라고 일갈했다."))

print()
from konlpy.tag import Okt
okt = Okt()

print(okt.pos("국민의힘 주호영 원내대표는 이날 당 비상대책위원회 회의에서 문 대통령의 부산 방문을 “노골적인 선거행보”라고 평가하며 “4차, 5차 재난지원금 공세에도 마음이 안 놓였는지 ‘가덕도 신공항’과 ‘동남권 메가시티’로 더불어민주당을 지원하는 선거운동에 나선 것”이라고 일갈했다. 반가워요"))
print(okt.pos("국민의힘 주호영 원내대표는 이날 당 비상대책위원회 회의에서 문 대통령의 부산 방문을 “노골적인 선거행보”라고 평가하며 “4차, 5차 재난지원금 공세에도 마음이 안 놓였는지 ‘가덕도 신공항’과 ‘동남권 메가시티’로 더불어민주당을 지원하는 선거운동에 나선 것”이라고 일갈했다. 반가워요", stem=True))
# stem=True를 써주면 원형 어근으로 출력됨
print(okt.nouns("국민의힘 주호영 원내대표는 이날 당 비상대책위원회 회의에서 문 대통령의 부산 방문을 “노골적인 선거행보”라고 평가하며 “4차, 5차 재난지원금 공세에도 마음이 안 놓였는지 ‘가덕도 신공항’과 ‘동남권 메가시티’로 더불어민주당을 지원하는 선거운동에 나선 것”이라고 일갈했다."))
print(okt.morphs("국민의힘 주호영 원내대표는 이날 당 비상대책위원회 회의에서 문 대통령의 부산 방문을 “노골적인 선거행보”라고 평가하며 “4차, 5차 재난지원금 공세에도 마음이 안 놓였는지 ‘가덕도 신공항’과 ‘동남권 메가시티’로 더불어민주당을 지원하는 선거운동에 나선 것”이라고 일갈했다."))
 