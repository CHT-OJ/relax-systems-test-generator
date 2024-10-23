'''
MIT License

Copyright (c) 2023 iotran207, is forked and edited by ntannn

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

AUTHOR King.#4732
'''
import os
import random
import shutil
import time
import subprocess
import sys

def make_random(start:int,end:int) -> int:
    return random.randint(start,end)
    
def make_input(file_name:str,start_line:int,end_line:int,start_random:int,end_random:int) -> None:
    content:str = ""
    with open(f"{file_name}.inp","w+") as file:
        for _line in range(random.randint(start_line,end_line)):
            content += f"{make_random(start=start_random,end=end_random)} {make_random(start=start_random,end=end_random)} {make_random(start=start_random,end=end_random)} {make_random(start=start_random,end=end_random)}\n"
        file.write(content)
        file.close()

if __name__ == "__main__":
    mode:int = 2
    if mode == 2:
        try:
            file_name = "code"
            for _test_file in os.listdir("inp"):
                _test = _test_file.split(".")[0]
                os.mkdir(f"out/test{_test}")
                os.rename(f"inp\\{_test_file}", f"inp\\{file_name}.inp")
                shutil.move(f"inp\\{file_name}.inp", f"{file_name}.inp")
                with open(f"{file_name}.out", "w") as file:
                    file.close()
                process = subprocess.run(f".\\code\\compile\\code.exe", shell=True)
                shutil.move(f"{file_name}.inp", f"out/test{_test}/{file_name}.inp")
                shutil.move(f"{file_name}.out", f"out/test{_test}/{file_name}.out")
                print("test", _test,"ok!")
        except Exception as error:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)