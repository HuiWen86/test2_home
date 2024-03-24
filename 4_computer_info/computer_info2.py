#컴퓨터 정보 중에서 필요한 정보만 출력할 수 있게 수정
#씨피유, 코어개수, 메모리, c,d 용량,  통신 속도 
import psutil
cpu =  psutil.cpu_freq()
cpu_current_ghz = round(cpu.current/1000,2)
print("CPU:{}GHz".format(cpu_current_ghz))

cpu_core = psutil.cpu_count(logical=False)
print("CORE:{} ea".format(cpu_core))

memory = psutil.virtual_memory()
memory_total = round(memory.total/1024**3)
print("MEMORY:{} GB".format(memory_total))

disk = psutil.disk_partitions()
#for p in disk:
for i,p in enumerate(disk):
    if i == 0 or i == 1:
        print(p.mountpoint,p.fstype,end='')
        du = psutil.disk_usage(p.mountpoint)
        disk_total = round(du.total/1024**3) 
        print("DISK size:{} GB".format(disk_total))

net = psutil.net_io_counters()
sent= round(net.bytes_sent/1024**2,1)
recv = round(net.bytes_recv/1024**2,1)
print("NET: send:{} MB recv:{} MB".format(sent,recv))
