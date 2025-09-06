"""
客户端测试代码 - 模拟用户如何使用你的API
这个文件展示了如何像使用库一样使用你的API
"""
import requests
import json

# API基础URL（部署后需要替换为实际的云端地址）
API_BASE_URL = "http://localhost:8000"  # 本地测试
# API_BASE_URL = "https://your-api.herokuapp.com"  # 云端部署后

class CloudAPIClient:
    """云端API客户端 - 就像使用一个库一样"""
    
    def __init__(self, base_url: str = API_BASE_URL):
        self.base_url = base_url
    
    def add_numbers(self, a: int, b: int) -> int:
        """加法运算 - 用户只需要传入参数，获得结果"""
        response = requests.post(
            f"{self.base_url}/math/add",
            json={"a": a, "b": b}
        )
        response.raise_for_status()
        return response.json()["result"]
    
    def multiply_numbers(self, a: float, b: float) -> float:
        """乘法运算"""
        response = requests.post(
            f"{self.base_url}/math/multiply",
            params={"a": a, "b": b}
        )
        response.raise_for_status()
        return response.json()["result"]
    
    def power_numbers(self, base: float, exponent: float) -> float:
        """幂运算"""
        response = requests.post(
            f"{self.base_url}/math/power",
            params={"base": base, "exponent": exponent}
        )
        response.raise_for_status()
        return response.json()["result"]
    
    def process_text(self, text: str, operation: str) -> dict:
        """文本处理"""
        response = requests.post(
            f"{self.base_url}/text/process",
            json={"text": text, "operation": operation}
        )
        response.raise_for_status()
        return response.json()
    
    def calculate_statistics(self, numbers: list) -> dict:
        """数据统计"""
        response = requests.post(
            f"{self.base_url}/stats/calculate",
            json={"numbers": numbers}
        )
        response.raise_for_status()
        return response.json()
    
    def health_check(self) -> dict:
        """健康检查"""
        response = requests.get(f"{self.base_url}/health")
        response.raise_for_status()
        return response.json()

def main():
    """演示如何使用API客户端"""
    print("=== 云端API客户端测试 ===\n")
    
    # 创建客户端实例
    client = CloudAPIClient()
    
    try:
        # 测试健康检查
        print("1. 健康检查:")
        health = client.health_check()
        print(f"   状态: {health['status']}")
        print(f"   服务: {health['service']}\n")
        
        # 测试数学运算
        print("2. 数学运算测试:")
        add_result = client.add_numbers(10, 20)
        print(f"   10 + 20 = {add_result}")
        
        multiply_result = client.multiply_numbers(3.5, 4.2)
        print(f"   3.5 × 4.2 = {multiply_result}")
        
        power_result = client.power_numbers(2, 3)
        print(f"   2^3 = {power_result}\n")
        
        # 测试文本处理
        print("3. 文本处理测试:")
        text = "Hello World! 123"
        
        upper_result = client.process_text(text, "upper")
        print(f"   原文: {text}")
        print(f"   大写: {upper_result['processed_text']}")
        
        reverse_result = client.process_text(text, "reverse")
        print(f"   反转: {reverse_result['processed_text']}")
        
        clean_result = client.process_text(text, "clean")
        print(f"   清理: {clean_result['processed_text']}\n")
        
        # 测试数据统计
        print("4. 数据统计测试:")
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        stats = client.calculate_statistics(numbers)
        print(f"   数据: {numbers}")
        print(f"   平均值: {stats['mean']}")
        print(f"   中位数: {stats['median']}")
        print(f"   最大值: {stats['max']}")
        print(f"   最小值: {stats['min']}")
        print(f"   数量: {stats['count']}")
        
    except requests.exceptions.ConnectionError:
        print("❌ 无法连接到API服务器")
        print("请确保API服务器正在运行 (python main.py)")
    except Exception as e:
        print(f"❌ 发生错误: {e}")

if __name__ == "__main__":
    main()
