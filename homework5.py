import subprocess
import sys

def check_if_program_stops(script_path, timeout_sec):
    """
    嘗試運行指定的 Python 程式，並在 timeout_sec 秒內判斷其是否停機。
    
    :param script_path: 要運行的 Python 程式的路徑
    :param timeout_sec: 超時秒數
    :return: True 如果程式在指定時間內停機，False 表示可能不會停機
    """
    try:
        # 使用 subprocess.run 運行程式，並設置超時
        result = subprocess.run([sys.executable, script_path], timeout=timeout_sec, capture_output=True, text=True)
        print(f"程式已停機。返回碼：{result.returncode}")
        print(f"輸出結果：\n{result.stdout}")
        if result.stderr:
            print(f"錯誤訊息：\n{result.stderr}")
        return True
    except subprocess.TimeoutExpired:
        print(f"程式在 {timeout_sec} 秒內未停機，可能會無限運行。")
        return False
    except Exception as e:
        print(f"運行程式時發生錯誤：{e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("用法：python check_halt.py <script_path> <timeout_sec>")
        sys.exit(1)
    
    script = sys.argv[1]
    timeout = float(sys.argv[2])
    
    halted = check_if_program_stops(script, timeout)
    if halted:
        print("程式已成功停機。")
    else:
        print("程式可能不會停機或需要更長的運行時間。")

# 參考 gemini