#custom function/method 函式, 函數
def get_todos(filename="files/todos.txt"):
    """
    讀取文字檔案的備忘錄資料, 回傳list
    """
    with open(filename, "r", encoding="utf-8") as file: #content manager
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_local, filename="files/todos.txt"):
    """
    將備忘錄資料寫入文字檔案
    """
    with open(filename, "w", encoding="utf-8") as file: #開啟檔案寫入資料
        file.writelines(todos_local)

#print("Hi!!!")