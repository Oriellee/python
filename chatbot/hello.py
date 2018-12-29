from flask import Flask, request

app = Flask(__name__)


@app.route('/')
class ChatBot():
    # 聊天机器人 http 请求处理逻辑
    def get(self, request):
        ask = request.args.get('ask')
        # 先获取url 参数值 如果没有值，返回 '你说啥'
        if ask:
            answer = get_momo_answer(ask)
            return text(answer)
        return text('你说啥?')
