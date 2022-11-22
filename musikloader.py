from pathlib import Path

class musikloader:
    def __init__(self, url: str):
        """ 
        constructor 
        str url: the channel url to be downloaded
        """
        self.url = url

    def update_url(self, url: str):
        """
        updates the channel url
        str url: the channel url
        """
        self.url = url
    
    def download(self, path: str = './download'):
        """
        starts the download progress
        str path: the target directory to download files to
        """
        base_dir = Path(path)
        print(base_dir)


if __name__ == "__main__":
    ml = musikloader("horden")
    ml.download()
