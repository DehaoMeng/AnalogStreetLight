import socket

def main():
	print("正在启动服务端")
	# 创建套接字
	udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # udp IPV4			tcp  IPV4
	# 绑定本地信息
	udp_socket.bind(('',8000))
	print("启动成功")
	# 创建循环事件,为了使能不断接收数据。。。。。。。客户端只要发消息 我就能收到。
	while 1:
		# 接收终端的数据
		recv_data_T,address = udp_socket.recvfrom(1024)		# 接收温度
		recv_data_W,address = udp_socket.recvfrom(1024)		# 接收湿度
		recv_data_L,address = udp_socket.recvfrom(1024) 	# 接收环境照度
		print("您接收到来自" + address[0] + "的数据为")
		print("温度为:" + recv_data_T.decode('utf-8'))
		print("湿度为:" + recv_data_W.decode('utf-8') + "%")
		print("亮度为:" + recv_data_L.decode('utf-8'))

		# 退出数据传送判断
		if recv_data_T == b'#' or recv_data_W == b'#' or recv_data_L == b'#':
			break
		#判断是否满足开灯条件
		if recv_data_T <= b'15' and recv_data_W <= b'50' or recv_data_L <= b'30':
			udp_socket.sendto(b"open",address)
		elif recv_data_T != b'20' or recv_data_L != b'5' or recv_data_W != b'25':
			udp_socket.sendto(b"close",address)
		
	# 关闭套接字
	udp_socket.close()

if __name__ == "__main__":
	main()