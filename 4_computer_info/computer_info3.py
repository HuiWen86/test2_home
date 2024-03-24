#1초마다 반복해서 컴퓨터 정보 출력하는 코드. 
import psutil

curr_sent = 0 
curr_recv = 0

prev_sent = 0
prev_recv = 0

while True:
    cpu_p = psutil.cpu_percent(interval=1)
    print("CPU usage:{} %".format(cpu_p))

    memory = psutil.virtual_memory()
    memory_avail = round(memory.available/1024**3,1)
    print("available memory:{} GB".format(memory_avail))

    net = psutil.net_io_counters()
    curr_sent = net.bytes_sent/1024**2
    curr_recv = net.bytes_recv/1024**2

    sent = round(curr_sent-prev_sent,1)
    recv = round(curr_recv-prev_recv,1)

    print("send:{} MB, recv:{} MB".format(sent,recv))
    print(" ")
    prev_sent = curr_sent
    prev_recv = curr_recv
