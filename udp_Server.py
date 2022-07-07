import socket

def main():
	# 创建套接字
	udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # udp IPV4			tcp  IPV4
	# 绑定本地信息
	udp_socket.bind(('',8000))
	# 创建循环事件,为了使能不断接收数据。。。。。。。客户端只要发消息 我就能收到。
	while 1:
		# 接收终端的数据
		recv_data_T,address = udp_socket.recvfrom(1024)		# 接收温度
		recv_data_W,address = udp_socket.recvfrom(1024)		# 接收湿度
		recv_data_L,address = udp_socket.recvfrom(1024) 	# 接收环境照度

		# 退出数据传送判断
		# if not recv_data_T_A:
		if recv_data_T == b'#' or recv_data_W == b'#' or recv_data_L == b'#':
			break
		#判断是否满足开灯条件
		elif recv_data_T == b'20' and recv_data_L == b'5' and recv_data_W == b'25':
			udp_socket.sendto(b"open",address)
		elif recv_data_T != b'20' or recv_data_L != b'5' or recv_data_W != b'25':
			udp_socket.sendto(b"close",address)
		
	# 关闭套接字
	udp_socket.close()

if __name__ == "__main__":
	main()