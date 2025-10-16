import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import matplotlib
matplotlib.use('Agg')  # usar backend sin interfaz gráfica
import matplotlib.pyplot as plt
import time, os, re

SAVE_PATH = '/root/ros2_ws/data/sensor_plot.png'

class PlotterNode(Node):
    def __init__(self):
        super().__init__('plotter_node')
        self.temps = []
        self.times = []
        self.start_time = time.time()
        self.subscription = self.create_subscription(String, 'sensor_data', self.listener_callback, 10)
        self.timer = self.create_timer(5.0, self.save_plot)
        os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)

    def listener_callback(self, msg):
        # extrae el número de la cadena
        match = re.search(r'(\d+)', msg.data)
        if match:
            temp = float(match.group(1))
            self.temps.append(temp)
            self.times.append(time.time() - self.start_time)

    def save_plot(self):
        if not self.temps:
            self.get_logger().info('Aún no hay datos para graficar.')
            return
        plt.figure()
        plt.plot(self.times, self.temps, marker='o')
        plt.xlabel('Tiempo [s]')
        plt.ylabel('Temperatura [°C]')
        plt.title('Temperatura del sensor')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(SAVE_PATH)
        plt.close()
        self.get_logger().info(f'Gráfico actualizado en: {SAVE_PATH}')

def main(args=None):
    rclpy.init(args=args)
    node = PlotterNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
