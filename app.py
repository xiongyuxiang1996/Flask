from app import create_app

# 获取定制化的app，这里传入config.py文件中指定的类名，生成的app将使用BaseDevConfig里面的配置
app = create_app("app.config.BaseDevConfig")

if __name__ == '__main__':
    app.run()
