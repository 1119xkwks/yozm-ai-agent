from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["article", "style"],
    template="다음 기사를 {style} 스타일로 요약하세요:\n\n{article}",
)
print(template.format(article="OpenAI가 GPT-5를 공개했다...", style="뉴스"))