import anthropic

client = anthropic.Anthropic()

# 대화 기록을 저장할 리스트
conversation = []

# 사용자 입력 추가
conversation.append({
    "role": "user",
    "content": "안녕 나는 영택이야."
})

# 클로드 호출
response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1000,
    messages=conversation
)

# 응답 출력 및 대화 기록에 추가
assistant_message = response.content[0].text
print(assistant_message)
conversation.append({
    "role": "assistant",
    "content": assistant_message
})

# 다음 사용자 입력
conversation.append({
    "role": "user",
    "content": "내 이름이 뭐라고?"
})

# 다시 클로드 호출
response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1000,
    messages=conversation
)

# 두 번째 응답 출력
print(response.content[0].text)
