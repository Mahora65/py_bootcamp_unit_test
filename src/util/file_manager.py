import os

def save_file(upload_file, path):
    with open(path, 'wb') as f:
        f.write(upload_file.getvalue())

if __name__ == '__main__':
    print("this is main")
