#!/bin/env python

import xml.etree.cElementTree as ET
import os
import shutil

nuspacker = "../nuspacker/NUSPacker.jar"    # Set path to NUSPacker.jar here. will be downloaded if empty

# Don't edit below this line

def checkAndDeleteFile(file):
    if os.path.exists(file):
        print(f"Deleting {file}")
        os.remove(file)

def checkAndDeleteDir(dir):
    if os.path.exists(dir):
        print(f"Deleting {dir}")
        shutil.rmtree(dir)

checkAndDeleteDir("out")

tmpArray = ["out/sohfw", "tmp/code", "tmp/content"]
for path in tmpArray:
    os.makedirs(path)

os.system(f"make -j$(nproc)")
shutil.copytree("meta", "tmp/meta")
for root, dirs, files in os.walk("tmp/meta"):
    for file in files:
        if file.endswith(".xcf"):
            print(os.path.join(root, file))
            os.remove(os.path.join(root, file))

tmpArray = ["soh.rpx", "tmp/meta/app.xml",  "tmp/meta/cos.xml"]
for file in tmpArray:
    shutil.move(file, "tmp/code")

fp = open('tmp/content/dummy', 'x')
fp.close()
os.system(f"java -jar {nuspacker} -in tmp -out out/sohfw")
shutil.rmtree("tmp")
