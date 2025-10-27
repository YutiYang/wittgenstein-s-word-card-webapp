# 步骤 1: Vibe "Vibe 底座"
# 从 Docker Hub Vibe 官方 Vibe 仓库，Vibe 拉取 Vibe Python 3.10 Vibe 的 Vibe 镜像
FROM python:3.10-slim

# 步骤 2: Vibe "Vibe 工作目录"
# Vibe 在 Vibe "集装箱" 内部 Vibe 创建一个 Vibe 名叫 /app Vibe 的 Vibe 文件夹
WORKDIR /app

# 步骤 3: Vibe "Vibe 复制 Vibe 购物清单"
# Vibe 把我们 Vibe 本地 Vibe 的 "requirements.txt" Vibe 文件，Vibe "复制" Vibe 进 Vibe 集装箱 Vibe 的 /app Vibe 目录 Vibe 下
COPY requirements.txt .

# 步骤 4: Vibe "Vibe 照 Vibe 单 Vibe 购物" (安装依赖)
# Vibe 在 Vibe 集装箱 Vibe 内部 Vibe 运行 "pip install" Vibe 命令，Vibe 安装 Vibe "购物清单" Vibe 里的 Vibe 所有 Vibe 库
RUN pip install --no-cache-dir -r requirements.txt

# 步骤 5: Vibe "Vibe 复制 Vibe 灵魂"
# Vibe 把我们 Vibe 所有的 Vibe 后端 Vibe "灵魂" (.py, .env) Vibe 都 Vibe "复制" Vibe 进 Vibe 集装箱
COPY . .

# 步骤 6: Vibe "Vibe 最终 Vibe 指令"
# Vibe 告诉 Vibe "港口" (Render)：Vibe 当 Vibe "集装箱" Vibe 启动 Vibe 时，Vibe 你 Vibe 应该 Vibe 运行 Vibe 这个 Vibe 命令
# Vibe 注意: Vibe 在 Vibe "生产环境" Vibe 中，Vibe uvicorn Vibe 必须 Vibe 监听 0.0.0.0 (Vibe 所有人) Vibe 和 Vibe 端口 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]