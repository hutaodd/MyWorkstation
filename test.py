import paddleocr

# 图片预处理
def preprocess(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges_image = cv2.Canny(gray_image, 100, 200)
    binary_image = cv2.threshold(edges_image, 127, 255, cv2.THRESH_BINARY)[1]

# 插件名称识别
def recognize_plugin_name(image):
    ocr = paddleocr.PaddleOCR(use_angle_cls=True)
    result = ocr.ocr(image)
    return result[0][0][1]

# 插件搜索
def search_plugin(plugin_name):
    url = f"https://marketplace.visualstudio.com/items?itemName={plugin_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text

# 插件安装
def install_plugin(plugin_name):
    vscode.commands.execute_command("workbench.extensions.installExtension", plugin_name)

# 主函数
def main():
    image = cv2.imread("image.png")
    preprocessed_image = preprocess(image)
    plugin_name = recognize_plugin_name(preprocessed_image)
    search_result = search_plugin(plugin_name)
    if search_result:
        install_plugin(plugin_name)
    else:
        print(f"未找到插件 {plugin_name}")

if __name__ == "__main__":
    main()
