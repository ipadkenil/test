import os
dirPath = r"C:\git\DelftStack\content"
result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
print(result)