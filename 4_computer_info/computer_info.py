import psutil
cpu = psutil.cpu_freq()
print("**cpu_info:",cpu,"추가설명: current:현재 cpu 주파수, min: cpu의 최소 주파수, max: cpu 최대 주파수--> cpu가 가장 높은 성능 발휘할 때 주파수")

cpu_core = psutil.cpu_count(logical=False)
print("**cpu_core_info:",cpu_core,"추가설명: 사용가능한 cpu 코어 수, 코어가 많을 수록 병렬처리, 다중 쓰레드 프로그램에서 유리")

memory = psutil.virtual_memory()
print("**memory_info:",memory,"추가설명: total: 총 시스템 메모리용량, available:현재 사용가능한 용량, percent=현재 메모리 사용량(%),used:사용량 수치, free: 사용가능한 메모리 ")

disk = psutil.disk_partitions()
print("**disk_info:",disk,"추가설명: device: 디스크 장치 경로, mountpoint:디스크 디렉토리, fstype:파일시스템유형,\
      opts:디스크마운트옵션,maxfile:저장할수있는 최대파일수,maxpath:저장할 수 있는 최대경로길이")

net = psutil.net_io_counters()
print("**net_info:",net,"추가설명: bytes_sent:전송된 바이트 수, bytes_recv: 수신된 바이트 수, packets_sent:전송된 패킷 수, \
      packets_recv:수신된 패킷 수, errin:수신 중에 발생한 오류 수, errout: 전송 중에 발생한 오류 수, dropin: 수신 중에 삭제된 패킷 수, dropout: 전송 중에 삭제된 패킷 수")