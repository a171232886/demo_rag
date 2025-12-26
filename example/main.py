from demo_rag import DEMORAG


def main():
    server = DEMORAG(config_path="config.yaml")
    server.run()


if __name__ == "__main__":
    main()
    
