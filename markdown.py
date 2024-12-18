#環境インストール
#pip install markitdown

from markitdown import MarkItDown

markitdown = MarkItDown()
result = markitdown.convert("test_wikipedia.html")
print(result.text_content)


###### 画像をmarkdown化する #######

#環境変数の設定
#使用前にAPIキーを設定してください
# cmd:
# set OPENAI_API_KEY=sk-xxxx
# 
# power shell:
# $env:OPENAI_API_KEY = "sk-xxxx"

# from markitdown import MarkItDown
# from openai import OpenAI
# import os

# #有料プランに加入しない限りこのコードは動作しません

# OpenAI.api_key = os.environ["OPENAI_API_KEY"]
# print(os.environ["OPENAI_API_KEY"])
# client = OpenAI()
# md = MarkItDown(llm_client=client, llm_model="gpt-3.5-turbo")
# result = md.convert("top_kv_04.jpg")
# print(result.text_content)