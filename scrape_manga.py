#Les données sont sur le site https://myanimelist.net/character.php
import requests

count = 0

for i in range(1,14000,10):
    try:
        url = f"https://i2.wp.com/caps.pictures/198/6-castleinthesky/full/castleinthesky-disneyscreencaps.com-{i}.jpg?zoom=1.25&strip=all"
        r = requests.get(url, allow_redirects=True)
        count+=1
        open(f"image{count}.jpg", 'wb').write(r.content)
    except:
        print("error")

for i in range(1,15000,10):
    try:
        url = f"https://i2.wp.com/caps.pictures/199/7-mononoke-hime/full/mononoke-disneyscreencaps.com-{i}.jpg?zoom=1.25&strip=all"
        r = requests.get(url, allow_redirects=True)
        count+=1
        open(f"image{count}.jpg", 'wb').write(r.content)
    except:
        print("error")

for i in range(1,9800,10):
    try:
        url = f"https://i2.wp.com/caps.pictures/198/8-neighbor-totoro/full/neighbor-totoro-disneyscreencaps.com-{i}.jpg?zoom=1.25&strip=all"
        r = requests.get(url, allow_redirects=True)
        count+=1
        open(f"image{count}.jpg", 'wb').write(r.content) 
    except:
        print("error")
        
for i in range(1,11000,10):
    try:
        url = f"https://i1.wp.com/caps.pictures/201/0-arrietty/full/arrietty-disneyscreencaps.com-{i}.jpg?zoom=1.25&strip=all"
        r = requests.get(url, allow_redirects=True)
        count+=1
        open(f"image{count}.jpg", 'wb').write(r.content) 
    except:
        print("error")
    
for i in range(1,10000,10):
    try:
        url = f"https://i1.wp.com/caps.pictures/200/1-spirited-away/full/spirited-away-disneyscreencaps.com-{i}.jpg?zoom=1.25&strip=all"
        r = requests.get(url, allow_redirects=True)
        count+=1
        open(f"image{count}.jpg", 'wb').write(r.content)
    except:
        print("error")
    
for i in range(1,13000,10):
    try:
        url = f"https://i0.wp.com/caps.pictures/199/1-only-yesterday/full/only-yesterday-disneyscreencaps.com-{i}.jpg?strip=all"
        r = requests.get(url, allow_redirects=True)
        count+=1
        open(f"image{count}.jpg", 'wb').write(r.content)
    except:
        print("error")

for i in range(1,13000,10):
    try:
        url = f"https://i0.wp.com/caps.pictures/200/6-earthsea/full/earthsea-disneyscreencaps.com-{i}.jpg?zoom=1.25&strip=all"
        r = requests.get(url, allow_redirects=True)
        count+=1
        open(f"image{count}.jpg", 'wb').write(r.content)
    except:
        print("error")
    
for i in range(1,11000,10):
    try:
        url = f"https://i2.wp.com/caps.pictures/200/9-ponyo/full/ponyo-disneyscreencaps.com-{i}.jpg?zoom=1.25&strip=all"
        r = requests.get(url, allow_redirects=True)
        count+=1
        open(f"image{count}.jpg", 'wb').write(r.content)
    except:
        print("error")

for i in range(1,12000,10):
    try:
        url = f"https://i1.wp.com/caps.pictures/198/9-kiki-delivery/full/kiki-delivery-disneyscreencaps.com-{i}.jpg?zoom=1.25&strip=all"
        r = requests.get(url, allow_redirects=True)
        count+=1
        open(f"image{count}.jpg", 'wb').write(r.content)
    except:
        print("error")