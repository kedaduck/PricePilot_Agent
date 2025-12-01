from langchain_community.llms import Tongyi
from langchain.agents import initialize_agent, Tool, AgentType
from crawler import crawl_price

# 初始化大模型（使用通义千问，免费且快）
llm = Tongyi(
    model_name="qwen-max",  # 或 qwen-plus
    temperature=0.1         # 降低随机性，保证结果稳定
)

# 定义工具
price_tool = Tool(
    name="电商比价",
    func=crawl_price,
    description="查询指定商品在京东、淘宝、拼多多的价格、销量和好评率"
)

# 创建 Agent
agent = initialize_agent(
    tools=[price_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,          # 打印思考过程（调试用）
    max_iterations=3       # 防止无限循环
)

# 测试函数
def query_price(user_input: str) -> str:
    try:
        response = agent.run(user_input)
        return response
    except Exception as e:
        return f"查询出错: {str(e)}"