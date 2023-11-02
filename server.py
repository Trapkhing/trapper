from waitress import serve
def trap():
    return "Trap"
host="0.0.0.0"
port=8080
serve(trap,host=host,port=port)