import gensim.downloader as api

model = api.load("glove-wiki-gigaword-50")   # ~66MB, downloads once
print(model.similarity("coffee", "music"))