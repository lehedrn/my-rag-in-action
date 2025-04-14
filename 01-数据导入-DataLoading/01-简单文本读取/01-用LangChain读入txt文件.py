from langchain_community.document_loaders import TextLoader

# 加载单个txt文件，指定编码为utf-8
loader = TextLoader('90-文档-Data/黑悟空/设定.txt', encoding='utf-8')
documents = loader.load()

# 输出加载的文档内容
print(documents)
print("-----------------")
for doc in documents:
    print(doc.page_content)
