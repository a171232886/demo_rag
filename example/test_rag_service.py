import os
os.chdir(os.path.dirname(__file__))

from demo_rag.service import RAGService
from demo_rag.card.config import Config


def test_rag_service_initialization():

    config = Config.from_yaml("config.yaml")

    # test initialization
    rag_service = RAGService(config.rag)

    # test build
    rag_service.clear()
    rag_service.build()

    # test retrieve
    data = rag_service.retrieve("什么是敏捷开发?")
    print(f"Retrieve results: {data}")

    # test upload file and download file
    BUCKET_NAME = config.rag.storage.file_store.bucket
    file_path = f"{BUCKET_NAME}/4.pdf"
    with open("data/4.pdf", "rb") as f:
        data = f.read()
    rag_service.upload_file(data, file_path)

    with open("download_4.pdf", "wb") as f:
        data = rag_service.download_file(file_path)
        f.write(data)

    # test add 
    rag_service.add(file_path)
    data = rag_service.retrieve("文后参考文献著录规则")
    print(f"Retrieve results: {data}")

    # test delete and delete_file
    rag_service.delete(file_path)
    rag_service.delete_file(file_path)

    # test clear
    rag_service.clear()
    

if __name__ == "__main__":
    test_rag_service_initialization()
    