# a=input()
# b=input()

# a = int(a)
# e=list(b)

# for i in range(len(e)-1,-1,-1):
#     c = e[i]
#     c = int(c)
#     d = a*c
#     print(d)

# b = int(b)

# print(a*b)

# a = input().split()
# b=0
# for i in range(len(a)):
#     b+=int(a[i])
# print(b)

# a = input().split()
# if int(a[0]) > int(a[1]):
#     print(">")
# elif int(a[0]) < int(a[1]):
#     print("<")
# else:print("==")

import requests
from bs4 import BeautifulSoup
import os

os.system("rmdir *test*")

url = input("problem number: ")

if "acm" not in url:
    url = f"https://www.acmicpc.net/problem/{url}"

html = requests.get(url, headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0"}).text
print(html, url)
document = BeautifulSoup(html)

i = 1

inputs = []
outputs = []
while True:
    tagin = document.body.find("pre", id=f"sample-input-{i}")
    tagout = document.body.find("pre", id=f"sample-output-{i}")
    if tagin is None or tagout is None:
        break

    inputs.append(tagin.text)
    outputs.append(tagout.text)

    i += 1

for index, (i, o) in enumerate(zip(inputs, outputs)):
    with open(f"test{index}", "w") as f:
        f.write(i)
    with open(f"output_test{index}", "w") as f:
        f.write(o)