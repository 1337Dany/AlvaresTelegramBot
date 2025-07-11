from fastapi import FastAPI, WebSocket
import asyncio

app = FastAPI()
LOG_FILE = "var/logs/my_app.log"

#Controller responsible for data transmission via websocket.
#this endpoint looks at changes in log file and sends it by request of user
@app.websocket("/ws/logs")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    open("var/logs/my_app.log", "w").close()
    with open(LOG_FILE, "r") as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if line:
                await websocket.send_text(line)
            else:
                await asyncio.sleep(0.5)
