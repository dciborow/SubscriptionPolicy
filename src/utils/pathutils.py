import os
from .jsonloader import JsonFileUtil

class PathUtils:
    @staticmethod
    def ensure_path(directory_path: str):
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

    @staticmethod 
    def load_json_files(directory_path: str):
        file_list = []
        for root, dirs, files in os.walk(directory_path, topdown=False):
            for name in files:
                file_name = os.path.join(root, name)
                file_list.append(JsonFileUtil.read_file_as_json(file_name))
        return file_list