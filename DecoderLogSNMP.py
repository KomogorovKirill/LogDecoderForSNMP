#!/usr/bin/python3
# -*- coding: utf-8 -*-

from fastapi import FastAPI
import uvicorn
import asyncio

app = FastAPI()

@app.get("/{log}")
async def GetDecodeLogOfSNMP(log):
    log = log.split(" ")
    message = bytearray()
    for byte in log:
        message.append(int(byte, 16))
    message = message.decode("windows-1251")
    backup = open(".backup_log", "a", encoding="utf-8")
    backup.write("\n" + message)
    backup.close()
    return {"decode_log": message}

if __name__ == "__main__":
    uvicorn.run(app)
