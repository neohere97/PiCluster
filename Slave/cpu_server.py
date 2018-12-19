import psutil
from flask import Flask,request

app = Flask(__name__)

@app.route('/getCPU', methods=['POST'])
def getCPU():
   return str(psutil.cpu_percent(percpu=False))

@app.route('/getCPUTemp', methods=['POST'])
def getCPUTemp():            
    return str(psutil.sensors_temperatures()['cpu-thermal'][0][1])

    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
