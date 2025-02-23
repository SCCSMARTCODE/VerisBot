from dotenv import load_dotenv
load_dotenv()


from fastapi import FastAPI
from psutil import virtual_memory, swap_memory, disk_usage, net_io_counters
from backend_server.routes.veris_core import core_router
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()
app.include_router(core_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "status": "success",
        "message": "welcome to VeriS"
    }



@app.get("/health-check")
def health():
    return {"status": "ok"}


@app.get("/verbose/health-check")
def verbose_health():
    mem = virtual_memory()
    return {
        "status": "ok",
        "virtual-memory": {
            "total": mem.total,
            "available": mem.available,
            "used": mem.used,
            "percent": mem.percent,
        },
        "swap-memory": {
            "total": swap_memory().total,
            "used": swap_memory().used,
            "free": swap_memory().free,
            "percent": swap_memory().percent,
            "sin": swap_memory().sin,
            "sout": swap_memory().sout,
        },
        "disk-usage": {
            "total": disk_usage("/").total,
            "used": disk_usage("/").used,
            "free": disk_usage("/").free,
            "percent": disk_usage("/").percent,
        },
        "network-io-counters": net_io_counters(),
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)